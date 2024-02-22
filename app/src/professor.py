from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
from app.src.resource.predefined_tabs import TAB_ARGS
from PIL import Image
import json


def sub_tab_professor_professor(school):
    professor_professor_basic = json.loads(getattr(school, "교원수_기초의학", "[]"))
    professor_professor_clinical = json.loads(getattr(school, "교원수_임상의학", "[]"))

    professor_clinical_professor_columns = \
        [{"name": ["", "", "소속교실"], "id": "구분"},
         {"name": ["전임 교원 (기금교수 포함)", "교수", "남"], "id": "전임교원_교수_남"},
         {"name": ["전임 교원 (기금교수 포함)", "교수", "여"], "id": "전임교원_교수_여"},
         {"name": ["전임 교원 (기금교수 포함)", "부교수", "남"], "id": "전임교원_부교수_남"},
         {"name": ["전임 교원 (기금교수 포함)", "부교수", "여"], "id": "전임교원_부교수_여"},
         {"name": ["전임 교원 (기금교수 포함)", "조교수", "남"], "id": "전임교원_조교수_남"},
         {"name": ["전임 교원 (기금교수 포함)", "조교수", "여"], "id": "전임교원_조교수_여"},
         {"name": ["전임 교원 (기금교수 포함)", "합계", "남"], "id": "전임교원_합계_남"},
         {"name": ["전임 교원 (기금교수 포함)", "합계", "여"], "id": "전임교원_합계_여"},
         {"name": ["전임 교원 (기금교수 포함)", "합계", "계"], "id": "전임교원_합계_계"},
         {"name": ["", "", "본교 의대/의전원 출신 교원수"], "id": "본교_출신_교원수"},
         {"name": ["", "", "의사 교원수"], "id": "의사_교원수"},
         {"name": ["", "", "비의사 교원수"], "id": "비의사_교원수"},
         {"name": ["", "비전임 교원", "임상 교수"], "id": "비전임_임상교수"},
         {"name": ["", "비전임 교원", "연구 교수"], "id": "비전임_연구교수"},
         {"name": ["", "비전임 교원", "기타"], "id": "비전임_기타"},
         {"name": ["", "비전임 교원", "합계"], "id": "비전임_합계"},
         ]
    professor_basic_professor_columns = professor_clinical_professor_columns + [
        {"name": ["", "", "MD 조교 (기초 전공의)"], "id": "MD_조교"}, ]

    professor_basic_professor_table = dash_table.DataTable(
        id={'index': 0, 'type': 'professor_professor_basic'},
        columns=(professor_basic_professor_columns),
        data=professor_professor_basic,
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
    professor_clinical_professor_table = dash_table.DataTable(
        id={'index': 0, 'type': 'professor_professor_clinical'},
        columns=(professor_clinical_professor_columns),
        data=professor_professor_clinical,
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
        dbc.Row([html.H6("기초의학")], align='center', className='custom-row'),
        dbc.Row([dbc.Col([professor_basic_professor_table])],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_professor_professor_basic'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_professor_professor_basic'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})])]),
        html.Hr(),
        dbc.Row([html.H6("임상의학")], align='center', className='custom-row'),
        dbc.Row([dbc.Col([professor_clinical_professor_table])],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_professor_professor_clinical'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_professor_professor_clinical'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_professor_full_time_professor(school):
    professor_full_time_new_basic_professor_data = json.loads(getattr(school, "전임교원수_변화_기초의학_신규임용", "[]"))
    professor_full_time_retire_basic_professor_data = json.loads(getattr(school, "전임교원수_변화_기초의학_정년퇴임", "[]"))
    professor_full_time_new_clinical_professor_data = json.loads(getattr(school, "전임교원수_변화_임상의학_신규임용", "[]"))
    professor_full_time_retire_clinical_professor_data = json.loads(getattr(school, "전임교원수_변화_임상의학_정년퇴임", "[]"))

    professor_full_time_professor_columns = \
        [
            {"name": ["성별"], "id": "성별"},
            {"name": ["의사"], "id": "의사"},
            {"name": ["비의사"], "id": "비의사"},
            {"name": ["계"], "id": "계"},
        ]

    professor_full_time_new_basic_professor_table = dash_table.DataTable(
        id={'index': 0, 'type': 'professor_full_time_new_basic_professor_data'},
        columns=(professor_full_time_professor_columns),
        data=professor_full_time_new_basic_professor_data,
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

    professor_full_time_retire_basic_professor_table = dash_table.DataTable(
        id={'index': 0, 'type': 'professor_full_time_retire_basic_professor_data'},
        columns=(professor_full_time_professor_columns),
        data=professor_full_time_retire_basic_professor_data,
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
    professor_full_time_new_clinical_professor_table = dash_table.DataTable(
        id={'index': 0, 'type': 'professor_full_time_new_clinical_professor_data'},
        columns=(professor_full_time_professor_columns),
        data=professor_full_time_new_clinical_professor_data,
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
    professor_full_time_retire_clinical_professor_table = dash_table.DataTable(
        id={'index': 0, 'type': 'professor_full_time_retire_clinical_professor_data'},
        columns=(professor_full_time_professor_columns),
        data=professor_full_time_retire_clinical_professor_data,
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
        dbc.Row([dbc.Col([html.H6('신규 임용 기초의학 전임교원 수')], width='auto')]),
        dbc.Row([dbc.Col([professor_full_time_new_basic_professor_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_professor_full_time_new_basic_professor_data'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_professor_full_time_new_basic_professor_data'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})])]),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('정년 퇴임 기초의학 전임교원 수')], width='auto')]),
        dbc.Row([dbc.Col([professor_full_time_retire_basic_professor_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_professor_full_time_retire_basic_professor_data'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_professor_full_time_retire_basic_professor_data'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})])]),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('신규 임용 임상의학 전임교원 수')], width='auto')]),
        dbc.Row([dbc.Col([professor_full_time_new_clinical_professor_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_professor_full_time_new_clinical_professor_data'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_professor_full_time_new_clinical_professor_data'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})])]),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('정년 퇴임 임상의학 전임교원 수')], width='auto')]),
        dbc.Row([dbc.Col([professor_full_time_retire_clinical_professor_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_professor_full_time_retire_clinical_professor_data'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_professor_full_time_retire_clinical_professor_data'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_professor_medical_education_training(school):
    professor_medical_education_training = json.loads(getattr(school, "의학교육_관련_연수", "[]"))
    professor_medical_education_training_columns = \
        [
            {"name": ["세미나 참가자", "교내"], "id": "세미나_교내"},
            {"name": ["세미나 참가자", "교외"], "id": "세미나_교외"},
            {"name": ["세미나 참가자", "계"], "id": "세미나_계"},
            {"name": ["학회 참가자", "교내"], "id": "학회_교내"},
            {"name": ["학회 참가자", "교외"], "id": "학회_교외"},
            {"name": ["학회 참가자", "계"], "id": "학회_계"},
            {"name": ["워크숍 참가자", "교내"], "id": "워크숍_교내"},
            {"name": ["워크숍 참가자", "교외"], "id": "워크숍_교외"},
            {"name": ["워크숍 참가자", "계"], "id": "워크숍_계"},
            {"name": ["연수 참가자", "교내"], "id": "연수_교내"},
            {"name": ["연수 참가자", "교외"], "id": "연수_교외"},
            {"name": ["연수 참가자", "계"], "id": "연수_계"},
        ]

    professor_medical_education_training_table = dash_table.DataTable(
        id={'index': 0, 'type': 'professor_medical_education_training'},
        columns=(professor_medical_education_training_columns),
        data=professor_medical_education_training,
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
        dbc.Row([dbc.Col([professor_medical_education_training_table], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_professor_medical_education_training'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_professor_medical_education_training'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_professor_professor_development_promotion_system(school):
    professor_specialized_teaching_track = getattr(school, '교수개발_승진체계_교수트랙_운영_여부', "예")
    professor_specialized_teaching_track_etc = getattr(school, '교수개발_승진체계_교수트랙_운영_여부_비고', None)
    professor_evaluation_system_by_rank = getattr(school, '교수개발_승진체계_직급별_평가제도_운영_여부', "예")
    professor_evaluation_system_by_rank_etc = getattr(school, '교수개발_승진체계_직급별_평가제도_운영_여부_비고', None)
    professor_evaluation_system_by_function = getattr(school, '교수개발_승진체계_기능별_평가제도_운영_여부', "예")
    professor_evaluation_system_by_function_etc = getattr(school, '교수개발_승진체계_기능별_평가제도_운영_여부_비고', None)
    professor_educational_achievement_require = getattr(school, '교수개발_승진체계_교육업적_요구_여부', "예")
    professor_educational_achievement_require_etc = getattr(school, '교수개발_승진체계_교육업적_요구_여부_비고', None)
    professor_new_faculty_training_require = getattr(school, '교수개발_승진체계_신임교원_연수교육_여부', "예")
    professor_new_faculty_training_require_etc = getattr(school, '교수개발_승진체계_신임교원_연수교육_여부_비고', None)
    professor_new_faculty_number = getattr(school, '교수개발_승진체계_신임교원_연수교육_교원수', None)
    professor_new_faculty_number_trained = getattr(school, '교수개발_승진체계_신임교원_연수교육_이수완료수', None)
    professor_full_time_faculty_training_require = getattr(school, '교수개발_승진체계_전임교원_프로그램참여_여부', "예")
    professor_full_time_faculty_training_require_etc = getattr(school, '교수개발_승진체계_전임교원_프로그램참여_여부_비고', None)
    professor_full_time_faculty_number = getattr(school, '교수개발_승진체계_전임교원_프로그램참여_교원수', None)
    professor_full_time_faculty_number_trained = getattr(school, '교수개발_승진체계_전임교원_프로그램참여_이수완료수', None)

    layer = dbc.Col([
        dbc.Row([dbc.Col([html.H6('특화된 교수트랙 운영 여부', style={'text-align': 'center', 'margin-top': '5px'})], width=3),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'radio_establishment_type'},
                                         options=[{'label': ' 예', 'value': '예'},
                                                  {'label': ' 아니오', 'value': '아니오'}],
                                         value=professor_specialized_teaching_track,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width='auto'),
                 dbc.Col([html.H6('비고', style={'text-align': 'center', 'margin-top': '5px'})], width=1),
                 dbc.Col([dcc.Input(id={'index': 0, 'type': 'etc'},
                                    value=professor_specialized_teaching_track_etc,
                                    type='text',
                                    style={'margin-top': '5px'})])
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('직급별로 세분화된 교수업적 평가제도 운영 여부', style={'text-align': 'center', 'margin-top': '5px'})],
                         width=3),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'radio_establishment_type'},
                                         options=[{'label': ' 예', 'value': '예'},
                                                  {'label': ' 아니오', 'value': '아니오'}],
                                         value=professor_evaluation_system_by_rank,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width='auto'),
                 dbc.Col([html.H6('비고', style={'text-align': 'center', 'margin-top': '5px'})], width=1),
                 dbc.Col([dcc.Input(id={'index': 0, 'type': 'etc'},
                                    value=professor_evaluation_system_by_rank_etc,
                                    type='text',
                                    style={'margin-top': '5px'})])
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('기능별로 세분화된 교수업적 평가제도 운영 여부', style={'text-align': 'center', 'margin-top': '5px'})],
                         width=3),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'radio_establishment_type'},
                                         options=[{'label': ' 예', 'value': '예'},
                                                  {'label': ' 아니오', 'value': '아니오'}],
                                         value=professor_evaluation_system_by_function,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width='auto'),
                 dbc.Col([html.H6('비고', style={'text-align': 'center', 'margin-top': '5px'})], width=1),
                 dbc.Col([dcc.Input(id={'index': 0, 'type': 'etc'},
                                    value=professor_evaluation_system_by_function_etc,
                                    type='text',
                                    style={'margin-top': '5px'})])
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row(
            [dbc.Col([html.H6('교수 승진 시 필수 교육업적 요구 여부', style={'text-align': 'center', 'margin-top': '5px'})], width=3),
             dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'radio_establishment_type'},
                                     options=[{'label': ' 예', 'value': '예'},
                                              {'label': ' 아니오', 'value': '아니오'}],
                                     value=professor_educational_achievement_require,
                                     inline=True,
                                     labelStyle={'margin-right': '20px',
                                                 'margin-left': '10px'})], width='auto'),
             dbc.Col([html.H6('비고', style={'text-align': 'center', 'margin-top': '5px'})], width=1),
             dbc.Col([dcc.Input(id={'index': 0, 'type': 'etc'},
                                value=professor_educational_achievement_require_etc,
                                type='text',
                                style={'margin-top': '5px'})])
             ],
            align='center',
            className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('신임교원 연수교육 필수 여부', style={'text-align': 'center', 'margin-top': '5px'})], width=3),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'radio_establishment_type'},
                                         options=[{'label': ' 예', 'value': '예'},
                                                  {'label': ' 아니오', 'value': '아니오'}],
                                         value=professor_new_faculty_training_require,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width='auto'),
                 dbc.Col([html.H6('비고', style={'text-align': 'center', 'margin-top': '5px'})], width=1),
                 dbc.Col([dcc.Input(id={'index': 0, 'type': 'etc'},
                                    value=professor_new_faculty_training_require_etc,
                                    type='text',
                                    style={'margin-top': '5px'})])
                 ],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('신임교원 수', style={'text-align': 'center', 'margin-top': '5px'})], width=3),
                 dbc.Col([dcc.Input(id={'index': 0, 'type': 'etc'},
                                    value=professor_new_faculty_number,
                                    style={'margin-top': '5px'})], width='auto'),
                 dbc.Col([html.P('명', style={'text-align': 'left', 'margin-top': '12px'})], width=1),
                 ],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('신임교원 연수교육 이수완료 인원', style={'text-align': 'center', 'margin-top': '5px'})], width=3),
                 dbc.Col([dcc.Input(id={'index': 0, 'type': 'etc'},
                                    value=professor_new_faculty_number_trained,
                                    style={'margin-top': '5px'})], width='auto'),
                 dbc.Col([html.P('명', style={'text-align': 'left', 'margin-top': '12px'})]),
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col(
            [html.H6('전임교원 교육 관련 교수개발 프로그램 참여 의무화 여부', style={'text-align': 'center', 'margin-top': '5px'})], width=3),
            dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'radio_establishment_type'},
                                    options=[{'label': ' 예', 'value': '예'},
                                             {'label': ' 아니오', 'value': '아니오'}],
                                    value=professor_full_time_faculty_training_require,
                                    inline=True,
                                    labelStyle={'margin-right': '20px',
                                                'margin-left': '10px'})], width='auto'),
            dbc.Col([html.H6('비고', style={'text-align': 'center', 'margin-top': '5px'})], width=1),
            dbc.Col([dcc.Input(id={'index': 0, 'type': 'etc'},
                               value=professor_full_time_faculty_training_require_etc,
                               type='text',
                               style={'margin-top': '5px'})])
        ],
            align='center',
            className='custom-row'),
        dbc.Row([dbc.Col([html.H6('전임교원 수', style={'text-align': 'center', 'margin-top': '5px'})], width=3),
                 dbc.Col([dcc.Input(id={'index': 0, 'type': 'etc'},
                                    value=professor_full_time_faculty_number,
                                    style={'margin-top': '5px'})], width='auto'),
                 dbc.Col([html.P('명', style={'text-align': 'left', 'margin-top': '12px'})], width=1),
                 ],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [html.H6('전임교원 교육 관련 교수개발 프로그램 이수완료 인원 (연간 3시간 이상)', style={'text-align': 'center', 'margin-top': '5px'})],
            width=3),
            dbc.Col([dcc.Input(id={'index': 0, 'type': 'etc'},
                               value=professor_full_time_faculty_number_trained,
                               style={'margin-top': '5px'})], width='auto'),
            dbc.Col([html.P('명', style={'text-align': 'left', 'margin-top': '12px'})]),
        ],
            align='center',
            className='custom-row'),
    ],
        className='custom-col')
    return layer
