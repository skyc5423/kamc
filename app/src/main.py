import dash
from dash import dcc, html, callback, MATCH, ALL, State
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app.src.dataclass.tabs import SubTabs
import plotly.graph_objects as go
import plotly.express as px

# from app.src.database.database_helper import fig

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

# Define the layout of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Loading(id='loading', type='circle', children=[html.Div(id='page-content')],
                loading_state={'is_loading': True, 'color': 'white'}),
])


@callback(Output('page-content', 'children'),
          [Input('url', 'pathname')])
def display_page(pathname):
    # if pathname == '/':
    from pages.login_page import LoginPage
    from pages.main_page import MainPage
    page = MainPage()
    # page = LoginPage()
    return page.get_layer()


@callback(
    Output({'type': 'tabs_sub', 'index': MATCH}, 'children'),
    Input({'type': 'tabs_main', 'index': MATCH}, 'value'),
    State({'type': 'tabs_main_store', 'index': MATCH}, 'data'),
    prevent_initial_call=True,
)
def change_tab(tab_values, tab_data):
    tab = [t for t in tab_data if t['value'] == tab_values][0]
    children = []
    for st in tab['sub_tabs']:
        st['parent_order'] = tab.get('order')
        children.append(SubTabs(**st).get_layer())
    return children


@callback(
    [Output({'type': 'main_graph', 'index': MATCH}, 'figure'),
     Output({'type': 'main_graph', 'index': MATCH}, 'style')],
    Input({'type': 'tabs_sub', 'index': MATCH}, 'active_tab'),
    [State({'type': 'tabs_main', 'index': MATCH}, 'value'),
     State({'type': 'tabs_main_store', 'index': MATCH}, 'data'),
     State({'type': 'main_graph', 'index': MATCH}, 'style')],
    prevent_initial_call=True,
)
def change_sub_tab(sub_tab_value, main_tab, tab_data, style):
    import pymongo
    from pymongo import MongoClient
    from pandas import DataFrame
    import plotly.express as px

    client = MongoClient('mongodb://kamc_root:kamc123456qwer!@43.201.146.205:19999/?authMechanism=DEFAULT')
    db = client['KAMC_EDU_학생']
    years = range(2018, 2021)
    data = []
    for y in years:
        collection = db[f'{y}_입학학생수']
        for doc in collection.find():
            univ = doc['대학명']
            male = doc['의예_남']
            female = doc['의예_여']
            data.append({'univ': univ, 'year': y, 'male': male, 'female': female})

    df = DataFrame(data)
    fig = px.pie(df, values='male', names='year')
    #
    # df = px.data.tips()
    # fig = px.pie(df, values='tip', names='day')

    style['display'] = 'block'
    return fig, style


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8050", debug=True)
