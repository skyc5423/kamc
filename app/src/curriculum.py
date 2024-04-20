from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
from app.src.resource.predefined_tabs import TAB_ARGS
from PIL import Image
import json


def sub_tab_education_process_curriculum_committee(school):
    education_process_curriculum_committee_presence = getattr(school, '교육과정위원회_유무', '있음')
    education_process_curriculum_committee_name = getattr(school, '교육과정위원회_명칭', None)
    education_process_curriculum_committee_education_process = json.loads(getattr(school, '교육과정위원회_담당교육과정', "[]"))
    education_process_curriculum_committee_head = getattr(school, '교육과정위원회_구성_위원장', None)
    education_process_curriculum_committee_head_type = getattr(school, '교육과정위원회_구성_당연직구분', None)
    education_process_curriculum_committee_head_type_etc = getattr(school, '교육과정위원회_구성_당연직구분_기타', None)
    education_process_curriculum_committee_num = json.loads(getattr(school, '교육과정위원회_위원수', "[]"))
    education_process_curriculum_committee_period = getattr(school, '교육과정위원회_위원임기', None)
    education_process_curriculum_committee_opening_num = getattr(school, '교육과정위원회_연간회의개최횟수', None)
    committee_num_table = dash_table.DataTable(
        id={'index': 0, 'type': 'education_process_curriculum_committee_num'},
        columns=(
            [{'id': '구분', 'name': '구분'},
             {'id': '교수', 'name': '교수'},
             {'id': '행정직원', 'name': '행정직원'},
             {'id': '학생', 'name': '학생'},
             {'id': '기타', 'name': '기타'},
             {'id': '계', 'name': '계'}]
        ),
        data=education_process_curriculum_committee_num,
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
            'border': '0px'
        }
    )
    layer = dbc.Col([
        dbc.Row([dbc.Col([html.H6('위원회 유무권', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'education_process_curriculum_committee_presence'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'}],
                                         value=education_process_curriculum_committee_presence,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=3)],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('명칭', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'education_process_curriculum_committee_name'},
                                    value=education_process_curriculum_committee_name)], width=3)],
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('담당 교육과정', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col(
                     [dcc.Checklist(id={'index': 0, 'type': 'education_process_curriculum_committee_education_process'},
                                    options=[{'label': ' 의예과', 'value': '의예과'},
                                             {'label': ' 의학과', 'value': '의학과'}],
                                    value=education_process_curriculum_committee_education_process,
                                    inline=True,
                                    labelStyle={'margin-right': '20px',
                                                'margin-left': '10px'})],
                     width=3)],
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('위원장', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'education_process_curriculum_committee_head'},
                                         options=[{'label': ' 당연직', 'value': '당연직'},
                                                  {'label': ' 임명직', 'value': '임명직'},
                                                  {'label': ' 선출직', 'value': '선출직'}],
                                         value=education_process_curriculum_committee_head,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=3)],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('당연직 구분', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'education_process_curriculum_committee_head_type'},
                                         options=[{'label': ' 학(원)장', 'value': '학(원)장'},
                                                  {'label': ' 교육부학장', 'value': '교육부학장'},
                                                  {'label': ' 기타', 'value': '기타'}],
                                         value=education_process_curriculum_committee_head_type,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=3),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'education_process_curriculum_committee_head_type_etc'},
                                    value=education_process_curriculum_committee_head_type_etc,
                                    size="10px")], width='auto')
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('위원수', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([committee_num_table], width=3),
                 dbc.Col([dbc.Button("추가", id={'index': 0, 'type': 'add_education_process_curriculum_committee_num'},
                                     color="primary",
                                     style={'margin-bottom': '10px'}),
                          dbc.Button("시각화",
                                     id={'index': 0, 'type': 'visualize_education_process_curriculum_committee_num'},
                                     color="primary",
                                     style={'margin-bottom': '10px', 'margin-left': '20px'})], width='auto'), ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('위원 임기', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'education_process_curriculum_committee_period'},
                                    value=education_process_curriculum_committee_period)], width=3)],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('연간 회의 개최 횟수', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'education_process_curriculum_committee_opening_num'},
                                    value=education_process_curriculum_committee_opening_num)], width=3)],
                # style={'display': 'flex', 'alignItems': 'center', 'margin-top': '1vh', 'margin-bottom': '1vh'},
                className='custom-row'),
    ],
        className='custom-col')
    return layer


def sub_tab_education_process_curriculum_characteristics(school):
    education_process_curriculum_characteristics_operation = json.loads(getattr(school, '교육과정특성_학제', "[]"))
    education_process_curriculum_characteristics_advantages = getattr(school, '교육과정특성_특장점', None)
    education_process_curriculum_characteristics_principles = getattr(school, '교육과정특성_편성원칙', None)
    education_process_curriculum_operation = json.loads(getattr(school, '교육과정운영', "[]"))
    education_process_curriculum_week = json.loads(getattr(school, '교육주수', "[]"))
    education_process_curriculum_operation_columns = [{'id': '구분', 'name': ['', '구분']},
                                                      {'id': '의예과_1학년', 'name': ['의예과', '1학년']},
                                                      {'id': '의예과_2학년', 'name': ['의예과', '2학년']},
                                                      {'id': '의학과_1학년', 'name': ['의학과', '1학년']},
                                                      {'id': '의학과_2학년', 'name': ['의학과', '2학년']},
                                                      {'id': '의학과_3학년', 'name': ['의학과', '3학년']},
                                                      {'id': '의학과_4학년', 'name': ['의학과', '4학년']}]
    education_process_curriculum_week_columns = [{'id': '학기', 'name': ['', '학기']},
                                                 {'id': '의예과_1학년', 'name': ['의예과', '1학년']},
                                                 {'id': '의예과_2학년', 'name': ['의예과', '2학년']},
                                                 {'id': '의학과_1학년', 'name': ['의학과', '1학년']},
                                                 {'id': '의학과_2학년', 'name': ['의학과', '2학년']},
                                                 {'id': '의학과_3학년', 'name': ['의학과', '3학년']},
                                                 {'id': '의학과_4학년', 'name': ['의학과', '4학년']}]

    education_process_curriculum_operation_table = dash_table.DataTable(
        id={'index': 0, 'type': 'education_process_curriculum_operation'},
        columns=(education_process_curriculum_operation_columns),
        data=education_process_curriculum_operation,
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
            'border': '0px'
        }
    )

    education_process_curriculum_week_table = dash_table.DataTable(
        id={'index': 0, 'type': 'education_process_curriculum_week'},
        columns=(education_process_curriculum_week_columns),
        data=education_process_curriculum_week,
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
            'border': '0px'
        }
    )
    layer = dbc.Col([
        dbc.Row([dbc.Col([html.H6('학제', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.Checklist(
                     value=education_process_curriculum_characteristics_operation,
                     id={'index': 0, 'type': 'education_process_curriculum_characteristics_operation'},
                     options=[{'label': ' 의과대학', 'value': 'O'},
                              {'label': ' 의학전문대학원', 'value': 'X'}],
                     inline=True,
                     labelStyle={'margin-right': '20px',
                                 'margin-left': '10px'})], width=3)],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col(html.H6('교육과정 특장점', style={'text-align': 'center', 'margin-top': '5px'}), width=2),
                 dbc.Col(
                     [dbc.Textarea(id={'index': 0, 'type': 'education_process_curriculum_characteristics_advantages'},
                                   value=education_process_curriculum_characteristics_advantages)])],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col(html.H6('교육과정 편성원칙', style={'text-align': 'center', 'margin-top': '5px'}), width=2),
                 dbc.Col(
                     [dbc.Textarea(id={'index': 0, 'type': 'education_process_curriculum_characteristics_principles'},
                                   value=education_process_curriculum_characteristics_principles)])],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('교육과정 운용', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([education_process_curriculum_operation_table], width=3),
                 dbc.Col([dbc.Button("추가", id={'index': 0, 'type': 'add_education_process_curriculum_operation'},
                                     color="primary",
                                     style={'margin-bottom': '10px'})], width='auto')],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('교육주수', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([education_process_curriculum_week_table], width=3),
                 dbc.Col([dbc.Button("추가", id={'index': 0, 'type': 'add_education_process_curriculum_week'},
                                     color="primary",
                                     style={'margin-bottom': '10px'}),
                          dbc.Button("시각화",
                                     id={'index': 0, 'type': 'visualize_education_process_curriculum_week'},
                                     color="primary",
                                     style={'margin-bottom': '10px', 'margin-left': '20px'})], width='auto')],
                align='center',
                className='custom-row'),
    ],
        className='custom-col')
    return layer


def sub_tab_education_process_curriculum_subject(school):
    pre_medicine_class = json.loads(getattr(school, '개설교과목_의예과', '[]'))
    medicine_class = json.loads(getattr(school, '개설교과목_의학과', '[]'))
    pre_medicine_curriculum_table_columns = [{"name": ["", "교과목"], "id": "교과목"},
                                             {"name": ["", "구분"], "id": "구분"},
                                             {"name": ["", "개설 학년"], "id": "개설학년"},
                                             {"name": ["개설 학기", "1"], "id": "개설학기_1"},
                                             {"name": ["개설 학기", "2"], "id": "개설학기_2"},
                                             {"name": ["총 교육시간 (학생 1인당)", "강의"], "id": "총교육시간_강의"},
                                             {"name": ["총 교육시간 (학생 1인당)", "실습"], "id": "총교육시간_실습"},
                                             {"name": ["총 교육시간 (학생 1인당)", "기타"], "id": "총교육시간_기타"},
                                             {"name": ["총 교육시간 (학생 1인당)", "계"], "id": "총교육시간_계"},
                                             {"name": ["", "학점"], "id": "학점"},
                                             {"name": ["", "통합 과목"], "id": "통합과목"},
                                             {"name": ["교육 내용", "기초 과학"], "id": "교육내용_기초과학"},
                                             {"name": ["교육 내용", "기초 의학"], "id": "교육내용_기초의학"},
                                             {"name": ["교육 내용", "임상 의학"], "id": "교육내용_임상의학"},
                                             {"name": ["교육 내용", "인문학"], "id": "교육내용_인문학"},
                                             {"name": ["교육 내용", "사회 과학"], "id": "교육내용_사회과학"},
                                             {"name": ["교육 내용", "기타"], "id": "교육내용_기타"},
                                             {"name": ["교수 학습법", "강의"], "id": "교수학습법_강의"},
                                             {"name": ["교수 학습법", "실험 실습"], "id": "교수학습법_실험 실습"},
                                             {"name": ["교수 학습법", "TBL"], "id": "교수 학습법_TBL"},
                                             {"name": ["교수 학습법", "플립드 러닝"], "id": "교수학습법_플립드 러닝"},
                                             {"name": ["교수 학습법", "소그룹 토의"], "id": "교수학습법_소그룹 토의"},
                                             {"name": ["교수 학습법", "세미나"], "id": "교수학습법_세미나"},
                                             {"name": ["교수 학습법", "게임"], "id": "교수학습법_게임"},
                                             {"name": ["교수 학습법", "상호 협력 학습"], "id": "교수학습법_상호협력학습"},
                                             {"name": ["평가 방법", "지필 시험"], "id": "평가방법_지필시험"},
                                             {"name": ["평가 방법", "구두 시험"], "id": "평가방법_구두시험"},
                                             {"name": ["평가 방법", "과제/보고서"], "id": "평가방법_과제/보고서"},
                                             {"name": ["평가 방법", "발표"], "id": "평가방법_발표"},
                                             {"name": ["평가 방법", "동료 평가"], "id": "평가방법_동료평가"},
                                             {"name": ["평가 방법", "교수 관찰 평가"], "id": "평가방법_교수관찰평가"},
                                             {"name": ["평가 방법", "기타"], "id": "평가방법_기타"},
                                             {"name": ["", "형성 평가 실시"], "id": "형성평가실시"}, ]
    medicine_curriculum_table_columns = [{"name": ["", "교과목"], "id": "교과목"},
                                         {"name": ["", "구분"], "id": "구분"},
                                         {"name": ["", "개설 학년"], "id": "개설학년"},
                                         {"name": ["개설 학기", "1"], "id": "개설학기_1"},
                                         {"name": ["개설 학기", "2"], "id": "개설학기_2"},
                                         {"name": ["총 교육시간 (학생 1인당)", "강의"], "id": "총교육시간_강의"},
                                         {"name": ["총 교육시간 (학생 1인당)", "실습"], "id": "총교육시간_실습"},
                                         {"name": ["총 교육시간 (학생 1인당)", "기타"], "id": "총교육시간_기타"},
                                         {"name": ["총 교육시간 (학생 1인당)", "계"], "id": "총교육시간_계"},
                                         {"name": ["", "학점"], "id": "학점"},
                                         {"name": ["", "통합 과목"], "id": "통합과목"},
                                         {"name": ["교육 내용", "기초 의학 (기초과학 포함)"], "id": "교육내용_기초의학"},
                                         {"name": ["교육 내용", "임상 의학"], "id": "교육내용_임상의학"},
                                         {"name": ["교육 내용", "의료 인문학"], "id": "교육내용_의료인문학"},
                                         {"name": ["교수 학습법", "강의"], "id": "교수학습법_강의"},
                                         {"name": ["교수 학습법", "실험 실습"], "id": "교수학습법_실험실습"},
                                         {"name": ["교수 학습법", "TBL"], "id": "교수학습법_TBL"},
                                         {"name": ["교수 학습법", "플립드 러닝"], "id": "교수학습법_플립드러닝"},
                                         {"name": ["교수 학습법", "소그룹 토의"], "id": "교수학습법_소그룹토의"},
                                         {"name": ["교수 학습법", "세미나"], "id": "교수학습법_세미나"},
                                         {"name": ["교수 학습법", "게임"], "id": "교수학습법_게임"},
                                         {"name": ["교수 학습법", "상호 협력 학습"], "id": "교수학습법_상호협력학습"},
                                         {"name": ["평가 방법", "지필 시험"], "id": "평가방법_지필시험"},
                                         {"name": ["평가 방법", "구두 시험"], "id": "평가방법_구두시험"},
                                         {"name": ["평가 방법", "과제/보고서"], "id": "평가방법_과제/보고서"},
                                         {"name": ["평가 방법", "발표"], "id": "평가방법_발표"},
                                         {"name": ["평가 방법", "동료 평가"], "id": "평가방법_동료평가"},
                                         {"name": ["평가 방법", "교수 관찰 평가"], "id": "평가방법_교수관찰평가"},
                                         {"name": ["평가 방법", "기타"], "id": "평가방법_기타"},
                                         {"name": ["", "형성 평가 실시"], "id": "형성평가실시"}, ]
    pre_medicine_curriculum_table = dash_table.DataTable(
        id={'index': 0, 'type': 'pre_medicine_class'},
        columns=pre_medicine_curriculum_table_columns,
        data=pre_medicine_class,
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

    medicine_curriculum_table = dash_table.DataTable(
        id={'index': 0, 'type': 'medicine_class'},
        columns=medicine_curriculum_table_columns,
        data=medicine_class,
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

    pre_medicine_total_credit = getattr(school, '수료요건_의예과_총이수학점', None)
    pre_medicine_required_major_credit = getattr(school, '수료요건_의예과_전공필수', None)
    pre_medicine_optional_major_credit = getattr(school, '수료요건_의예과_전공선택', None)
    pre_medicine_liberal_credit = getattr(school, '수료요건_의예과_교양', None)
    pre_medicine_etc_credit = getattr(school, '수료요건_의예과_기타', None)
    pre_medicine_etc_condition = getattr(school, '수료요건_의예과_기타요구조건', "[]")
    pre_medicine_etc_condition_etc = getattr(school, '수료요건_의예과_기타요구조건_기타', "[]")

    medicine_total_credit = getattr(school, '졸업요건_의학과_총이수학점', None)
    medicine_required_major_credit = getattr(school, '졸업요건_의학과_전공필수', None)
    medicine_optional_major_credit = getattr(school, '졸업요건_의학과_전공선택', None)
    medicine_etc_credit = getattr(school, '졸업요건_의학과_기타', None)
    medicine_etc_condition = getattr(school, '졸업요건_의학과_기타요구조건', "[]")
    medicine_etc_condition_etc = getattr(school, '졸업요건_의학과_기타요구조건_기타', "[]")

    layer = dbc.Col([
        dbc.Row(
            [dbc.Col([html.H6('의예과 교과목', style={'text-align': 'left', 'margin-top': '5px', 'margin-left': '5px'})])],
            align='center',
            className='custom-row'
        ),
        dbc.Row([dbc.Col([pre_medicine_curriculum_table], width='auto'),
                 dbc.Col([dbc.Button("추가", id={'index': 0, 'type': 'add_pre_medicine_class'},
                                     color="primary",
                                     style={'margin-top': '10px'})])],
                align='center',
                className='custom-row'),
        dbc.Row(
            [dbc.Col([html.H6('총 이수학점', style={'text-align': 'left', 'margin-top': '5px', 'margin-left': '5px'})],
                     width=2),
             dbc.Col([dbc.Input(id={'index': 0, 'type': 'pre_medicine_total_credit'}, value=pre_medicine_total_credit,
                                type='number')], width=2), ],
            align='center',
            className='custom-row'),
        dbc.Row([
            dbc.Col([html.H6('전공 필수', style={'text-align': 'left', 'margin-top': '5px', 'margin-left': '5px'})],
                    width=2),
            dbc.Col([dbc.Input(id={'index': 0, 'type': 'pre_medicine_required_major_credit'},
                               value=pre_medicine_required_major_credit,
                               type='number')], width=2),
            dbc.Col([html.H6('전공 선택', style={'text-align': 'left', 'margin-top': '5px', 'margin-left': '5px'})],
                    width=2),
            dbc.Col([dbc.Input(id={'index': 0, 'type': 'pre_medicine_optional_major_credit'},
                               value=pre_medicine_optional_major_credit,
                               type='number')], width=2), ],
            align='center',
            className='custom-row'
        ),
        dbc.Row([
            dbc.Col([html.H6('교양', style={'text-align': 'left', 'margin-top': '5px', 'margin-left': '5px'})],
                    width=2),
            dbc.Col([dbc.Input(id={'index': 0, 'type': 'pre_medicine_liberal_credit'},
                               value=pre_medicine_liberal_credit,
                               type='number')], width=2),
            dbc.Col([html.H6('기타', style={'text-align': 'left', 'margin-top': '5px', 'margin-left': '5px'})],
                    width=2),
            dbc.Col([dbc.Input(id={'index': 0, 'type': 'pre_medicine_etc_credit'},
                               value=pre_medicine_etc_credit,
                               type='number')], width=2), ],
            align='center',
            className='custom-row'
        ),
        dbc.Row([
            dbc.Col([html.H6('기타요구조건', style={'text-align': 'left', 'margin-top': '5px', 'margin-left': '5px'})],
                    width=2),
            dbc.Col([dbc.Checklist(id={'index': 0, 'type': 'pre_medicine_etc_condition'},
                                   options=[{'label': ' 외국어능력시험', 'value': '외국어능력시험'},
                                            {'label': ' 봉사활동', 'value': '봉사활동'}],
                                   value=pre_medicine_etc_condition, inline=True)], width=2)],
            align='center',
            className='custom-row'),
        html.Hr(),
        dbc.Row(
            [dbc.Col([html.H6('의학과 교과목', style={'text-align': 'left', 'margin-top': '5px', 'margin-left': '5px'})])],
            align='center',
            className='custom-row'
        ),
        dbc.Row([dbc.Col([medicine_curriculum_table]),
                 dbc.Col([dbc.Button("추가", id={'index': 0, 'type': 'add_medicine_class'},
                                     color="primary",
                                     style={'margin-top': '10px'})], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row(
            [dbc.Col([html.H6('총 이수학점', style={'text-align': 'left', 'margin-top': '5px', 'margin-left': '5px'})],
                     width=2),
             dbc.Col([dbc.Input(id={'index': 0, 'type': 'medicine_total_credit'}, value=medicine_total_credit,
                                type='number')], width=2), ],
            align='center',
            className='custom-row'),
        dbc.Row([
            dbc.Col([html.H6('전공 필수', style={'text-align': 'left', 'margin-top': '5px', 'margin-left': '5px'})],
                    width=2),
            dbc.Col([dbc.Input(id={'index': 0, 'type': 'medicine_required_major_credit'},
                               value=medicine_required_major_credit,
                               type='number')], width=2),
            dbc.Col([html.H6('전공 선택', style={'text-align': 'left', 'margin-top': '5px', 'margin-left': '5px'})],
                    width=2),
            dbc.Col([dbc.Input(id={'index': 0, 'type': 'medicine_optional_major_credit'},
                               value=medicine_optional_major_credit,
                               type='number')], width=2), ],
            align='center',
            className='custom-row'
        ),
        dbc.Row([
            dbc.Col([html.H6('기타', style={'text-align': 'left', 'margin-top': '5px', 'margin-left': '5px'})],
                    width=2),
            dbc.Col([dbc.Input(id={'index': 0, 'type': 'medicine_etc_credit'},
                               value=medicine_etc_credit,
                               type='number')], width=2), ],
            align='center',
            className='custom-row'
        ),
        dbc.Row([
            dbc.Col([html.H6('기타요구조건', style={'text-align': 'left', 'margin-top': '5px', 'margin-left': '5px'})],
                    width=2),
            dbc.Col([dbc.Checklist(id={'index': 0, 'type': 'medicine_etc_condition'},
                                   options=[{'label': ' 기초의학종합평가 이수', 'value': '기초의학종합평가'},
                                            {'label': ' 임상의학종합평가 이수', 'value': '임상의학종합평가'},
                                            {'label': ' 임상수행능력평가 이수', 'value': '임상수행능력평가'}],
                                   value=medicine_etc_condition, inline=True)], width=2)],
            align='center',
            className='custom-row'),
    ],
        className='custom-col')
    return layer


def sub_tab_education_process_curriculum_clinical_practice(school):
    education_process_curriculum_clinical_practice_week = json.loads(getattr(school, '임상실습_교육주수', "[]"))
    education_process_curriculum_clinical_practice_required = json.loads(getattr(school, '임상실습_개설과목_필수', "[]"))
    education_process_curriculum_clinical_practice_optional_ox = getattr(school, '임상실습_개설과목_선택_운영여부', "운영")
    education_process_curriculum_clinical_practice_optional = json.loads(getattr(school, '임상실습_개설과목_선택', "[]"))
    education_process_curriculum_clinical_practice_intern_ox = getattr(school, '임상실습_학생인턴_운영여부', "운영")
    education_process_curriculum_clinical_practice_intern = json.loads(getattr(school, '임상실습_학생인턴', "[]"))
    education_process_curriculum_clinical_practice_week_columns = \
        [{'id': '학년', 'name': '학년'},
         {'id': '필수실습', 'name': '필수교육 주수'},
         {'id': '선택실습', 'name': '선택교육 주수'},
         {'id': '기타실습', 'name': '기타교육 주수'},
         {'id': '합계', 'name': '합계'}]
    curriculum_table_columns = [{"name": ["", "과목(프로그램)명"], "id": "과목명"},
                                {"name": ["", "개설학년(의학과)"], "id": "개설학년"},
                                {"name": ["개설 학기", "1"], "id": "개설 학기_1"},
                                {"name": ["개설 학기", "2"], "id": "개설 학기_2"},
                                {"name": ["", "학점"], "id": "학점"},
                                {"name": ["", "총 실습주수 (학생 1인당)"], "id": "총 실슴주수"},
                                {"name": ["총 교육시간 (학생 1인당)", "부속병원/교육병원"], "id": "총 교육시간_부속병원"},
                                {"name": ["총 교육시간 (학생 1인당)", "1차 의료기관"], "id": "총 교육시간_1차의료기관"},
                                {"name": ["총 교육시간 (학생 1인당)", "기타"], "id": "총 교육시간_기타"},
                                {"name": ["총 교육시간 (학생 1인당)", "계"], "id": "총 교육시간_계"},
                                {"name": ["평가 방법", "OSCE"], "id": "평가 방법_OSCE"},
                                {"name": ["평가 방법", "CPX"], "id": "평가 방법_CPX"},
                                {"name": ["평가 방법", "진료 능력 평가"], "id": "평가 방법_진료 능력 평가"},
                                {"name": ["평가 방법", "교수 관찰 평가"], "id": "평가 방법_교수 관찰 평가"},
                                {"name": ["평가 방법", "360도 다면 평가"], "id": "평가 방법_360도 다면 평가"},
                                {"name": ["평가 방법", "동료 평가"], "id": "평가 방법_동료 평가"},
                                {"name": ["평가 방법", "의무 기록 평가"], "id": "평가 방법_의무 기록 평가"},
                                {"name": ["평가 방법", "지필 시험"], "id": "평가 방법_지필 시험"},
                                {"name": ["평가 방법", "과제/보고서"], "id": "평가 방법_과제/보고서"},
                                {"name": ["평가 방법", "발표"], "id": "평가 방법_발표"},
                                {"name": ["평가 방법", "구두 시험"], "id": "평가 방법_구두 시험"},
                                {"name": ["평가 방법", "업무 일지"], "id": "평가 방법_업무 일지"},
                                {"name": ["평가 방법", "성찰 일지"], "id": "평가 방법_성찰 일지"},
                                {"name": ["평가 방법", "포트폴리오"], "id": "평가 방법_포트폴리오"}]
    intern_table_columns = [{"name": ["", "학생인턴 프로그램 (실습과)"], "id": "학생인턴 프로그램"},
                            {"name": ["", "구분"], "id": "구분"},
                            {"name": ["", "시행 학년 (의학과)"], "id": "시행 학년"},
                            {"name": ["시행 학기", "1"], "id": "시행 학기_1"},
                            {"name": ["시행 학기", "2"], "id": "시행 학기_2"},
                            {"name": ["", "시행주수 (학생 1인당)"], "id": "시행주수"},
                            {"name": ["", "학점"], "id": "학점"},
                            {"name": ["", "참여 학생 수 (명)"], "id": "참여학생수"},
                            {"name": ["", "비고"], "id": "비고"}]

    education_process_curriculum_clinical_practice_week_table = dash_table.DataTable(
        id={'index': 0, 'type': 'education_process_curriculum_clinical_practice_week'},
        columns=(education_process_curriculum_clinical_practice_week_columns),
        data=education_process_curriculum_clinical_practice_week,
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
            'minWidth': '5vw'
        },
        style_table={
            'border': '0px'
        },
        merge_duplicate_headers=True
    )

    education_process_curriculum_clinical_practice_required_table = dash_table.DataTable(
        id={'index': 0, 'type': 'education_process_curriculum_clinical_practice_required'},
        columns=curriculum_table_columns,
        data=education_process_curriculum_clinical_practice_required,
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
    education_process_curriculum_clinical_practice_optional_table = dash_table.DataTable(
        id={'index': 0, 'type': 'education_process_curriculum_clinical_practice_optional'},
        columns=curriculum_table_columns,
        data=education_process_curriculum_clinical_practice_optional,
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

    education_process_curriculum_clinical_practice_intern_table = dash_table.DataTable(
        id={'index': 0, 'type': 'education_process_curriculum_clinical_practice_intern'},
        columns=intern_table_columns,
        data=education_process_curriculum_clinical_practice_intern,
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
        dbc.Row(
            [dbc.Col([html.H6('교육 주수', style={'text-align': 'center', 'margin-top': '5px'})],
                     align='center',
                     className='custom-row'
                     ), ]),
        dbc.Row([dbc.Col([education_process_curriculum_clinical_practice_week_table], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_education_process_curriculum_clinical_practice_week'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_education_process_curriculum_clinical_practice_week'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})])]),
        html.Hr(),
        dbc.Row(
            [dbc.Col([html.H6('개설과목 (필수)', style={'text-align': 'left', 'margin-top': '5px', 'margin-left': '5px'})])],
            align='center',
            className='custom-row'
        ),
        dbc.Row([dbc.Col([education_process_curriculum_clinical_practice_required_table])],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_education_process_curriculum_clinical_practice_required'},
                        color="primary",
                        style={'margin-bottom': '10px'})])]),
        html.Hr(),
        dbc.Row(
            [dbc.Col([html.H6('개설과목 (선택)', style={'text-align': 'left', 'margin-top': '5px', 'margin-left': '5px'})])],
            align='center',
            className='custom-row'
        ),
        dbc.Row([dbc.Col([html.H6('선택과목 운영 여부', style={'text-align': 'left', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(
                     id={'index': 0, 'type': 'education_process_curriculum_clinical_practice_optional_ox'},
                     options=[{'label': ' 운영', 'value': '운영'},
                              {'label': ' 미운영', 'value': '미운영'}],
                     value=education_process_curriculum_clinical_practice_optional_ox,
                     inline=True,
                     labelStyle={'margin-right': '20px',
                                 'margin-left': '10px'})], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([education_process_curriculum_clinical_practice_optional_table])],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_education_process_curriculum_clinical_practice_optional'},
                        color="primary",
                        style={'margin-bottom': '10px'})])]),
        html.Hr(),
        dbc.Row(
            [dbc.Col([html.H6('학생인턴', style={'text-align': 'left', 'margin-top': '5px', 'margin-left': '5px'})])],
            align='center',
            className='custom-row'
        ),
        dbc.Row([dbc.Col([html.H6('학생인턴 프로그램 운영 여부', style={'text-align': 'left', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(
                     id={'index': 0, 'type': 'education_process_curriculum_clinical_practice_intern_ox'},
                     options=[{'label': ' 운영', 'value': '운영'},
                              {'label': ' 미운영', 'value': '미운영'}],
                     value=education_process_curriculum_clinical_practice_intern_ox,
                     inline=True,
                     labelStyle={'margin-right': '20px',
                                 'margin-left': '10px'})], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([education_process_curriculum_clinical_practice_intern_table])],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_education_process_curriculum_clinical_practice_intern'},
                        color="primary",
                        style={'margin-bottom': '10px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_education_process_curriculum_clinical_practice_time(school):
    introduction_to_clinical_practice_patient_interview_training_time_columns = \
        [{"name": ["", "학년"], "id": "학년"},
         {"name": ["학기", "1학기"], "id": "1학기"},
         {"name": ["학기", "2학기"], "id": "2학기"},
         {"name": ["", "임상실습입문 총 교육시간 (학생 1인당)"], "id": "임상실습입문_교육시간"},
         {"name": ["", "환자면담 총 교육시간 (학생 1인당)"], "id": "환자면담_교육시간"},
         {"name": ["", "임상실습 전 감염예방 총 교육시간 (학생 1인당)"], "id": "감염예방_교육시간"},
         {"name": ["", "비고"], "id": "비고"}]
    treatment_performance_clinical_skill_training_time_columns = \
        [{"name": ["", "학년"], "id": "학년"},
         {"name": ["학기", "1학기"], "id": "1학기"},
         {"name": ["학기", "2학기"], "id": "2학기"},
         {"name": ["진료수행 총 교육시간 (학생 1인당)", "별도 수업으로 진행"], "id": "진료수행_별도수업"},
         {"name": ["진료수행 총 교육시간 (학생 1인당)", "임상실습 중 진행"], "id": "진료수행_임상실습"},
         {"name": ["진료수행 총 교육시간 (학생 1인당)", "합계"], "id": "진료수행_합계"},
         {"name": ["임상술기 총 교육시간 (학생 1인당)", "별도 수업으로 진행"], "id": "임상술기_별도수업"},
         {"name": ["임상술기 총 교육시간 (학생 1인당)", "임상실습 중 진행"], "id": "임상술기_임상실습"},
         {"name": ["임상술기 총 교육시간 (학생 1인당)", "합계"], "id": "임상술기_합계"},
         {"name": ["", "비고"], "id": "비고"}]

    introduction_to_clinical_practice_patient_interview_training_time = json.loads(getattr(school, '임상실습입문_환자면담', "[]"))
    treatment_performance_clinical_skill_training_time = json.loads(getattr(school, '진료수행_임상술기', "[]"))
    introduction_to_clinical_practice_patient_interview_training_time_table = \
        dash_table.DataTable(
            id={'index': 0, 'type': 'introduction_to_clinical_practice_patient_interview_training_time'},
            columns=introduction_to_clinical_practice_patient_interview_training_time_columns,
            data=introduction_to_clinical_practice_patient_interview_training_time,
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
            merge_duplicate_headers=True)
    treatment_performance_clinical_skill_training_time_table = \
        dash_table.DataTable(
            id={'index': 0, 'type': 'treatment_performance_clinical_skill_training_time'},
            columns=treatment_performance_clinical_skill_training_time_columns,
            data=treatment_performance_clinical_skill_training_time,
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
            merge_duplicate_headers=True)
    layer = dbc.Col([
        dbc.Row(
            [dbc.Col([html.H6('임상실습입문/환자면담 교육시간', style={'text-align': 'center', 'margin-top': '5px'})],
                     align='center',
                     className='custom-row'
                     ), ]),
        dbc.Row([dbc.Col([introduction_to_clinical_practice_patient_interview_training_time_table])],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0,
                                  'type': 'add_introduction_to_clinical_practice_patient_interview_training_time'},
                        color="primary",
                        style={'margin-bottom': '10px'})])]),
        html.Hr(),
        dbc.Row(
            [dbc.Col(
                [html.H6('진료수행/임상술기 교육시간', style={'text-align': 'left', 'margin-top': '5px', 'margin-left': '5px'})])],
            align='center',
            className='custom-row'
        ),
        dbc.Row([dbc.Col([treatment_performance_clinical_skill_training_time_table])],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_treatment_performance_clinical_skill_training_time'},
                        color="primary",
                        style={'margin-bottom': '10px'})])]),
    ],
        className='custom-col')

    return layer


def sub_tab_education_process_student_evaluation(school):
    pre_medicine_evaluation = json.loads(getattr(school, '학생평가_의예과_평가방법', '[]'))
    pre_medicine_relative_evaluation_grade = getattr(school, '학생평가_의예과_상대평가_등급', None)
    pre_medicine_absolute_evaluation_grade = getattr(school, '학생평가_의예과_절대평가_등급', None)
    medicine_evaluation = json.loads(getattr(school, '학생평가_의학과_평가방법', '[]'))
    medicine_relative_evaluation_grade = getattr(school, '학생평가_의학과_상대평가_등급', None)
    medicine_absolute_evaluation_grade = getattr(school, '학생평가_의학과_절대평가_등급', None)
    criteria_repeating = getattr(school, '학생평가_유급기준', "있음")
    criteria_repeating_content = getattr(school, '학생평가_유급기준_내용', None)
    criteria_expulsion = getattr(school, '학생평가_제적기준', "있음")
    criteria_expulsion_content = getattr(school, '학생평가_제적기준_내용', None)

    layer = dbc.Col([
        dbc.Row(
            [dbc.Col([html.H6('의예과 필수교과목 성적평가 산출방법', style={'text-align': 'center', 'margin-top': '5px'})],
                     align='center',
                     className='custom-row'), ]),
        dbc.Row([
            dbc.Col([dcc.Checklist(id={'index': 0, 'type': 'pre_medicine_evaluation'},
                                   options=[{'label': ' 상대평가', 'value': '상대평가'},
                                            {'label': ' 절대평가', 'value': '절대평가'},
                                            {'label': ' pass/non-pass', 'value': 'pass_non_pass'},
                                            {'label': ' honor/pass/non-pass', 'value': 'honor_pass_non_pass'},
                                            {'label': ' 부분절대평가', 'value': '부분절대평가'},
                                            {'label': ' 100점 기준', 'value': '100점기준'}],
                                   value=pre_medicine_evaluation,
                                   inline=True,
                                   labelStyle={'margin-right': '20px',
                                               'margin-left': '10px'})], width='auto'),
            # dbc.Col([dbc.Input(id={'index': 0, 'type': 'completion_basic_medical_eval_grade'},
            #                    value=pre_medicine_relative_evaluation_grade, type='text', style={'width': '50px'})],
            #         width='auto'),
            # dbc.Col([html.Plaintext('등급', style={'margin-top': '12px'})]),
        ],
            align='center',
            className='custom-row'),
        html.Hr(),
        dbc.Row(
            [dbc.Col([html.H6('의학과 필수교과목 성적평가 산출방법', style={'text-align': 'center', 'margin-top': '5px'})],
                     align='center',
                     className='custom-row'), ]),
        dbc.Row([
            dbc.Col([dcc.Checklist(id={'index': 0, 'type': 'medicine_evaluation'},
                                   options=[{'label': ' 상대평가', 'value': '상대평가'},
                                            {'label': ' 절대평가', 'value': '절대평가'},
                                            {'label': ' pass/non-pass', 'value': 'pass_non_pass'},
                                            {'label': ' honor/pass/non-pass', 'value': 'honor_pass_non_pass'},
                                            {'label': ' 부분절대평가', 'value': '부분절대평가'},
                                            {'label': ' 100점 기준', 'value': '100점기준'}],
                                   value=medicine_evaluation,
                                   inline=True,
                                   labelStyle={'margin-right': '20px',
                                               'margin-left': '10px'})], width='auto'), ]),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('유급 기준', style={'text-align': 'left', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(
                     id={'index': 0, 'type': 'criteria_repeating'},
                     options=[{'label': ' 있음', 'value': '있음'},
                              {'label': ' 없음', 'value': '없음'}],
                     value=criteria_repeating,
                     inline=True,
                     labelStyle={'margin-right': '20px',
                                 'margin-left': '10px'})], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([
            dbc.Textarea(id={'index': 0, 'type': 'criteria_repeating_content'},
                         value=criteria_repeating_content, style={'width': '100%', 'height': 100})], align='center',
            className='custom-row')]),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('제적 기준', style={'text-align': 'left', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(
                     id={'index': 0, 'type': 'criteria_expulsion'},
                     options=[{'label': ' 있음', 'value': '있음'},
                              {'label': ' 없음', 'value': '없음'}],
                     value=criteria_expulsion,
                     inline=True,
                     labelStyle={'margin-right': '20px',
                                 'margin-left': '10px'})], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([
            dbc.Textarea(id={'index': 0, 'type': 'criteria_expulsion_content'},
                         value=criteria_expulsion_content, style={'width': '100%', 'height': 100})], align='center',
            className='custom-row')]),
    ],
        className='custom-col')
    return layer


def sub_tab_education_process_educational_department(school):
    education_process_educational_department_ox = getattr(school, '의학교육_전문부서_유무', "있음")
    education_process_educational_department = json.loads(getattr(school, '의학교육_전문부서', "[]"))
    columns = [{'id': '전문부서명', 'name': '전문부서명'},
               {'id': '전임교수', 'name': '전임교수'},
               {'id': '겸직교수', 'name': '겸직교수'},
               {'id': '연구교수', 'name': '연구교수'},
               {'id': '행정직원', 'name': '행정직원'},
               {'id': '기타', 'name': '기타'},
               {'id': '합계', 'name': '합계'}]
    table = dash_table.DataTable(
        id={'index': 0, 'type': 'education_process_educational_department'},
        columns=(columns),
        data=education_process_educational_department,
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
            'minWidth': '5vh'
        },
        style_table={
            'border': '0px'
        }
    )
    layer = dbc.Col([
        dbc.Row([dbc.Col([html.H6('의학교육 전문부서 유무', style={'text-align': 'left', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(
                     id={'index': 0, 'type': 'education_process_educational_department_ox'},
                     options=[{'label': ' 있음', 'value': '있음'},
                              {'label': ' 없음', 'value': '없음'}],
                     value=education_process_educational_department_ox,
                     inline=True,
                     labelStyle={'margin-right': '20px',
                                 'margin-left': '10px'})], width=3)],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([table], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_education_process_educational_department'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_education_process_educational_department'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})])]),
    ],
        className='custom-col')
    return layer


def sub_tab_education_process_medical_humanities(school):
    education_process_humanity_department_ox = getattr(school, '의료인문학_전문부서_유무', "있음")
    education_process_humanity_department = json.loads(getattr(school, '의료인문학_전문부서', "[]"))
    columns = [{'id': '전문부서명', 'name': '전문부서명'},
               {'id': '전임교수', 'name': '전임교수'},
               {'id': '겸직교수', 'name': '겸직교수'},
               {'id': '연구교수', 'name': '연구교수'},
               {'id': '행정직원', 'name': '행정직원'},
               {'id': '기타', 'name': '기타'},
               {'id': '합계', 'name': '합계'}]
    table = dash_table.DataTable(
        id={'index': 0, 'type': 'education_process_humanity_department'},
        columns=(columns),
        data=education_process_humanity_department,
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
            'minWidth': '5vh'
        },
        style_table={
            'border': '0px'
        }
    )
    layer = dbc.Col([
        dbc.Row([dbc.Col([html.H6('의료인문학 전문부서 유무', style={'text-align': 'left', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(
                     id={'index': 0, 'type': 'education_process_humanity_department_ox'},
                     options=[{'label': ' 있음', 'value': '있음'},
                              {'label': ' 없음', 'value': '없음'}],
                     value=education_process_humanity_department_ox,
                     inline=True,
                     labelStyle={'margin-right': '20px',
                                 'margin-left': '10px'})], width=3)],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([table], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(
            [dbc.Button("추가", id={'index': 0, 'type': 'add_education_process_humanity_department'},
                        color="primary",
                        style={'margin-bottom': '10px'}),
             dbc.Button("시각화",
                        id={'index': 0, 'type': 'visualize_education_process_humanity_department'},
                        color="primary",
                        style={'margin-bottom': '10px', 'margin-left': '20px'})
             ])]),
    ],
        className='custom-col')
    return layer
