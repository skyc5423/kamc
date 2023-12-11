from dataclasses import dataclass
from dash import dcc
import dash_bootstrap_components as dbc


@dataclass
class Tabs:
    order: int
    name: str
    value: str
    sub_tabs: list

    def __init__(self, order, name, value, sub_tabs: list = None):
        self.order = order
        self.name = name
        self.value = value
        self.sub_tabs = []
        for sub_tab_arg in sub_tabs:
            sub_tab = SubTabs(**sub_tab_arg)
            sub_tab.set_parent_order(self.order)
            self.sub_tabs.append(sub_tab)

    def __lt__(self, other):
        return self.order < other.order

    def get_layer(self):
        return dcc.Tab(id=self.value, label=f"{self.order}. {self.name}", value=self.value)

    def set_sub_tabs(self, sub_tabs):
        for sub_tab in sub_tabs:
            sub_tab.set_parent_order(self.order)
        self.sub_tabs = sub_tabs


@dataclass
class SubTabs:
    order: int
    name: str
    value: str

    def __init__(self, order, name, value, parent_order=None):
        self.order = order
        self.name = name
        self.value = value
        self.parent_order = parent_order

    def set_parent_order(self, parent_order):
        self.parent_order = parent_order

    def __lt__(self, other):
        return self.order < other.order

    def get_layer(self):
        return dbc.Tab(label=f"{self.parent_order}-{self.order}. {self.name}", id=self.value,
                       label_style={'font-size': '12px'})
