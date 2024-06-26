from dash import Dash, dcc, html, callback, MATCH, State, ALL
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app.src.database.dataclass.tabs import SubTabs
import plotly.express as px
from database.database_helper import database_helper
from pages.main_page import MainPage
from pages.login_page import LoginPage
from util import get_page_content, total_state_list, total_state_key_dict, total_add_button_input, \
    total_add_button_state, total_add_button_output, visualize_state_dict, visualize_state_list, visualize_input_list, \
    visualize_output_list, extract_school
import json
import pandas as pd
import io
from database.dataclass.school import School
from flask import Flask, request

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

modal_load_year = dbc.Modal(
    [
        dbc.ModalHeader("데이터 불러오기"),
        dbc.ModalBody(
            html.Div([
                html.P("특정 연도의 데이터를 불러와서 현재 연도의 데이터에 덮어씌웁니다.", style={"text-align": "left"}),
                html.P("불러올 연도를 선택하고 Load 버튼을 눌러주세요.", style={"text-align": "left"}),
                dcc.Dropdown(
                    id='year_dropdown_modal',
                    options=[{'label': i, 'value': i} for i in range(2018, 2025)],
                    value=2024,
                    style={
                        "width": "150px",
                        "margin-left": "0",
                    }
                )
            ])
        ),
        dbc.ModalFooter(
            html.Div([
                dbc.Button("Load", id="load_modal_button", className="mr-2"),
                dbc.Button("Close", id="close_modal_button", className="ml-2")
            ], style={"display": "flex", "justify-content": "center", "gap": "10px"})
        ),
    ],
    id="modal",
    is_open=False,
    centered=True,
)

# Define the layout of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.H2('기본의학교육 데이터베이스',
            style={"margin-top": "5vh",
                   "text-align": "center"}),
    dbc.Col([
        dbc.Row([
            dbc.Col([dcc.Dropdown(id='year_dropdown',
                                  options=[{'label': i, 'value': i} for i in range(2018, 2025)],
                                  value=2024,
                                  style={
                                      "width": "16vh",
                                      "height": "5vh",
                                      "margin": "5vh",
                                      "text-align": "center",
                                      "display": "none"
                                  }), ], width=2),
            dbc.Col([
                dbc.Button("데이터 불러오기",
                           id="open_modal_button",
                           color="primary",
                           style={
                               "width": "16vh",
                               "height": "5vh",
                               "margin": "5vh",
                               "display": "none"
                           }), ], width='auto')
        ])
    ], align="center"),
    dbc.Col([html.Div(id='page-content')]),
    dbc.Col(
        id='col_add_button',
        children=[dbc.Button("Save",
                             id={
                                 'type': 'refresh',
                                 'index': 0
                             },
                             color="primary",
                             className="mr-1",
                             ), ],
        style={"margin-top": "5vh",
               "text-align": "center",
               "display": "none"}),
    dbc.Col([dbc.Alert("저장되었습니다.", color="success",
                       duration=5000,
                       id={
                           'type': 'alert',
                           'index': 0
                       }, dismissable=True, is_open=False)],
            style={"margin": "5vh"}),
    dcc.Store(id='school_name', data=""),
    dcc.Download(id={
        'type': 'download',
        'index': 0
    }),
    modal_load_year,
    dcc.Location(id='dummy-location', refresh=False),
    dcc.Store(id='popup-trigger'),
    dcc.Interval(
        id='interval-component',
        interval=10 * 1000,  # in milliseconds
        n_intervals=0
    ),
])
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <script type="text/javascript">
            function openPopup(url) {
                window.open(url, '_blank', 'width=600,height=400');
            }
        </script>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''


@app.server.route('/popup/<int:notice_id>')
def popup(notice_id):
    notices = database_helper.get_notice()
    if 0 <= notice_id < len(notices):
        notice = notices[notice_id]
        return f'''
        <!DOCTYPE html>
        <html>
            <head>
                <title> 공지사항 </title>
            </head>
            <body>
                <h2>{notice['head']}</h2>
                <p>{notice['body']}</p>
                <p>{notice['time']}</p>
            </body>
        </html>
        '''
    else:
        return "Notice not found", 404


@app.callback(
    Output("modal", "is_open", allow_duplicate=True),
    [Input("open_modal_button", "n_clicks")],
    [State("modal", "is_open")],
    prevent_initial_call=True
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open


@app.callback(
    Output("modal", "is_open", allow_duplicate=True),
    [Input("close_modal_button", "n_clicks")],
    [State("modal", "is_open")],
    prevent_initial_call=True
)
def close_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open


@app.callback(
    [Output("modal", "is_open", allow_duplicate=True)],
    [Input('load_modal_button', 'n_clicks')],
    [State('year_dropdown_modal', 'value'),
     State('year_dropdown', 'value'),
     State('school_name', 'data')],
    prevent_initial_call=True
)
def load_data(n_clicks, year_modal, year, school_name):
    try:
        selected_school = [school for school in
                           database_helper._get_data_from_school_name_year(school_name, year_modal)]
        target_school = [school for school in database_helper._get_data_from_school_name_year(school_name, year)]
        if len(target_school) == 0:
            if len(selected_school) == 0:
                new_school = School()
                setattr(new_school, '대학명', school_name)
                setattr(new_school, '연도', year)
                database_helper.update_school_data(new_school)
            else:
                source_school = selected_school[0]
                new_school = School()
                for attr_name in [d for d in dir(source_school) if not d.startswith('_')]:
                    setattr(new_school, attr_name, getattr(source_school, attr_name))
                setattr(new_school, '연도', year)
                database_helper.update_school_data(new_school)
        else:
            if len(selected_school) == 0:
                return [False]
            else:
                source_school = selected_school[0]
                target_school = target_school[0]
                for attr_name in [d for d in dir(source_school) if not d.startswith('_')]:
                    setattr(target_school, attr_name, getattr(source_school, attr_name))
                setattr(target_school, '연도', year)
                database_helper.update_school_data(target_school)
    except:
        return [True]
    return [False]


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
        if len(table_data[0]) != 0 and '합계' in table_data[0][-1].values():
            table_data[0].insert(-1, {c['id']: '' for c in table_column[0]})
        else:
            table_data[0].append({c['id']: '' for c in table_column[0]})
        button_input_n_clicks[i][0] = None

    return list(button_input_n_clicks) + list(table_datas)


@callback(Output({'type': 'alert', 'index': ALL}, 'is_open', allow_duplicate=True),
          [Input({'type': 'refresh', 'index': ALL}, 'n_clicks')],
          [State('school_name', 'data'), State('year_dropdown', 'value')] + total_state_list,
          prevent_initial_call=True
          )
def toggle_alert(n, school_name, year, *args):
    name_matched_school_list = [school for school in database_helper._get_data_from_school_name_year(school_name)]
    if len(name_matched_school_list) == 0:
        return [False]
    year_matched_school_list = [school for school in name_matched_school_list if getattr(school, '연도') == year]
    if len(year_matched_school_list) == 0:
        school = School()
        setattr(school, '대학명', school_name)
        setattr(school, '연도', year)
    else:
        school = year_matched_school_list[0]
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
        school = \
            [school for school in database_helper._get_data_from_school_name_year(school_name)][0]
        out = extract_school(school)
        return list(button_input_n_clicks) + [[out]]

    for i in range(button_num):
        if len(button_input_n_clicks[i]) == 0 or not button_input_n_clicks[i][0]:
            continue
        table_data = table_datas[i][0]
        button_input_n_clicks[i][0] = None
        graph_html = visualize_state_dict[i]['function'](school_name, table_data)
        file_name = visualize_state_dict[i]['file_name']
        return list(button_input_n_clicks) + [[dict(content=graph_html, filename=f"{file_name}.html")]]
    return list(button_input_n_clicks) + [[None]]


@callback(Output('page-content', 'children', allow_duplicate=True),
          [Input('url', 'pathname')],
          State('school_name', 'data'),
          prevent_initial_call=True)
def display_page(pathname, school_name):
    if school_name == '':
        return LoginPage().get_layer()
    page = MainPage()
    return page.get_layer()


@callback([Output('school_name', 'data'),
           Output('page-content', 'children', allow_duplicate=True),
           Output('year_dropdown', 'style'),
           Output('col_add_button', 'style'),
           Output('open_modal_button', 'style'),
           Output('popup-trigger', 'data')],
          [Input({'type': 'login_password_submit', 'index': ALL}, 'n_clicks'),
           Input('year_dropdown', 'value')],
          [State({'type': 'login_id', 'index': ALL}, 'value'),
           State({'type': 'login_password', 'index': ALL}, 'value'),
           State('year_dropdown', 'style'),
           State('school_name', 'data'),
           State('col_add_button', 'style'),
           State("open_modal_button", "style")],
          prevent_initial_call=True)
def login(n_clicks, year, school_name, password, style, saved_school_name, style_button, style_modal_button):
    if (len(school_name) < 1 or school_name[0] is None) and saved_school_name == '':
        return ['', LoginPage().get_layer(), style, style_button, style_modal_button, dash.no_update]

    user = database_helper.verify_login(school_name[0], password[0])
    if not user:
        return ['', LoginPage().get_layer(), style, style_button, style_modal_button, dash.no_update]

    style['display'] = 'block'
    style_button['display'] = 'block'
    style_modal_button['display'] = 'block'

    if len(school_name) < 1 or school_name[0] is None:
        school = saved_school_name
    else:
        school = school_name[0]

    notices = database_helper.get_notice()  # Fetch latest notices
    popups_to_open = [f'/popup/{i}' for i in range(len(notices))]

    return [school, MainPage().get_layer(), style, style_button, style_modal_button, popups_to_open]


app.clientside_callback(
    """
    function(triggers) {
        if (Array.isArray(triggers)) {
            triggers.forEach(url => openPopup(url));
        }
        return "";
    }
    """,
    Output('dummy-location', 'pathname'),
    Input('popup-trigger', 'data')
)


@callback(
    [Output({'type': 'tabs_sub', 'index': MATCH}, 'children'),
     Output({'type': 'tabs_main_content', 'index': MATCH}, 'children'),
     Output({'type': 'tabs_main_store', 'index': MATCH}, 'data'),
     Output({'type': 'tabs_sub', 'index': MATCH}, 'active_tab')],
    [Input({'type': 'tabs_main', 'index': MATCH}, 'value'),
     Input({'type': 'tabs_sub', 'index': MATCH}, 'active_tab'),
     Input("modal", "is_open")],
    [State({'type': 'tabs_main_store', 'index': MATCH}, 'data'),
     State('school_name', 'data'),
     State('year_dropdown', 'value')],
)
def change_tab_value(main_tab_value, sub_tab_value, modal_open, tab_data, school_name, year):
    tab = [t for t in tab_data if t['value'] == main_tab_value][0]
    if tab['last_selected']:
        sub_tabs = []
        for st in tab['sub_tabs']:
            st['parent_order'] = tab.get('order')
            sub_tabs.append(SubTabs(**st).get_layer())
        sub_tab = [st for st in tab['sub_tabs'] if st['order'] == int(sub_tab_value.split('-')[1]) + 1][0]['value']
        main_content = get_page_content(main_tab_value, sub_tab, school_name, year)
    else:
        sub_tabs = []
        for t in tab_data:
            t['last_selected'] = False
        tab['last_selected'] = True
        for st in tab['sub_tabs']:
            st['parent_order'] = tab.get('order')
            sub_tabs.append(SubTabs(**st).get_layer())
        sub_tab = [st for st in tab['sub_tabs'] if st['order'] == 1][0]['value']
        main_content = get_page_content(main_tab_value, sub_tab, school_name, year)
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
