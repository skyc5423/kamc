import dash
from dash import dcc, html, callback, MATCH, State, ALL
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app.src.database.dataclass.tabs import SubTabs
import plotly.express as px
from database.database_helper import school_list
from pages.main_page import MainPage
from pages.login_page import LoginPage
from util import get_page_content, total_state_list, total_state_key_dict, total_add_button_input, \
    total_add_button_state, total_add_button_output, visualize_state_dict, visualize_state_list, visualize_input_list, \
    visualize_output_list, extract_school
import json
from database.database_helper import database_helper
import pandas as pd
import io

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

# Define the layout of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.H2('기본의학교육 데이터베이스',
            style={"margin-top": "5vh",
                   "text-align": "center"}),
    dbc.Col([html.Div(id='page-content')]),
    dbc.Col([dbc.Button("Save", id={
        'type': 'refresh',
        'index': 0
    }, color="primary", className="mr-1"), ],
            style={"margin-top": "5vh",
                   "text-align": "center"}),
    dbc.Col([dbc.Alert("저장되었습니다.", color="success",
                       duration=3000,
                       id={
                           'type': 'alert',
                           'index': 0
                       }, dismissable=True, is_open=False)],
            style={"margin": "5vh"}),
    dcc.Store(id='school_name', data="서울"),
    dcc.Download(id={
        'type': 'download',
        'index': 0
    })
])


@callback(total_add_button_output,
          total_add_button_input,
          total_add_button_state,
          prevent_initial_call=True)
def add_row(*args):
    button_num = len(args) // 3
    button_input_n_clicks = args[:button_num]
    table_datas = args[button_num::2]
    table_columns = args[button_num + 1::2]
    for i in range(button_num):
        if len(button_input_n_clicks[i]) == 0 or not button_input_n_clicks[i][0]:
            continue
        table_data = table_datas[i]
        table_column = table_columns[i]
        if '합계' in table_data[0][-1].values():
            table_data[0].insert(-1, {c['id']: '' for c in table_column[0]})
        else:
            table_data[0].append({c['id']: '' for c in table_column[0]})
        button_input_n_clicks[i][0] = None

    return list(button_input_n_clicks) + list(table_datas)


@callback(Output({'type': 'alert', 'index': ALL}, 'is_open', allow_duplicate=True),
          [Input({'type': 'refresh', 'index': ALL}, 'n_clicks')],
          [State('school_name', 'data')] + total_state_list,
          prevent_initial_call=True
          )
def toggle_alert(n, school_name, *args):
    school = [school for school in school_list if getattr(school, '대학명') == school_name][0]
    for arg, key_dict in zip(args, total_state_key_dict):
        if len(arg) == 0:
            continue
        arg = arg[0]
        if isinstance(arg, list):
            arg = json.dumps(arg, ensure_ascii=False)
        attr_name = key_dict['state_name']
        setattr(school, attr_name, arg)
    try:
        database_helper.update_school_data(school)
        return [True]
    except Exception as e:
        print(e)
        return [False]


@callback(
    visualize_output_list + [Output({'type': "download", 'index': ALL}, "data")],
    [Input({'type': 'db_extraction', 'index': ALL}, "n_clicks")] + visualize_input_list,
    [State('school_name', 'data')] + visualize_state_list,
    prevent_initial_call=True,
)
def func(db_extract_clicked, *args):
    button_num = len(args) // 2
    button_input_n_clicks = args[:button_num]
    table_datas = args[button_num + 1:]
    school_name = args[button_num]
    if len(db_extract_clicked) > 0 and db_extract_clicked[0]:
        school = [school for school in school_list if getattr(school, '대학명') == school_name][0]
        out = extract_school(school)
        return list(button_input_n_clicks) + [[out]]

    for i in range(button_num):
        if len(button_input_n_clicks[i]) == 0 or not button_input_n_clicks[i][0]:
            continue
        table_data = table_datas[i][0]
        button_input_n_clicks[i][0] = None
        graph_html = visualize_state_dict[i]['function'](table_data)
        file_name = visualize_state_dict[i]['file_name']
        return list(button_input_n_clicks) + [[dict(content=graph_html, filename=f"{file_name}.html")]]
    return list(button_input_n_clicks) + [[None]]


@callback(Output('page-content', 'children'),
          [Input('url', 'pathname')])
def display_page(pathname):
    page = MainPage()
    return page.get_layer()


@callback(
    [Output({'type': 'tabs_sub', 'index': MATCH}, 'children'),
     Output({'type': 'tabs_main_content', 'index': MATCH}, 'children'),
     Output({'type': 'tabs_main_store', 'index': MATCH}, 'data'),
     Output({'type': 'tabs_sub', 'index': MATCH}, 'active_tab')],
    [Input({'type': 'tabs_main', 'index': MATCH}, 'value'),
     Input({'type': 'tabs_sub', 'index': MATCH}, 'active_tab')],
    [State({'type': 'tabs_main_store', 'index': MATCH}, 'data'),
     State('school_name', 'data')],
)
def change_tab_value(main_tab_value, sub_tab_value, tab_data, school_name):
    tab = [t for t in tab_data if t['value'] == main_tab_value][0]
    if tab['last_selected']:
        sub_tabs = []
        for st in tab['sub_tabs']:
            st['parent_order'] = tab.get('order')
            sub_tabs.append(SubTabs(**st).get_layer())
        sub_tab = [st for st in tab['sub_tabs'] if st['order'] == int(sub_tab_value.split('-')[1]) + 1][0]['value']
        main_content = get_page_content(main_tab_value, sub_tab, school_list, school_name)
    else:
        sub_tabs = []
        for t in tab_data:
            t['last_selected'] = False
        tab['last_selected'] = True
        for st in tab['sub_tabs']:
            st['parent_order'] = tab.get('order')
            sub_tabs.append(SubTabs(**st).get_layer())
        sub_tab = [st for st in tab['sub_tabs'] if st['order'] == 1][0]['value']
        main_content = get_page_content(main_tab_value, sub_tab, school_list, school_name)
        sub_tab_value = 'tab-0'
    return sub_tabs, main_content, tab_data, sub_tab_value


@callback(
    Output({'index': MATCH, 'type': 'collapse'}, "is_open"),
    [Input({'index': MATCH, 'type': 'toggle'}, "n_clicks")],
    [State({'index': MATCH, 'type': 'collapse'}, "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8050", debug=True)
