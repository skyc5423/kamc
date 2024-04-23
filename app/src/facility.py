from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
from app.src.resource.predefined_tabs import TAB_ARGS
from PIL import Image
import json


def sub_tab_facility_education_basic_facility(school):
    facility_num_lecture_room = getattr(school, '교육기본시설_강의실수', None)
    facility_num_laboratory = getattr(school, '교육기본시설_실험실습실수', None)
    clinical_center_ox = getattr(school, '임상술기센터_센터유무', None)
    clinical_center_where = json.loads(getattr(school, '임상술기센터_센터위치', "[]"))
    clinical_center_practical_num = getattr(school, '임상술기센터_실습방수', None)
    clinical_center_mock_test_num = getattr(school, '임상술기센터_모의시험가능장소', None)
    clinical_center_lecture_num = getattr(school, '임상술기센터_강의실수', None)
    clinical_center_equipment = json.loads(getattr(school, '임상술기센터_구형장비', "[]"))
    clinical_center_student_space_ox = getattr(school, '교육병원내_학생전용공간_유무', None)
    clinical_center_student_space = json.loads(getattr(school, '교육병원내_학생전용공간', "[]"))
    clinical_center_education_facility_ox = getattr(school, '교육병원내_학생교육시설_유무', None)
    clinical_center_education_facility = json.loads(getattr(school, '교육병원내_학생교육시설', "[]"))
    equip_column = \
        [
            {"name": ["장비명"], "id": "장비명"},
            {"name": ["장비 보유"], "id": "장비_보유"},
            {"name": ["보유 수량 (단위: 개)"], "id": "보유_수량"},
        ]
    facility_equip_table = dash_table.DataTable(
        id={'index': 0, 'type': 'clinical_center_equipment'},
        columns=(equip_column),
        data=clinical_center_equipment,
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
    facility_education_hospital_columns = \
        [
            {"name": ["위치(호실)명"], "id": "위치명"},
            {"name": ["수용 인원"], "id": "수용인원"},
        ]
    facility_education_hospital_for_student_table = dash_table.DataTable(
        id={'index': 0, 'type': 'clinical_center_student_space'},
        columns=(facility_education_hospital_columns),
        data=clinical_center_student_space,
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

    facility_education_hospital_for_education_table = dash_table.DataTable(
        id={'index': 0, 'type': 'clinical_center_education_facility'},
        columns=(facility_education_hospital_columns),
        data=clinical_center_education_facility,
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
        dbc.Row([dbc.Col([html.H6('총 강의실 수', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'),
                 dbc.Col([dcc.Input(id={'index': 0, 'type': 'etc'},
                                    value=facility_num_lecture_room,
                                    type='text')], width='auto'),
                 dbc.Col([html.P('실', style={'text-align': 'left', 'margin-top': '15px'})]),
                 dbc.Col([html.H6('총 실험실습실 수', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'),
                 dbc.Col([dcc.Input(id={'index': 0, 'type': 'etc'},
                                    value=facility_num_laboratory,
                                    type='text')], width='auto'),
                 dbc.Col([html.P('실', style={'text-align': 'left', 'margin-top': '15px'})]),
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row(
            [dbc.Col([html.H6('임상술기센터 (임상수기센터)', style={'text-align': 'center', 'margin-top': '5px'})], width='auto')],
            align='center',
            className='custom-row'),
        dbc.Row(
            [dbc.Col([html.H6('센터 유무', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'),
             dbc.Col([dbc.RadioItems(
                 id={'index': 0, 'type': 'clinical_center_ox'},
                 options=[{'label': ' 있음', 'value': '있음'},
                          {'label': ' 없음', 'value': '없음'}],
                 value=clinical_center_ox,
                 inline=True)], width='auto')],
            align='center',
            className='custom-row'),
        dbc.Row(
            [dbc.Col([html.H6('센터 위치', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'),
             dbc.Col(
                 [dbc.Checklist(
                     id={'index': 0, 'type': 'clinical_center_where'},
                     options=[{'label': '의대/의전원 내', 'value': '의대/의전원 내'},
                              {'label': '병원 내', 'value': '병원 내'}],
                     value=clinical_center_where,
                     inline=True)], width='auto')],
            align='center',
            className='custom-row'),
        dbc.Row([dbc.Col([html.H6('총 실습방 수', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'),
                 dbc.Col([dcc.Input(id={'index': 0, 'type': 'clinical_center_practical_num'},
                                    value=clinical_center_practical_num,
                                    type='text')], width='auto'),
                 dbc.Col([html.P('실', style={'text-align': 'left', 'margin-top': '15px'})]),
                 dbc.Col([html.H6('모의시험 가능장소', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'),
                 dbc.Col([dcc.Input(id={'index': 0, 'type': 'clinical_center_mock_test_num'},
                                    value=clinical_center_mock_test_num,
                                    type='text')], width='auto'),
                 dbc.Col([html.P('실', style={'text-align': 'left', 'margin-top': '15px'})]),
                 ],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('강의(교육)실 수', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'),
                 dbc.Col([dcc.Input(id={'index': 0, 'type': 'clinical_center_lecture_num'},
                                    value=clinical_center_lecture_num,
                                    type='text')], width='auto'),
                 dbc.Col([html.P('실', style={'text-align': 'left', 'margin-top': '15px'})]),
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('구비 장비', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'), ],
                align='center',
                className='custom-row'),
        dbc.Row(dbc.Col([facility_equip_table], width='auto'),
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_clinical_center_equipment'},
                        color="primary",
                        style={'margin-top': '10px'})])]),
        html.Hr(),
        dbc.Row(
            [dbc.Col([html.H6('교육병원 내 학생전용공간', style={'text-align': 'center', 'margin-top': '5px'}), ], width='auto'),
             dbc.Col([dbc.RadioItems(
                 id={'index': 0, 'type': 'clinical_center_student_space_ox'},
                 options=[{'label': ' 있음', 'value': '있음'},
                          {'label': ' 없음', 'value': '없음'}],
                 value=clinical_center_student_space_ox,
                 inline=True)])],
            align='center',
            className='custom-row'),
        dbc.Row(dbc.Col([facility_education_hospital_for_student_table], width='auto'),
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_clinical_center_student_space'},
                        color="primary",
                        style={'margin-top': '10px'})])]),
        html.Hr(),
        dbc.Row(
            [dbc.Col([html.H6('교육병원 내 학생교육시설', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'),
             dbc.Col([dbc.RadioItems(
                 id={'index': 0, 'type': 'clinical_center_education_facility_ox'},
                 options=[{'label': ' 있음', 'value': '있음'},
                          {'label': ' 없음', 'value': '없음'}],
                 value=clinical_center_education_facility_ox,
                 inline=True)])
             ],
            align='center',
            className='custom-row'),
        dbc.Row(dbc.Col([facility_education_hospital_for_education_table], width='auto'),
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_clinical_center_education_facility'},
                        color="primary",
                        style={'margin-top': '10px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_facility_medical_library(school):
    medical_library_present = getattr(school, '의학도서관_유무', "있음")
    medical_library_type = json.loads(getattr(school, '의학도서관_종류', "[]"))
    medical_library_independent_academin_information_system = getattr(school, '독립적_학술정보서비스_체제_구축_여부', "예")
    medical_library_annual_budget = getattr(school, '학술정보서비스_연간_예산액', None)
    medical_library_annual_budget_execution = getattr(school, '학술정보서비스_연간_예산_집행액', None)
    medical_library_professional_manpower = getattr(school, '학술정보서비스_전문인력', None)
    medical_library_columns = \
        [
            {"name": ["", "", "도서관명"], "id": "도서관명"},
            {"name": ["", "", "위치"], "id": "위치"},
            {"name": ["", "", "총 좌석수 (석)"], "id": "총좌석수"},
            {"name": ["열람석 사용 시간", "시작시간", "시"], "id": "열람석_시작시간_시"},
            {"name": ["열람석 사용 시간", "시작시간", "분"], "id": "열람석_시작시간_분"},
            {"name": ["열람석 사용 시간", "종료시간", "시"], "id": "열람석_종료시간_시"},
            {"name": ["열람석 사용 시간", "종료시간", "분"], "id": "열람석_종료시간_분"},
            {"name": ["", "전담직원 수 (명)", "사서"], "id": "전담직원_수_사서"},
            {"name": ["", "전담직원 수 (명)", "기타"], "id": "전담직원_수_기타"},
            {"name": ["", "전담직원 수 (명)", "계"], "id": "전담직원_수_계"},
        ]
    medical_library_table = dash_table.DataTable(
        id={'index': 0, 'type': 'medical_library_type'},
        columns=(medical_library_columns),
        data=medical_library_type,
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
            [dbc.Col([html.H6('의학도서관 유무', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'),
             dbc.Col([dbc.RadioItems(
                 id={'index': 0, 'type': 'medical_library_present'},
                 options=[{'label': ' 있음', 'value': '있음'}, {'label': ' 없음', 'value': ' 없음'}],
                 value=medical_library_present,
                 inline=True)], width='auto')],
            align='center',
            className='custom-row'),
        dbc.Row(
            [dbc.Col([html.H6('의학도서관 정보', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'), ], ),
        dbc.Row(dbc.Col([medical_library_table], width='auto'),
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_medical_library_type'},
                        color="primary",
                        style={'margin-top': '10px'})])]),
        html.Hr(),
        dbc.Row(
            [dbc.Col([html.H6('독립적 학술정보서비스 체제 구축 여부', style={'text-align': 'center', 'margin-top': '5px'})],
                     width='auto'),
             dbc.Col([dbc.RadioItems(
                 id={'index': 0, 'type': 'medical_library_independent_academin_information_system'},
                 options=[{'label': ' 예', 'value': '예'}, {'label': ' 아니오', 'value': ' 아니오'}],
                 value=medical_library_independent_academin_information_system,
                 inline=True)], width='auto')],
            align='center',
            className='custom-row'),
        dbc.Row(
            [dbc.Col([html.H6('학술정보서비스 연간 예산액 (비공개)', style={'text-align': 'center', 'margin-top': '5px'})],
                     width='auto'),
             dbc.Col([dbc.Input(
                 id={'index': 0, 'type': 'medical_library_annual_budget'},
                 value=medical_library_annual_budget, placeholder="연간 예산액", type="number")],
                 width='auto'),
             dbc.Col([html.P('천원', style={'text-align': 'left', 'margin-top': '12px'})]), ],
            align='center',
            className='custom-row'),
        dbc.Row(
            [dbc.Col([html.H6('학술정보서비스 연간 예산 집행액 (비공개)', style={'text-align': 'center', 'margin-top': '5px'})],
                     width='auto'),
             dbc.Col([dbc.Input(
                 id={'index': 0, 'type': 'medical_library_annual_budget_execution'},
                 value=medical_library_annual_budget_execution, placeholder="연간 예산 집행액", type="number")],
                 width='auto'),
             dbc.Col([html.P('천원', style={'text-align': 'left', 'margin-top': '12px'})]), ],
            align='center',
            className='custom-row'),
        dbc.Row(
            [dbc.Col([html.H6('학술정보서비스 전문인력', style={'text-align': 'center', 'margin-top': '5px'})],
                     width='auto'),
             dbc.Col([dbc.Input(
                 id={'index': 0, 'type': 'medical_library_professional_manpower'},
                 value=medical_library_professional_manpower, placeholder="전문인력", type="number")],
                 width='auto'),
             dbc.Col([html.P('명', style={'text-align': 'left', 'margin-top': '12px'})]), ],
            align='center',
            className='custom-row'),
    ],
        className='custom-col')
    return layer


def sub_tab_facility_student_small_group_discussion_room(school):
    facility_student_small_group_discussion_room = json.loads(getattr(school, "학생_소그룹_토의실", "[]"))
    facility_student_small_group_discussion_room_columns = \
        [
            {"name": ["구분"], "id": "구분"},
            {"name": ["총 개수(실)"], "id": "총개수"},
            {"name": ["실당 평균 수용인원(명)"], "id": "실당_평균_수용인원"},
        ]
    facility_student_small_group_discussion_room_table = dash_table.DataTable(
        id={'index': 0, 'type': 'facility_student_small_group_discussion_room'},
        columns=(facility_student_small_group_discussion_room_columns),
        data=facility_student_small_group_discussion_room,
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
            'minWidth': '200px',
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
            [dbc.Col([html.H6('소학습실 유무', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'), ]),
        dbc.Row(
            [dbc.Col([facility_student_small_group_discussion_room_table], width='auto'), ]),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_facility_student_small_group_discussion_room'},
                        color="primary",
                        style={'margin-top': '10px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_facility_dormitory(school):
    student_housing_status_survey = getattr(school, '학생_주거현황_조사_실시_여부', "예")
    dormitory_type = json.loads(getattr(school, '기숙사_형태', "[]"))
    dormitory_type_etc = getattr(school, '기숙사_형태_기타', None)
    dormitory_student_num = json.loads(getattr(school, '입실_학생수', "[]"))
    student_satisfaction_survey = getattr(school, '학생_만족도_조사_실시_여부', "아니오")
    dormitory_cost = json.loads(getattr(school, '학기별_기숙사비', "[]"))
    facility_dormitory_student_columns = \
        [
            {"name": ["남"], "id": "남"},
            {"name": ["여"], "id": "여"},
            {"name": ["계"], "id": "계"},
        ]
    facility_dormitory_student_table = dash_table.DataTable(
        id={'index': 0, 'type': 'dormitory_student_num'},
        columns=(facility_dormitory_student_columns),
        data=dormitory_student_num,
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
            'minWidth': '200px',
        },
        style_table={
            'border': '0px',
            'overflowY': 'auto',
            'overflowX': 'auto'
        },
        merge_duplicate_headers=True
    )
    facility_dormitory_cost_columns = \
        [
            {"name": ["구분"], "id": "구분"},
            {"name": ["학기별 기숙사비 (천원)"], "id": "학기별_기숙사비"},
        ]
    facility_dormitory_cost_table = dash_table.DataTable(
        id={'index': 0, 'type': 'dormitory_cost'},
        columns=(facility_dormitory_cost_columns),
        data=dormitory_cost,
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
            'minWidth': '200px',
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
            [dbc.Col([html.H6('학생 주거현황 조사 실시 여부', style={'text-align': 'center', 'margin-top': '5px'})],
                     width='auto'),
             dbc.Col([dbc.RadioItems(
                 id={'type': 'student_housing_status_survey', 'index': 0},
                 options=[{'label': ' 예', 'value': '예'}, {'label': ' 아니오', 'value': ' 아니오'}],
                 value=student_housing_status_survey,
                 inline=True)], width='auto'),],
            align='center',
            className='custom-row'),
        dbc.Row(
            [dbc.Col([html.H6('기숙사 형태', style={'text-align': 'center', 'margin-top': '5px'})],
                     width='auto'),
             dbc.Col([dbc.RadioItems(
                 id={'type': 'dormitory_type', 'index': 0},
                 options=[{'label': ' 전용 기숙사', 'value': '전용_기숙사'},
                          {'label': ' 공용 기숙사', 'value': '공용_기숙사'},
                          {'label': ' 기타', 'value': '기타'}],
                 value=dormitory_type,
                 inline=True)], width='auto'),
             dbc.Col([dcc.Input(id={'type': 'dormitory_type_etc', 'index': 0}, value=dormitory_type_etc)], width='auto')
             ],
            align='center',
            className='custom-row'),
        dbc.Row(
            [dbc.Col([html.H6('입실 학생수', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'), ]),
        dbc.Row(
            [dbc.Col([facility_dormitory_student_table], width='auto'), ]),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_dormitory_student_num'},
                        color="primary",
                        style={'margin-top': '10px'})])]),
        dbc.Row(
            [dbc.Col([html.H6('학생 만족도 조사 실시 여부', style={'text-align': 'center', 'margin-top': '5px'})],
                     width='auto'),
             dbc.Col([dbc.RadioItems(options=[{'label': ' 예', 'value': '예'}, {'label': ' 아니오', 'value': ' 아니오'}],
                                     value=student_satisfaction_survey,
                                     inline=True)], width='auto')],
            align='center',
            className='custom-row'),
        dbc.Row(
            [dbc.Col([html.H6('학기별 기숙사비 (비공개)', style={'text-align': 'center', 'margin-top': '5px'})],
                     width='auto'), ]),
        dbc.Row(
            [dbc.Col([facility_dormitory_cost_table], width='auto'), ]),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_dormitory_cost'},
                        color="primary",
                        style={'margin-top': '10px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_facility_student_self_study_space(school):
    student_self_study_space = json.loads(getattr(school, "학생_자율학습_공간", "[]"))
    student_self_study_space_ox = getattr(school, "학생_자율학습_공간_유무", "있음")

    facility_student_self_study_space_columns = \
        [
            {"name": ["자율학습 공간 명칭"], "id": "자율학습_공간_명칭"},
            {"name": ["개수 (실)"], "id": "개수"},
            {"name": ["수용인원 (명)"], "id": "수용인원"},
        ]
    facility_student_self_study_space_table = dash_table.DataTable(
        id={'index': 0, 'type': 'student_self_study_space'},
        columns=(facility_student_self_study_space_columns),
        data=student_self_study_space,
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
            'minWidth': '200px',
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
            [dbc.Col([html.H6('자율학습 공간 유무', style={'text-align': 'center', 'margin-top': '5px'})],
                     width='auto'),
             dbc.Col([dbc.RadioItems(
                 id={'type': 'student_self_study_space_ox', 'index': 0},
                 options=[{'label': ' 있음', 'value': '있음'}, {'label': ' 없음', 'value': ' 없음'}],
                 value=student_self_study_space_ox,
                 inline=True)], width='auto')],
            align='center',
            className='custom-row'),
        dbc.Row(
            [dbc.Col([facility_student_self_study_space_table], width='auto'), ]),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_student_self_study_space'},
                        color="primary",
                        style={'margin-top': '10px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_facility_student_welfare_facility(school):
    facility_student_welfare_facility = json.loads(getattr(school, "학생_복지시설", "[]"))
    facility_student_welfare_convenient = json.loads(getattr(school, "학생_편의시설", "[]"))
    facility_student_welfare_facility_columns = \
        [
            {"name": ["학생복지시설명"], "id": "학생복지시설명"},
            {"name": ["개수"], "id": "복지시설_개수"},
        ]
    facility_student_welfare_facility_table = dash_table.DataTable(
        id={'index': 0, 'type': 'facility_student_welfare_facility'},
        columns=(facility_student_welfare_facility_columns),
        data=facility_student_welfare_facility,
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
            'minWidth': '200px',
        },
        style_table={
            'border': '0px',
            'overflowY': 'auto',
            'overflowX': 'auto'
        },
        merge_duplicate_headers=True
    )
    facility_student_welfare_convenient_columns = \
        [
            {"name": ["학생편의시설명"], "id": "학생편의시설명"},
            {"name": ["개수"], "id": "편의시설_개수"},
        ]
    facility_student_welfare_convenient_table = dash_table.DataTable(
        id={'index': 0, 'type': 'facility_student_welfare_convenient'},
        columns=(facility_student_welfare_convenient_columns),
        data=facility_student_welfare_convenient,
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
            'minWidth': '200px',
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
            [dbc.Col([html.H6('학생복지시설명', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'), ]),
        dbc.Row(
            [dbc.Col([facility_student_welfare_facility_table], width='auto'), ]),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_facility_student_welfare_facility'},
                        color="primary",
                        style={'margin-top': '10px'})])]),
        html.Hr(),
        dbc.Row(
            [dbc.Col([html.H6('학생편의시설명', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'), ]),
        dbc.Row(
            [dbc.Col([facility_student_welfare_convenient_table], width='auto'), ]),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_facility_student_welfare_convenient'},
                        color="primary",
                        style={'margin-top': '10px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_facility_education_information_system(school):
    information_manpower = getattr(school, "정보화_전담인력_유무", "있음")
    facility_education_management_system = json.loads(getattr(school, "교육관리시스템", "[]"))
    facility_education_evaluation_system = json.loads(getattr(school, "교육평가시스템", "[]"))
    facility_education_management_system_columns = \
        [
            {"name": ["", "시스템"], "id": "시스템"},
            {"name": ["시스템 유무", "있음"], "id": "시스템_유"},
            {"name": ["시스템 유무", "없음"], "id": "시스템_무"},
            {"name": ["사용 학년", "의예 1"], "id": "사용학년_의예_1"},
            {"name": ["사용 학년", "의예 2"], "id": "사용학년_의예_2"},
            {"name": ["사용 학년", "의학 1"], "id": "사용학년_의학_1"},
            {"name": ["사용 학년", "의학 2"], "id": "사용학년_의학_2"},
            {"name": ["사용 학년", "의학 3"], "id": "사용학년_의학_3"},
            {"name": ["사용 학년", "의학 4"], "id": "사용학년_의학_4"},
            {"name": ["", "비고"], "id": "비고"},
        ]
    facility_education_management_system_table = dash_table.DataTable(
        id={'index': 0, 'type': 'facility_education_management_system'},
        columns=(facility_education_management_system_columns),
        data=facility_education_management_system,
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
    facility_education_evaluation_system_columns = \
        [
            {"name": ["", "시스템"], "id": "시스템"},
            {"name": ["시스템 유무", "있음"], "id": "시스템_유"},
            {"name": ["시스템 유무", "없음"], "id": "시스템_무"},
            {"name": ["사용 학년", "의예 1"], "id": "사용학년_의예_1"},
            {"name": ["사용 학년", "의예 2"], "id": "사용학년_의예_2"},
            {"name": ["사용 학년", "의학 1"], "id": "사용학년_의학_1"},
            {"name": ["사용 학년", "의학 2"], "id": "사용학년_의학_2"},
            {"name": ["사용 학년", "의학 3"], "id": "사용학년_의학_3"},
            {"name": ["사용 학년", "의학 4"], "id": "사용학년_의학_4"},
            {"name": ["", "1회 최대 이용가능 인원 (명)"], "id": "1회_최대_이용가능_인원"},
            {"name": ["", "비고"], "id": "비고"},
        ]
    facility_education_evaluation_system_table = dash_table.DataTable(
        id={'index': 0, 'type': 'facility_education_evaluation_system'},
        columns=(facility_education_evaluation_system_columns),
        data=facility_education_evaluation_system,
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
            [dbc.Col([html.H6('정보화 전담인력 유무', style={'text-align': 'center', 'margin-top': '5px'})],
                     width='auto'),
             dbc.Col([dbc.RadioItems(options=[{'label': ' O', 'value': 'O'}, {'label': ' X', 'value': ' X'}],
                                     value=information_manpower,
                                     inline=True)], width='auto')],
            align='center',
            className='custom-row'),
        html.Hr(),
        dbc.Row(
            [dbc.Col([html.H6('교육관리시스템', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'), ]),
        dbc.Row(
            [dbc.Col([facility_education_management_system_table], width='auto'), ]),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_facility_education_management_system'},
                        color="primary",
                        style={'margin-top': '10px'})])]),
        html.Hr(),
        dbc.Row(
            [dbc.Col([html.H6('교육평가시스템', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'), ]),
        dbc.Row(
            [dbc.Col([facility_education_evaluation_system_table], width='auto'), ]),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_facility_education_evaluation_system'},
                        color="primary",
                        style={'margin-top': '10px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_facility_student_research_laboratory(school):
    facility_student_research_laboratory_presence = getattr(school, "학생_연구실험실_유무", "있음")
    facility_student_research_laboratory_number = getattr(school, "총_실험실_수", None)
    facility_student_research_laboratory = json.loads(getattr(school, "이용대상학년_이용실적", "[]"))
    facility_student_research_laboratory_columns = \
        [
            {"name": ["", "구분"], "id": "구분"},
            {"name": ["의예과", "1학년"], "id": "의예과_1학년"},
            {"name": ["의예과", "2학년"], "id": "의예과_2학년"},
            {"name": ["의학과", "1학년"], "id": "의학과_1학년"},
            {"name": ["의학과", "2학년"], "id": "의학과_2학년"},
            {"name": ["의학과", "3학년"], "id": "의학과_3학년"},
            {"name": ["의학과", "4학년"], "id": "의학과_4학년"},
        ]
    facility_student_research_laboratory_table = dash_table.DataTable(
        id={'index': 0, 'type': 'facility_student_research_laboratory'},
        columns=(facility_student_research_laboratory_columns),
        data=facility_student_research_laboratory,
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
            [dbc.Col([html.H6('연구실험실 유무', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'),
             dbc.Col([dbc.RadioItems(
                 id={'type': 'facility_student_research_laboratory_presence', 'index': 0},
                 options=[{'label': ' O', 'value': 'O'}, {'label': ' X', 'value': ' X'}],
                 value=facility_student_research_laboratory_presence,
                 inline=True)], width='auto')],
            align='center',
            className='custom-row'),
        dbc.Row([dbc.Col([html.H6('연구실험실 수', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'),
                 dbc.Col([dbc.Input(
                     id={'type': 'facility_student_research_laboratory_number', 'index': 0},
                     value=facility_student_research_laboratory_number, type="number"), ], width=1),
                 dbc.Col([html.P('실', style={'text-align': 'left', 'margin-top': '12px'})])],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row(
            [dbc.Col([html.H6('연구실험실 이용 현황', style={'text-align': 'center', 'margin-top': '5px'})], width='auto'), ]),
        dbc.Row(
            [dbc.Col([facility_student_research_laboratory_table], width='auto'), ]),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_facility_student_research_laboratory'},
                        color="primary",
                        style={'margin-top': '10px'})])]),
    ],
        className='custom-col')
    return layer
