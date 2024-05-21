import dash
from dash import dcc, html, Dash
from dash.dependencies import Input, Output

# Initialize the Dash app
app = Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.Button("Open Popup 1", id="open-popup-1"),
    dcc.Location(id='dummy-location', refresh=False)
])

# Include the JavaScript for opening popups
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

# Callback to open Popup 1
@app.callback(
    Output('dummy-location', 'href'),
    Input('open-popup-1', 'n_clicks'),
    prevent_initial_call=True
)
def open_popup_1(n_clicks):
    if n_clicks:
        return dash.no_update
    return dash.no_update

app.clientside_callback(
    """
    function(n_clicks) {
        if (n_clicks) {
            openPopup('/popup1');
        }
        return "";
    }
    """,
    Output('dummy-location', 'pathname'),
    Input('open-popup-1', 'n_clicks')
)

# Define the popup content pages
@app.server.route('/popup1')
def popup1():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Popup 1</title>
        </head>
        <body>
            <h2>Popup 1</h2>
            <p>This is the content of Popup 1</p>
        </body>
    </html>
    '''

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
