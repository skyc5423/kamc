from dash import dcc, html
from app.src.database.dataclass.tabs import Tabs
from app.src.resource.predefined_tabs import TAB_ARGS
import dash_bootstrap_components as dbc
import dataclasses


class MainPage:

    def __init__(self):
        self.tabs = []
        for tab_arg in TAB_ARGS:
            tab = Tabs(**tab_arg)
            self.tabs.append(tab)
        pass

    def get_layer(self):
        children = [dcc.Tabs(id={'index': 0, 'type': 'tabs_main'},
                             value=self.tabs[0].value,
                             children=[tab.get_layer() for tab in self.tabs]),
                    dbc.Tabs(id={'index': 0, 'type': 'tabs_sub'},
                             children=[sub_tab.get_layer() for sub_tab in self.tabs[0].sub_tabs]),
                    dcc.Loading(id='loading', type='circle',
                                children=[html.Div(id={'index': 0, 'type': 'tabs_main_content'})],
                                loading_state={'is_loading': True, 'color': 'white'}),
                    dcc.Store(id={'index': 0, 'type': 'tabs_main_store'},
                              data=[dataclasses.asdict(tab) for tab in self.tabs])]
        return html.Div(children)
