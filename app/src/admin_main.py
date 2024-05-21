import dash
from dash import dcc, html, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import pandas as pd
from flask import Flask
from database.database_helper import database_helper

# Initialize the Flask server and the Dash app
server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# In-memory storage for demonstration purposes
admin_credentials = {'username': 'admin', 'password': 'admin123'}
clients_data = database_helper.get_all_user()
notices = database_helper.get_notice()


# Layout for login page

def get_login_layout():
    return dbc.Container([
        dbc.Row(dbc.Col(html.H2("Admin Login"), width=12, className="text-center")),
        dbc.Row(dbc.Col(dbc.Input(id="input-username", placeholder="Username", type="text"), width=4),
                className="mb-3"),
        dbc.Row(dbc.Col(dbc.Input(id="input-password", placeholder="Password", type="password"), width=4),
                className="mb-3"),
        dbc.Row(dbc.Col(dbc.Button("Login", id="login-button", n_clicks=0, color="primary"), width=4),
                className="mb-3"),
        dbc.Row(dbc.Col(html.Div(id="login-output"), width=12))
    ], className="mt-4")


def get_client_table_view(clients_data):
    return dbc.Table.from_dataframe(
        pd.DataFrame(
            {'ID': [d['id'] for d in clients_data], 'Password': [d['password'] for d in clients_data]}
        ),
        striped=True, bordered=True, hover=True, className="mt-3"
    )


# Layout for ID/Password management and status checking page
def get_id_passwd_status_layout():
    id_passwd_status_layout = dbc.Container([
        dbc.Row(dbc.Col(html.H2("ID/Password Management & Check Status"), width=12, className="text-center")),
        dbc.Row(
            dbc.Col(dbc.Input(id={"type": "new-client-id", "index": 0}, placeholder="Client ID", type="text"), width=4),
            className="mb-3"),
        dbc.Row(dbc.Col(
            dbc.Input(id={"type": "new-client-password", "index": 0}, placeholder="Client Password", type="password"),
            width=4), className="mb-3"),
        dbc.Row(dbc.Col(dbc.Button("Add/Update Client", id={"type": "add-update-client-button", "index": 0}, n_clicks=0,
                                   color="primary"), width=4), className="mb-3"),
        dbc.Row(dbc.Col(html.Div(id={"type": "id-passwd-output", "index": 0}), width=12), className="mb-3"),
        html.Hr(),
        html.H3("Current Clients"),
        html.Div(get_client_table_view(database_helper.get_all_user()), id={'type': 'clients-table', 'index': 0},
                 className='mt-3')
    ], className="mt-4")
    return id_passwd_status_layout


def get_set_period_layout():
    set_period_layout = dbc.Container([
        dbc.Row(dbc.Col(html.H2("Set Service Period"), width=12, className="text-center")),
        dbc.Row(dbc.Col(dcc.DatePickerRange(id={"type": "date-picker-range", "index": 0}), width=6), className="mb-3"),
        dbc.Row(
            dbc.Col(dbc.Button("Set Period", id={"type": "set-period-button", "index": 0}, n_clicks=0, color="primary"),
                    width=4), className="mb-3"),
        dbc.Row(dbc.Col(html.Div(id={"type": "set-period-output", "index": 0}), width=12), className="mb-3"),
    ], className="mt-4")
    return set_period_layout


def make_notice_view(notices):
    notice_view = [html.Li([
        html.Button('x', id={'type': 'delete-button', 'index': i},
                    style={'border': 'none', 'background': 'none', 'color': 'red', 'cursor': 'pointer',
                           'margin-right': '10px'}),
        f"{notice['head']}: {notice['body']}"], id=f'notice-{i}') for i, notice in enumerate(notices)]
    return notice_view


# Layout for notices page
def get_notices_layout():
    notices_layout = dbc.Container([
        dbc.Row(dbc.Col(html.H2("Notices"), width=12, className="text-center")),
        dbc.Row(dbc.Col(dbc.Textarea(id={"type": "notice-head", "index": 0}, placeholder="Enter notice head here...",
                                     style={"width": "100%", "height": "50%"}), width=6), className="mb-3"),
        dbc.Row(dbc.Col(dbc.Textarea(id={"type": "notice-text", "index": 0}, placeholder="Enter notice here...",
                                     style={"width": "100%"}), width=6), className="mb-3"),
        dbc.Row(
            dbc.Col(
                dbc.Button("Post Notice", id={"type": "post-notice-button", "index": 0}, n_clicks=0, color="primary"),
                width=4), className="mb-3"),
        dbc.Row(dbc.Col(html.Div(id={"type": "notice-output", "index": 0}), width=12), className="mb-3"),
        html.Hr(),
        html.H3("Current Notices"),
        html.Div(make_notice_view(database_helper.get_notice()), id={"type": "notices-list", "index": 0},
                 className='mt-3')
    ], className="mt-4")
    return notices_layout


# Layout for tabs
tabs_layout = html.Div([
    dcc.Tabs(id={'type': 'tabs', 'index': 0}, value='id-passwd-status', children=[
        dcc.Tab(label='ID/Password Management & Check Status', value='id-passwd-status'),
        dcc.Tab(label='Set Service Period', value='set-period'),
        dcc.Tab(label='Notices', value='notices'),
    ]),
    html.Div(id='tabs-content', className="p-4")
])

# Main layout with a hidden div to store the login status
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(id="page-content"),
    dcc.Store(id='login-status', data={'logged_in': False}),
    dcc.Store(id='dummy', data={})
])


# Callback for handling login
@app.callback(
    [Output('login-output', 'children'),
     Output('login-status', 'data'),
     Output('url', 'pathname')],
    Input('login-button', 'n_clicks'),
    [State('input-username', 'value'),
     State('input-password', 'value'),
     State('login-status', 'data')]
)
def handle_login(n_clicks, username, password, login_status):
    if n_clicks > 0:
        if username == admin_credentials['username'] and password == admin_credentials['password']:
            login_status['logged_in'] = True
            return "", login_status, "/dashboard"
        else:
            return "Invalid username or password", login_status, "/"
    return "", login_status, "/"


# Callback to update page content based on URL and login status
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname'),
    State('login-status', 'data')
)
def display_page(pathname, login_status):
    if not login_status['logged_in']:
        return get_login_layout()
    elif pathname == '/dashboard':
        return tabs_layout
    else:
        return get_login_layout()


# Callback to update tabs content
@app.callback(
    Output('tabs-content', 'children'),
    Input({'type': 'tabs', 'index': ALL}, 'value')
)
def render_tab_content(tab):
    tab = tab[0]
    if tab == 'id-passwd-status':
        return get_id_passwd_status_layout()
    elif tab == 'set-period':
        return get_set_period_layout()
    elif tab == 'notices':
        return get_notices_layout()
    return html.Div("404 Page Not Found")


# Callback to update the clients table on initial login and tab change
@app.callback(
    Output('dummy', 'data'),
    Input({'type': 'tabs', 'index': ALL}, 'value'),
    prevent_initial_call=True
)
def update_clients_table(tab):
    global clients_data, notices
    clients_data = database_helper.get_all_user()
    notices = database_helper.get_notice()
    return {}


# Callbacks for ID/Password management
@app.callback(
    [Output({'type': 'id-passwd-output', 'index': MATCH}, 'children'),
     Output({'type': 'clients-table', 'index': MATCH}, 'children', allow_duplicate=True)],
    Input({'type': 'add-update-client-button', 'index': MATCH}, 'n_clicks'),
    [State({'type': 'new-client-id', 'index': MATCH}, 'value'),
     State({'type': 'new-client-password', 'index': MATCH}, 'value')],
    prevent_initial_call=True
)
def manage_id_passwd(n_clicks, client_id, client_password):
    global clients_data
    if n_clicks > 0 and client_id and client_password:
        if client_id in [d['id'] for d in clients_data]:
            if database_helper.change_password({'user_id': client_id, 'pw': client_password}):
                client = [d for d in clients_data if d['id'] == client_id][0]
                client['password'] = client_password
            return get_client_table_view(clients_data), f"Updated password for {client_id}"
        else:
            new_client = {'id': client_id, 'password': client_password}
            if database_helper.add_user(new_client):
                clients_data.append(new_client)
                return get_client_table_view(clients_data), f"Added new client {client_id}"
            else:
                return dash.no_update, f"Error adding new client {client_id}"
    return dash.no_update, ""


# Callbacks for setting period
@app.callback(
    Output({'type': 'set-period-output', 'index': MATCH}, 'children'),
    Input({'type': 'set-period-button', 'index': MATCH}, 'n_clicks'),
    [State({'type': 'date-picker-range', 'index': MATCH}, 'start_date'),
     State({'type': 'date-picker-range', 'index': MATCH}, 'end_date')]
)
def set_period(n_clicks, start_date, end_date):
    if n_clicks > 0 and start_date and end_date:
        return f"Set period from {start_date} to {end_date}"
    return ""


# Callback to post notices
@app.callback(
    [Output({'type': 'notice-output', 'index': MATCH}, 'children'),
     Output({'type': 'notices-list', 'index': MATCH}, 'children', allow_duplicate=True)],
    Input({'type': 'post-notice-button', 'index': MATCH}, 'n_clicks'),
    [State({'type': 'notice-head', 'index': MATCH}, 'value'),
     State({'type': 'notice-text', 'index': MATCH}, 'value')],
    prevent_initial_call=True
)
def post_notice(n_clicks, notice_head, notice_text):
    if n_clicks and notice_text and notice_head:
        notice_time = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
        notice = {'head': notice_head, 'body': notice_text, 'time': notice_time, 'active': True}
        if database_helper.insert_notice(notice):
            notices.append(notice)
            return "Notice posted!", make_notice_view(notices)
        else:
            return "Error posting notice", make_notice_view(notices)
    return "", make_notice_view(notices)


# Callback to delete notices
@app.callback(
    Output({'type': 'notices-list', 'index': ALL}, 'children', allow_duplicate=True),
    Input({'type': 'delete-button', 'index': ALL}, 'n_clicks'),
    State({'type': 'delete-button', 'index': ALL}, 'id'),
    prevent_initial_call=True
)
def delete_notice(n_clicks, button_ids):
    for (n_click, btn_id) in zip(n_clicks, button_ids):
        if n_click:
            notice_index = btn_id['index']
            notice = notices[notice_index]
            if database_helper.deactivate_notice(notice):
                del notices[notice_index]
                return [make_notice_view(notices)]
    return [make_notice_view(notices)]


if __name__ == '__main__':
    app.run_server(debug=True, port="8051")
