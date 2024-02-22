from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
from app.src.resource.predefined_tabs import TAB_ARGS
from PIL import Image
import json


def sub_tab_student_admission_system(school):
    student_admission_system_manager = json.loads(getattr(school, '입학업무_담당', "[]"))
    student_admission_system_manager_etc = getattr(school, '입학업무_담당_기타', None)
    rolling_student_admission_system_data = json.loads(getattr(school, '입학제도_수시모집', "[]"))
    regular_student_admission_system_data = json.loads(getattr(school, '입학제도_정시모집', "[]"))
    student_admission_system_columns = \
        [{"name": ["", "정원구분"], "id": "정원구분"},
         {"name": ["", "선발전형"], "id": "선발전형"},
         {"name": ["시행 여부", "시행"], "id": "시행"},
         {"name": ["시행 여부", "미시행"], "id": "미시행"},
         {"name": ["", "모집 정원 (명)"], "id": "모집정원"},
         {"name": ["면접 유무", "있음"], "id": "면접_있음"},
         {"name": ["면접 유무", "없음"], "id": "면접_없음"},
         {"name": ["면접 방법", "인성 면접"], "id": "면접방법_인성면접"},
         {"name": ["면접 방법", "적성 면접"], "id": "면접방법_적성면접"},
         {"name": ["면접 방법", "학업역량 면접"], "id": "면접방법_학업역량면접"},
         {"name": ["면접 방법", "인적성 면접"], "id": "면접방법_인적성면접"},
         {"name": ["면접 방법", "다면인적성 면접"], "id": "면접방법_다면인적성면접"},
         {"name": ["면접 방법", "서류확인 면접"], "id": "면접방법_서류확인면접"},
         {"name": ["면접 방법", "출제문항 면접"], "id": "면접방법_출제문항면접"},
         {"name": ["", "특별전형 해당 유무"], "id": "특별전형_해당유무"}]

    rolling_table = dash_table.DataTable(
        id={'type': 'rolling_student_admission_system_data', 'index': 0},
        columns=student_admission_system_columns,
        data=rolling_student_admission_system_data,
        editable=True,
        row_deletable=True,
        style_header={
            'backgroundColor': 'rgb(160, 220, 255)',
            'fontWeight': 'bold',
            'textAlign': 'center',
            'font-size': '11px'
        },
        style_cell={
            'textAlign': 'center',
            'padding': '3px',
            'font-size': '10px'
        },
        style_table={
            'border': '0px',
            'overflowY': 'auto',
            'overflowX': 'auto'
        },
        merge_duplicate_headers=True
    )
    regular_table = dash_table.DataTable(
        id={'type': 'regular_student_admission_system_data', 'index': 0},
        columns=student_admission_system_columns,
        data=regular_student_admission_system_data,
        editable=True,
        row_deletable=True,
        style_header={
            'backgroundColor': 'rgb(160, 220, 255)',
            'fontWeight': 'bold',
            'textAlign': 'center',
            'font-size': '11px'
        },
        style_cell={
            'textAlign': 'center',
            'padding': '3px',
            'font-size': '10px'
        },
        style_table={
            'border': '0px',
            'overflowY': 'auto',
            'overflowX': 'auto'
        },
        merge_duplicate_headers=True
    )
    layer = dbc.Col([
        dbc.Row([dbc.Col([html.H6('입학업무 담당', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.Checklist(id={'index': 0, 'type': 'student_admission_system_manager'},
                                        options=[{'label': ' 대학본부', 'value': '대학본부'},
                                                 {'label': ' 의과대학(의학전문대학원)', 'value': '의과대학'},
                                                 {'label': ' 기타', 'value': '기타'}],
                                        value=student_admission_system_manager,
                                        inline=True,
                                        labelStyle={'margin-right': '20px',
                                                    'margin-left': '10px'})],
                         align='center', width='auto'),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'student_admission_system_manager_etc'},
                                    value=student_admission_system_manager_etc,
                                    size="10px")], width='auto')
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row(
            [dbc.Col([html.H6('수시모집', style={'text-align': 'center', 'margin-top': '5px'})],
                     align='center',
                     className='custom-row'
                     ), ]),
        dbc.Row([dbc.Col([rolling_table])],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_rolling_student_admission_system_data'},
                        color="primary",
                        style={'margin-bottom': '10px'})])]),
        html.Hr(),
        dbc.Row(
            [dbc.Col([html.H6('정시모집', style={'text-align': 'center', 'margin-top': '5px'})],
                     align='center',
                     className='custom-row'
                     ), ]),
        dbc.Row([dbc.Col([regular_table])],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_regular_student_admission_system_data'},
                        color="primary",
                        style={'margin-bottom': '10px'})])]),
        html.Hr(),
    ],
        className='custom-col')
    return layer


def sub_tab_student_admission_student(school):
    student_admission_student = json.loads(getattr(school, '입학학생수', "[]"))
    columns = [
        {'id': '구분', 'name': '구분'},
        {'id': '성별', 'name': '성별'},
        {'id': '의예과', 'name': '의예과'},
        {'id': '의전원', 'name': '의전원'},
        {'id': '편입학', 'name': '편입학'},
        {'id': '합계', 'name': '합계'}]

    in_bound_table = dash_table.DataTable(
        id={'index': 0, 'type': 'student_admission_student'},
        columns=(columns),
        data=student_admission_student,
        editable=True,
        row_deletable=True,
        style_header={
            'backgroundColor': 'rgb(160, 220, 255)',
            'fontWeight': 'bold',
            'textAlign': 'center',
            'font-size': '11px'
        },
        style_cell={
            'textAlign': 'center',
            'padding': '3px',
            'font-size': '10px',
            'minWidth': '100px'
        },
        style_table={
            'border': '0px'
        }
    )

    layer = dbc.Col([
        dbc.Row([dbc.Col([in_bound_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_student_admission_student'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_student_admission_student'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_student_enrolled_student(school):
    student_enrolled_student = json.loads(getattr(school, '재적학생수', "[]"))

    student_enrolled_student_columns = \
        [{"name": ["", "", "구분"], "id": "구분"},
         {"name": ["", "", "성별"], "id": "성별"},
         {"name": ["의예과", "1학년", "1학기"], "id": "의예과_1학년_1학기"},
         {"name": ["의예과", "1학년", "2학기"], "id": "의예과_1학년_2학기"},
         {"name": ["의예과", "2학년", "1학기"], "id": "의예과_2학년_1학기"},
         {"name": ["의예과", "2학년", "2학기"], "id": "의예과_2학년_2학기"},
         {"name": ["의학과/의전원", "1학년", "1학기"], "id": "의학과_1학년_1학기"},
         {"name": ["의학과/의전원", "1학년", "2학기"], "id": "의학과_1학년_2학기"},
         {"name": ["의학과/의전원", "2학년", "1학기"], "id": "의학과_2학년_1학기"},
         {"name": ["의학과/의전원", "2학년", "2학기"], "id": "의학과_2학년_2학기"},
         {"name": ["의학과/의전원", "3학년", "1학기"], "id": "의학과_3학년_1학기"},
         {"name": ["의학과/의전원", "3학년", "2학기"], "id": "의학과_3학년_2학기"},
         {"name": ["의학과/의전원", "4학년", "1학기"], "id": "의학과_4학년_1학기"},
         {"name": ["의학과/의전원", "4학년", "2학기"], "id": "의학과_4학년_2학기"},
         ]

    student_enrolled_student_table = dash_table.DataTable(
        id={'index': 0, 'type': 'student_enrolled_student'},
        columns=(student_enrolled_student_columns),
        data=student_enrolled_student,

        editable=True,
        row_deletable=True,
        style_header={
            'backgroundColor': 'rgb(160, 220, 255)',
            'fontWeight': 'bold',
            'textAlign': 'center',
            'font-size': '11px'
        },
        style_cell={
            'textAlign': 'center',
            'padding': '3px',
            'font-size': '10px',
            'minWidth': '100px'
        },
        style_table={
            'border': '0px',
            'overflowY': 'auto',
            'overflowX': 'auto'
        },
        merge_duplicate_headers=True
    )

    layer = dbc.Col([
        dbc.Row([dbc.Col([student_enrolled_student_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_student_enrolled_student'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_student_enrolled_student'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_student_admission_student_structure(school):
    student_admission_student_structure = json.loads(getattr(school, '의예과입학학생구성', "[]"))
    student_admission_student_structure_columns = \
        [
            {"name": ["입학전형"], "id": "입학전형"},
            {"name": ["당해연도 고교졸업생 수"], "id": "당해연도 고교졸업생 수"},
            {"name": ["총 입학생 수"], "id": "총 입학생 수"},
            {"name": ["총 입학생 대비 비율(%)"], "id": "총 입학생 대비 비율(%)"},
        ]

    student_admission_student_structure_table = dash_table.DataTable(
        id={'index': 0, 'type': 'student_admission_student_structure'},
        columns=(student_admission_student_structure_columns),
        data=student_admission_student_structure,
        editable=True,
        row_deletable=True,
        style_header={
            'backgroundColor': 'rgb(160, 220, 255)',
            'fontWeight': 'bold',
            'textAlign': 'center',
            'font-size': '11px'
        },
        style_cell={
            'textAlign': 'center',
            'padding': '3px',
            'font-size': '10px',
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
        dbc.Row([dbc.Col([student_admission_student_structure_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_student_admission_student_structure'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             # dbc.Button("시각화",
             #            id={'index': 0, 'type': 'visualize_student_admission_student_structure'},
             #            color="primary",
             #            style={'margin-bottom': '10px', 'margin-left': '20px'})
             ])]),
    ],
        className='custom-col')
    return layer


def sub_tab_student_scholarship(school):
    student_scholarship = json.loads(getattr(school, '장학금수혜현황', "[]"))
    student_scholarship_columns = \
        [
            {"name": ["", "구분"], "id": "구분"},
            {"name": ["의예과", "총 수혜학생 수"], "id": "의예과_수혜학생"},
            {"name": ["의예과", "총 수혜금액 (천원)"], "id": "의예과_수혜금액"},
            {"name": ["의예과", "비고"], "id": "의예과_비고"},
            {"name": ["의학과", "총 수혜학생 수"], "id": "의학과_수혜학생"},
            {"name": ["의학과", "총 수혜금액 (천원)"], "id": "의학과_수혜금액"},
            {"name": ["의학과", "비고"], "id": "의학과_비고"},
        ]

    student_scholarship_table = dash_table.DataTable(
        id={'index': 0, 'type': 'student_scholarship'},
        columns=(student_scholarship_columns),
        data=student_scholarship,
        editable=True,
        row_deletable=True,
        style_header={
            'backgroundColor': 'rgb(160, 220, 255)',
            'fontWeight': 'bold',
            'textAlign': 'center',
            'font-size': '11px'
        },
        style_cell={
            'textAlign': 'center',
            'padding': '3px',
            'font-size': '10px',
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
        dbc.Row([dbc.Col([student_scholarship_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_student_scholarship'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_student_scholarship'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_student_graduate_career(school):
    student_graduate_career = json.loads(getattr(school, '졸업생의진로', "[]"))
    student_graduate_career_columns = \
        [
            {"name": ["", "인턴 수련"], "id": "인턴수련"},
            {"name": ["대학원 진학", "기초의학"], "id": "대학원_기초의학"},
            {"name": ["대학원 진학", "타분야"], "id": "대학원_타분야"},
            {"name": ["", "군입대"], "id": "군입대"},
            {"name": ["", "개원/봉직"], "id": "개원/봉직"},
            {"name": ["", "타 분야"], "id": "타분야"},
            {"name": ["", "미취업"], "id": "미취업"},
            {"name": ["", "미상"], "id": "미상"},
            {"name": ["", "기타"], "id": "기타"},
            {"name": ["", "합계"], "id": "합계"},
        ]

    student_graduate_career_table = dash_table.DataTable(
        id={'index': 0, 'type': 'student_graduate_career'},
        columns=(student_graduate_career_columns),
        data=student_graduate_career,
        editable=True,
        row_deletable=True,
        style_header={
            'backgroundColor': 'rgb(160, 220, 255)',
            'fontWeight': 'bold',
            'textAlign': 'center',
            'font-size': '11px'
        },
        style_cell={
            'textAlign': 'center',
            'padding': '3px',
            'font-size': '10px',
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
        dbc.Row([dbc.Col([student_graduate_career_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_student_graduate_career'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_student_graduate_career'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_student_graduate_student(school):
    student_graduate_student_basic_domestic = json.loads(getattr(school, '의학계열_대학원_학생_수_기초의학_내국인', "[]"))
    student_graduate_student_basic_foreigner = json.loads(getattr(school, '의학계열_대학원_학생_수_기초의학_외국인', "[]"))
    student_graduate_student_clinical_domestic = json.loads(getattr(school, '의학계열_대학원_학생_수_임상의학_내국인', "[]"))
    student_graduate_student_clinical_foreigner = json.loads(getattr(school, '의학계열_대학원_학생_수_임상의학_외국인', "[]"))
    student_graduate_student_columns = \
        [
            {"name": ["", "", "전공 분야"], "id": "전공분야"},
            {"name": ["석사과정", "입학생 수", "의사"], "id": "석사_입학생_의사"},
            {"name": ["석사과정", "입학생 수", "비의사"], "id": "석사_입학생_비의사"},
            {"name": ["석사과정", "재학생 수", "의사"], "id": "석사_재학생_의사"},
            {"name": ["석사과정", "재학생 수", "비의사"], "id": "석사_재학생_비의사"},
            {"name": ["석사과정", "졸업생 수", "의사"], "id": "석사_졸업생_의사"},
            {"name": ["석사과정", "졸업생 수", "비의사"], "id": "석사_졸업생_비의사"},
            {"name": ["박사과정", "입학생 수", "의사"], "id": "박사_입학생_의사"},
            {"name": ["박사과정", "입학생 수", "비의사"], "id": "박사_입학생_비의사"},
            {"name": ["박사과정", "재학생 수", "의사"], "id": "박사_재학생_의사"},
            {"name": ["박사과정", "재학생 수", "비의사"], "id": "박사_재학생_비의사"},
            {"name": ["박사과정", "졸업생 수", "의사"], "id": "박사_졸업생_의사"},
            {"name": ["박사과정", "졸업생 수", "비의사"], "id": "박사_졸업생_비의사"},
        ]

    student_graduate_student_domestic_basic_table = dash_table.DataTable(
        id={'index': 0, 'type': 'student_graduate_student_basic_domestic'},
        columns=(student_graduate_student_columns),
        data=student_graduate_student_basic_domestic,
        editable=True,
        row_deletable=True,
        style_header={
            'backgroundColor': 'rgb(160, 220, 255)',
            'fontWeight': 'bold',
            'textAlign': 'center',
            'font-size': '11px'
        },
        style_cell={
            'textAlign': 'center',
            'padding': '3px',
            'font-size': '10px',
            'minWidth': '100px',
        },
        style_table={
            'border': '0px',
            'overflowY': 'auto',
            'overflowX': 'auto'
        },
        merge_duplicate_headers=True
    )

    student_graduate_student_foreigner_basic_table = dash_table.DataTable(
        id={'index': 0, 'type': 'student_graduate_student_basic_foreigner'},
        columns=(student_graduate_student_columns),
        data=student_graduate_student_basic_foreigner,
        editable=True,
        row_deletable=True,
        style_header={
            'backgroundColor': 'rgb(160, 220, 255)',
            'fontWeight': 'bold',
            'textAlign': 'center',
            'font-size': '11px'
        },
        style_cell={
            'textAlign': 'center',
            'padding': '3px',
            'font-size': '10px',
            'minWidth': '100px',
        },
        style_table={
            'border': '0px',
            'overflowY': 'auto',
            'overflowX': 'auto'
        },
        merge_duplicate_headers=True
    )

    student_graduate_student_domestic_clinical_table = dash_table.DataTable(
        id={'index': 0, 'type': 'student_graduate_student_clinical_domestic'},
        columns=(student_graduate_student_columns),
        data=student_graduate_student_clinical_domestic,
        editable=True,
        row_deletable=True,
        style_header={
            'backgroundColor': 'rgb(160, 220, 255)',
            'fontWeight': 'bold',
            'textAlign': 'center',
            'font-size': '11px'
        },
        style_cell={
            'textAlign': 'center',
            'padding': '3px',
            'font-size': '10px',
            'minWidth': '100px',
        },
        style_table={
            'border': '0px',
            'overflowY': 'auto',
            'overflowX': 'auto'
        },
        merge_duplicate_headers=True
    )

    student_graduate_student_foreigner_clinical_table = dash_table.DataTable(
        id={'index': 0, 'type': 'student_graduate_student_clinical_foreigner'},
        columns=(student_graduate_student_columns),
        data=student_graduate_student_clinical_foreigner,
        editable=True,
        row_deletable=True,
        style_header={
            'backgroundColor': 'rgb(160, 220, 255)',
            'fontWeight': 'bold',
            'textAlign': 'center',
            'font-size': '11px'
        },
        style_cell={
            'textAlign': 'center',
            'padding': '3px',
            'font-size': '10px',
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
        dbc.Row([dbc.Col([html.H6('기초의학 (내국인)')], width='auto'), ]),
        dbc.Row([dbc.Col([student_graduate_student_domestic_basic_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_student_graduate_student_basic_domestic'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_student_graduate_student_basic_domestic'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})])]),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('기초의학 (외국인)')], width='auto'), ]),
        dbc.Row([dbc.Col([student_graduate_student_foreigner_basic_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_student_graduate_student_basic_foreigner'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_student_graduate_student_basic_foreigner'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})])]),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('임상의학 (내국인)')], width='auto'), ]),
        dbc.Row([dbc.Col([student_graduate_student_domestic_clinical_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_student_graduate_student_clinical_domestic'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_student_graduate_student_clinical_domestic'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})])]),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('임상의학 (외국인)')], width='auto'), ]),
        dbc.Row([dbc.Col([student_graduate_student_foreigner_clinical_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_student_graduate_student_clinical_foreigner'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_student_graduate_student_clinical_foreigner'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_student_education_hospital(school):
    student_education_affiliated_hospital = json.loads(getattr(school, '교육병원_부속병원', "[]"))
    student_education_partner_hospital = json.loads(getattr(school, '교육병원_협력병원', "[]"))
    student_education_hospital_columns = \
        [
            {"name": ["병원명"], "id": "병원명"},
            {"name": ["주소"], "id": "주소"},
            {"name": ["대표전화"], "id": "대표전화"},
            {"name": ["병상수(베드)"], "id": "병상수(베드)"},
        ]

    student_education_affiliated_hospital_table = dash_table.DataTable(
        id={'index': 0, 'type': 'student_education_affiliated_hospital'},
        columns=(student_education_hospital_columns),
        data=student_education_affiliated_hospital,
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

    student_education_partner_hospital_table = dash_table.DataTable(
        id={'index': 0, 'type': 'student_education_partner_hospital'},
        columns=(student_education_hospital_columns),
        data=student_education_partner_hospital,
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
        dbc.Row([dbc.Col([html.H6('부속병원')], width='auto'), ]),
        dbc.Row([dbc.Col([student_education_affiliated_hospital_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_student_education_affiliated_hospital'},
                        color="primary",
                        style={'margin-bottom': '10px'})])]),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('부속병원 외 교육(협력)병원')], width='auto'), ]),
        dbc.Row([dbc.Col([student_education_partner_hospital_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_student_education_partner_hospital'},
                        color="primary",
                        style={'margin-bottom': '10px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_student_student_support(school):
    student_support_organization_ox = getattr(school, '학생지원전담기구_유무', "있음")
    student_support_organization = json.loads(getattr(school, '학생지원_전담기구', "[]"))
    student_student_support_columns = \
        [
            {"name": ["전담기구명"], "id": "전담기구명"},
            {"name": ["설립연도"], "id": "설립연도"},
            {"name": ["직원 수"], "id": "직원 수"},
            {"name": ["예산 (천원)"], "id": "예산(천원)"},
        ]

    student_student_support_table = dash_table.DataTable(
        id={'index': 0, 'type': 'student_support_organization'},
        columns=(student_student_support_columns),
        data=student_support_organization,
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
        dbc.Row([dbc.Col([html.H6('학생지원전담기구 유무')], width='auto'),
                 dbc.Col([dbc.RadioItems(
                     options=[
                         {"label": "있음", "value": "있음"},
                         {"label": "없음", "value": "없음"},
                     ],
                     value=student_support_organization_ox,
                     inline=True,
                     id="student_support_organization_ox",
                     labelStyle={'display': 'inline-block'}
                 )], width='auto'),
                 ]),
        dbc.Row([dbc.Col([student_student_support_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_student_support_organization'},
                        color="primary",
                        style={'margin-bottom': '10px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_student_student_support_program(school):
    student_support_program = json.loads(getattr(school, '주요_학생지원_프로그램', "[]"))
    student_student_support_program_columns = \
        [
            {"name": ["프로그램 구분"], "id": "프로그램_구분"},
            {"name": ["프로그램명"], "id": "프로그램명"},
            {"name": ["프로그램 설명"], "id": "프로그램_설명"},
            {"name": ["주관"], "id": "주관"},
        ]

    student_student_support_program_table = dash_table.DataTable(
        id={'index': 0, 'type': 'student_support_program'},
        columns=(student_student_support_program_columns),
        data=student_support_program,
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
        dbc.Row([dbc.Col([student_student_support_program_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_student_support_program'},
                        color="primary",
                        style={'margin-bottom': '10px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_student_student_health_checkup(school):
    student_health_checkup_ox = getattr(school, '학생_건강검진_시행여부', "예")
    student_health_checkup_period = json.loads(getattr(school, '학생_건강검진_시행시기', "[]"))
    student_health_checkup_period_etc = getattr(school, '학생_건강검진_시행시기_기타', None)

    layer = dbc.Col([
        dbc.Row([dbc.Col([html.H6('감염 및 안전 관련 지침 유무', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'radio_establishment_type'},
                                         options=[{'label': ' 예', 'value': '예'},
                                                  {'label': ' 아니오', 'value': '아니오'}],
                                         value=student_health_checkup_ox,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=3)
                 ],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('시행 시기', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Checklist(id={'index': 0, 'type': 'checklist_student_health_checkup_period'},
                                        options=[{'label': ' 입학 시', 'value': '입학 시'},
                                                 {'label': ' 의학과 진학 시', 'value': '의학과 진학 시'},
                                                 {'label': ' 임상실습 진입 시', 'value': '임상실습 진입 시'},
                                                 {'label': ' 기타', 'value': '기타'}],
                                        value=student_health_checkup_period,
                                        inline=True,
                                        labelStyle={'margin-right': '20px',
                                                    'margin-left': '10px'})], width='auto'),
                 dbc.Col([dcc.Input(id={'index': 0, 'type': 'input_student_health_checkup_period_etc'},
                                    value=student_health_checkup_period_etc,
                                    type='text',
                                    style={'width': '100px'})], width='auto')
                 ],
                align='center',
                className='custom-row'),
    ],
        className='custom-col')
    return layer


def sub_tab_student_student_safety_management(school):
    student_safety_guideline_ox = getattr(school, '학생_안전관리_지침_유무', "있음")
    student_safety_education_ox = getattr(school, '학생_안전관리_교육_여부', "예")
    student_safety_education_period = json.loads(getattr(school, '학생_안전관리_교육_시행_시기', "[]"))
    student_safety_education_period_etc = getattr(school, '학생_안전관리_교육_시행_시기_기타', None)
    student_vaccination_ox = getattr(school, '학생_안전관리_교육_예방접종_여부', "예")
    student_school_life_insurance_ox = getattr(school, '학생_안전관리_교육_안전관련_보험가입_여부', "예")
    student_clinical_insurance_ox = getattr(school, '학생_안전관리_교육_임상실습_보험가입_여부', "예")

    layer = dbc.Col([
        dbc.Row([dbc.Col([html.H6('감염 및 안전관련 지침 유무', style={'text-align': 'center', 'margin-top': '5px'})], width=3),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'student_safety_guideline_ox'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'}],
                                         value=student_safety_guideline_ox,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=3)
                 ],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('감염 및 안전관련 교육 여부', style={'text-align': 'center', 'margin-top': '5px'})], width=3),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'student_safety_education_ox'},
                                         options=[{'label': ' 예', 'value': '예'},
                                                  {'label': ' 아니오', 'value': '아니오'}],
                                         value=student_safety_education_ox,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=3)
                 ],
                align='center',
                className='custom-row'),
        dbc.Row(
            [dbc.Col([html.H6('감염 및 안전 관련 교육 시행 시기', style={'text-align': 'center', 'margin-top': '5px'})], width=3),
             dbc.Col([dbc.Checklist(id={'index': 0, 'type': 'student_safety_education_period'},
                                    options=[{'label': ' 입학 시', 'value': '입학'},
                                             {'label': ' 의학과 진학 시', 'value': '의학과_진학'},
                                             {'label': ' 임상실습 진입 시', 'value': '임상실습_진입'},
                                             {'label': ' 기타', 'value': '기타'}],
                                    value=student_safety_education_period,
                                    inline=True,
                                    labelStyle={'margin-right': '20px',
                                                'margin-left': '10px'})], width='auto'),
             dbc.Col([dcc.Input(id={'index': 0, 'type': 'student_safety_education_period_etc'},
                                value=student_safety_education_period_etc,
                                type='text',
                                style={'width': '100px'})], width='auto')
             ],
            align='center',
            className='custom-row'),
        dbc.Row(
            [dbc.Col([html.H6('임상실습 전 필수 예방접종 확인 여부', style={'text-align': 'center', 'margin-top': '5px'})], width=3),
             dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'student_vaccination_ox'},
                                     options=[{'label': ' 예', 'value': '예'},
                                              {'label': ' 아니오', 'value': '아니오'}],
                                     value=student_vaccination_ox,
                                     inline=True,
                                     labelStyle={'margin-right': '20px',
                                                 'margin-left': '10px'})], width=3)
             ],
            align='center',
            className='custom-row'),
        dbc.Row(
            [dbc.Col([html.H6('학교생활 안전 관련 보험 가입 여부', style={'text-align': 'center', 'margin-top': '5px'})], width=3),
             dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'student_school_life_insurance_ox'},
                                     options=[{'label': ' 예', 'value': '예'},
                                              {'label': ' 아니오', 'value': '아니오'}],
                                     value=student_school_life_insurance_ox,
                                     inline=True,
                                     labelStyle={'margin-right': '20px',
                                                 'margin-left': '10px'})], width=3)
             ],
            align='center',
            className='custom-row'),
        dbc.Row([dbc.Col([html.H6('임상실습 시 보험 가입 여부', style={'text-align': 'center', 'margin-top': '5px'})], width=3),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'student_clinical_insurance_ox'},
                                         options=[{'label': ' 예', 'value': '예'},
                                                  {'label': ' 아니오', 'value': '아니오'}],
                                         value=student_clinical_insurance_ox,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=3)
                 ],
                align='center',
                className='custom-row'),
    ],
        className='custom-col')
    return layer


def sub_tab_student_student_per_professor(school):
    student_per_professor = json.loads(getattr(school, '지도교수당_평균학생수', "[]"))
    student_student_per_professor_columns = \
        [
            {"name": ["지도교수 종류"], "id": "지도교수 종류"},
            {"name": ["지도교수 유무"], "id": "지도교수 유무"},
            {"name": ["지도교수 1인당 평균 학생수"], "id": "지도교수 1인당 평균 학생수"},
            {"name": ["비고"], "id": "비고"},
        ]

    student_student_per_professor_table = dash_table.DataTable(
        id={'index': 0, 'type': 'student_per_professor'},
        columns=(student_student_per_professor_columns),
        data=student_per_professor,
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
        dbc.Row([dbc.Col([student_student_per_professor_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_student_per_professor'},
                        color="primary",
                        style={'margin-bottom': '10px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_student_student_international_exchange(school):
    student_international_exchange = json.loads(getattr(school, '학생_국제교류_현황', "[]"))
    student_student_international_exchange_columns = \
        [
            {"name": ["", "", "구분"], "id": "구분"},
            {"name": ["의예과", "1학년", "남"], "id": "의예과_1학년_남"},
            {"name": ["의예과", "1학년", "여"], "id": "의예과_1학년_여"},
            {"name": ["의예과", "2학년", "남"], "id": "의예과_2학년_남"},
            {"name": ["의예과", "2학년", "여"], "id": "의예과_2학년_여"},
            {"name": ["의학과", "1학년", "남"], "id": "의학과_1학년_남"},
            {"name": ["의학과", "1학년", "여"], "id": "의학과_1학년_여"},
            {"name": ["의학과", "2학년", "남"], "id": "의학과_2학년_남"},
            {"name": ["의학과", "2학년", "여"], "id": "의학과_2학년_여"},
            {"name": ["의학과", "3학년", "남"], "id": "의학과_3학년_남"},
            {"name": ["의학과", "3학년", "여"], "id": "의학과_3학년_여"},
            {"name": ["의학과", "4학년", "남"], "id": "의학과_4학년_남"},
            {"name": ["의학과", "4학년", "여"], "id": "의학과_4학년_여"},
            {"name": ["합계", "합계", "남"], "id": "합계_남"},
            {"name": ["합계", "합계", "여"], "id": "합계_여"},
            {"name": ["합계", "합계", "계"], "id": "합계_계"},
        ]

    student_student_international_exchange_table = dash_table.DataTable(
        id={'index': 0, 'type': 'student_international_exchange'},
        columns=(student_student_international_exchange_columns),
        data=student_international_exchange,
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
            'minWidth': '50px',
        },
        style_table={
            'border': '0px',
            'overflowY': 'auto',
            'overflowX': 'auto'
        },
        merge_duplicate_headers=True
    )

    layer = dbc.Col([
        dbc.Row([dbc.Col([student_student_international_exchange_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_student_international_exchange'},
                        color="primary",
                        style={'margin-bottom': '10px'})])]),
    ],
        className='custom-col')
    return layer
