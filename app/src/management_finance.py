from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
from app.src.resource.predefined_tabs import TAB_ARGS
from PIL import Image
import json


def sub_tab_management_finance_professor_development(school):
    educational_competency_enhancement_support_policy_presence = getattr(school, "교육역량_강화지원_정책_유무", "있음")
    professional_competency_enhancement_support_policy_presence = getattr(school, "전문역량_강화지원_정책_유무", "없음")
    management_finance_budget = getattr(school, "경영재정_역량개발_예산액", None)
    management_finance_budget_execution = getattr(school, "경영재정_역량개발_집행액", None)
    layer = dbc.Col([
        dbc.Row(
            [dbc.Col([html.H6('교육역량 강화 지원 정책 유무', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'),
             dbc.Col([dbc.RadioItems(
                 id={"type": "educational_competency_enhancement_support_policy_presence", "index": 0},
                 options=[{'label': ' 있음', 'value': '있음'}, {'label': ' 없음', 'value': '없음'}],
                 value=educational_competency_enhancement_support_policy_presence,
                 inline=True)], width='auto')],
            align='center',
            className='custom-row'),
        dbc.Row(
            [dbc.Col([html.H6('전문역량 강화 지원 정책 유무', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'),
             dbc.Col([dbc.RadioItems(
                 id={"type": "professional_competency_enhancement_support_policy_presence", "index": 0},
                 options=[{'label': ' 있음', 'value': '있음'}, {'label': ' 없음', 'value': '없음'}],
                 value=professional_competency_enhancement_support_policy_presence,
                 inline=True)], width='auto')],
            align='center',
            className='custom-row'),
        dbc.Row([dbc.Col([html.H6('예산액', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'),
                 dbc.Col([dbc.Input(
                     id={"type": "management_finance_budget", "index": 0},
                     value=management_finance_budget, type="number"), ], width=1),
                 dbc.Col([html.P('천원', style={'text-align': 'left', 'margin-top': '12px'})])],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('집행액', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'),
                 dbc.Col([dbc.Input(
                     id={"type": "management_finance_budget_execution", "index": 0},
                     value=management_finance_budget_execution, type="number"), ], width=1),
                 dbc.Col([html.P('천원', style={'text-align': 'left', 'margin-top': '12px'})])],
                align='center',
                className='custom-row'),
    ],
        className='custom-col')
    return layer


def sub_tab_management_finance_student_education(school):
    management_finance_student_education = json.loads(getattr(school, "학생교육_관련_비용", "[]"))
    management_finance_student_education_columns = \
        [
            {"name": ["항목"], "id": "항목"},
            {"name": ["의예과 1학년"], "id": "의예과_1학년"},
            {"name": ["의예과 2학년"], "id": "의예과_2학년"},
            {"name": ["의예과 1~4학년"], "id": "의학과"},
            {"name": ["연간비용 (천원)"], "id": "연간비용"},
            {"name": ["비고"], "id": "비고"},
        ]
    management_finance_student_education_table = dash_table.DataTable(
        id={'index': 0, 'type': 'management_finance_student_education'},
        columns=(management_finance_student_education_columns),
        data=management_finance_student_education,
        editable=True,
        row_deletable=True,
        style_header={
            'backgroundColor': 'rgb(160, 220, 255)',
            'fontWeight': 'bold',
            'textAlign': 'center',
            'font-size': '13px'
        },
        style_cell={
            'textAlign': 'center',
            'padding': '3px',
            'font-size': '12px',
            'minWidth': '100px',
        },
        style_table={
            'border': '0px',
            'overflowY': 'auto',
            'overflowX': 'auto'
        },
        merge_duplicate_headers=True
    )
    layer = dbc.Col([
        dbc.Row(
            [dbc.Col([management_finance_student_education_table], width='auto'), ]),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_management_finance_student_education'},
                        color="primary",
                        style={'margin-top': '10px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_management_finance_student_tuition(school):
    management_finance_student_tuition_medical_school = json.loads(getattr(school, "학생등록금_의과대학", "[]"))
    management_finance_student_tuition_graduate_medicine = json.loads(getattr(school, "학생등록금_의학전문대학원", "[]"))
    management_finance_student_tuition_medical_school_columns = \
        [
            {"name": ["과정"], "id": "과정"},
            {"name": ["학년"], "id": "학년"},
            {"name": ["1학기 (천원)"], "id": "1학기"},
            {"name": ["2학기 (천원)"], "id": "2학기"},
        ]
    management_finance_student_tuition_medical_school_table = dash_table.DataTable(
        id={'index': 0, 'type': 'management_finance_student_tuition_medical_school'},
        columns=(management_finance_student_tuition_medical_school_columns),
        data=management_finance_student_tuition_medical_school,
        editable=True,
        row_deletable=True,
        style_header={
            'backgroundColor': 'rgb(160, 220, 255)',
            'fontWeight': 'bold',
            'textAlign': 'center',
            'font-size': '13px'
        },
        style_cell={
            'textAlign': 'center',
            'padding': '3px',
            'font-size': '12px',
            'minWidth': '100px',
        },
        style_table={
            'border': '0px',
            'overflowY': 'auto',
            'overflowX': 'auto'
        },
        merge_duplicate_headers=True
    )
    management_finance_student_tuition_graduate_medicine_columns = \
        [
            {"name": ["학년"], "id": "학년"},
            {"name": ["1학기 (천원)"], "id": "1학기"},
            {"name": ["2학기 (천원)"], "id": "2학기"},
        ]
    management_finance_student_tuition_graduate_medicine_table = dash_table.DataTable(
        id={'index': 0, 'type': 'management_finance_student_tuition_graduate_medicine'},
        columns=(management_finance_student_tuition_graduate_medicine_columns),
        data=management_finance_student_tuition_graduate_medicine,
        editable=True,
        row_deletable=True,
        style_header={
            'backgroundColor': 'rgb(160, 220, 255)',
            'fontWeight': 'bold',
            'textAlign': 'center',
            'font-size': '13px'
        },
        style_cell={
            'textAlign': 'center',
            'padding': '3px',
            'font-size': '12px',
            'minWidth': '100px',
        },
        style_table={
            'border': '0px',
            'overflowY': 'auto',
            'overflowX': 'auto'
        },
        merge_duplicate_headers=True
    )
    layer = dbc.Col([
        dbc.Row(
            [dbc.Col([html.H6('의과대학', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'), ]),
        dbc.Row(
            [dbc.Col([management_finance_student_tuition_medical_school_table], width='auto'), ]),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_management_finance_student_tuition_medical_school'},
                        color="primary",
                        style={'margin-top': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_management_finance_student_tuition_medical_school'},
                        color="primary",
                        style={'margin-top': '10px', 'margin-left': '20px'})])]),
        html.Hr(),
        dbc.Row(
            [dbc.Col([html.H6('의학전문대학원', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'), ]),
        dbc.Row(
            [dbc.Col([management_finance_student_tuition_graduate_medicine_table], width='auto'), ]),
        dbc.Row([dbc.Col(
            [dbc.Button("추가",
                        id={'index': 0, 'type': 'add_management_finance_student_tuition_graduate_medicine'},
                        color="primary",
                        style={'margin-top': '10px'}
                        ),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_management_finance_student_tuition_graduate_medicine'},
                        color="primary",
                        style={'margin-top': '10px', 'margin-left': '20px'})])]),
    ],
        className='custom-col')
    return layer
