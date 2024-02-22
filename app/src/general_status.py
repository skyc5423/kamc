from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
from app.src.resource.predefined_tabs import TAB_ARGS
import json
from PIL import Image


def sub_tab_general_status_basic_info(school):
    prompt = '■ 작성 방법\n' \
             '1) 자료기준일 : 2023. 2. 28. 기준. 단, 졸업횟수와 졸업생수는 2022학년도(2022.3.1.~2023.2.28.) 기준\n' \
             '2) 대학명 : 의과대학 또는 의학전문대학원 공식 명칭\n' \
             '3) 설립인가연도 : 의과대학 설립 인가를 받은 연도\n' \
             '4) 최초입학연도 : 의과대학에 학생이 최초로 입학한 연도\n' \
             '5) 누적 졸업횟수 : 설립 이후 해당 학년도까지 누적된 의대‧의전원 총 졸업 횟수\n' \
             '6) 누적 졸업생수 : 설립 이후 해당 학년도까지 누적된 의대‧의전원 총 졸업자 수(의학사, 의무석사 취득자)\n' \
             '- 해당 학년도 졸업생 수를 입력하면 누적 합계는 자동 계산됨.\n' \
             '7) 학교 주소 : 행정실 주소, 대표 전화번호 등'
    school_name_korean = getattr(school, '국문대학명')
    school_name_english = getattr(school, '영문대학명')
    school_establish_year = getattr(school, '설립인가연도')
    school_first_year = getattr(school, '최초입학연도')
    school_sum_graduation = getattr(school, '누적졸업횟수')
    school_sum_alumni = json.loads(getattr(school, '누적졸업생수', "[]"))
    school_address_list = json.loads(getattr(school, '학교주소_캠퍼스명'))
    alumni_table = dash_table.DataTable(
        id={'index': 0, 'type': 'school_sum_alumni'},
        columns=(
            [{'id': '남', 'name': '남자 졸업생 수'},
             {'id': '여', 'name': '여자 졸업생 수'},
             {'id': '계', 'name': '졸업생 수'}]
        ),
        data=school_sum_alumni,
        editable=True,
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
    address_table = dash_table.DataTable(
        id={'index': 0, 'type': 'school_address_list'},
        columns=(
            [{'id': '캠퍼스명', 'name': '캠퍼스명'},
             {'id': '주소', 'name': '주소'},
             {'id': '우편번호', 'name': '우편번호'},
             {'id': '전화번호', 'name': '전화번호'},
             {'id': '팩스번호', 'name': '팩스번호'}]
        ),
        data=school_address_list,
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
        dbc.Row([dbc.Col([html.H6('대학명 국문', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'input_school_name_korean'},
                                    value=school_name_korean,
                                    size="10px")],
                         width=3),
                 dbc.Col([html.H6('대학명 영문', style={'text-align': 'center', 'margin-top': '5px'})],
                         width={'size': 2, 'offset': 1}),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'input_school_name_english'},
                                    value=school_name_english,
                                    size="10px")],
                         width=3),
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('설립 인가 연도', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'input_school_establish_year'},
                                    value=school_establish_year,
                                    size="10px")],
                         width=3),
                 dbc.Col([html.H6('최초 입학 연도', style={'text-align': 'center', 'margin-top': '5px'})],
                         width={'size': 2, 'offset': 1}),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'input_school_first_year'},
                                    value=school_first_year,
                                    size="10px")],
                         width=3),
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('누적 졸업 횟수', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'input_school_sum_graduation'},
                                    value=school_sum_graduation,
                                    size="10px")],
                         width=3),
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('누적 졸업생 수', style={'text-align': 'center', 'margin-top': '5px'}), ], width=2),
                 dbc.Col([alumni_table], width=3),
                 dbc.Col([dbc.Button("시각화",
                                     id={'index': 0, 'type': 'visualize_school_sum_alumni'},
                                     color="primary",
                                     style={'margin-bottom': '10px', 'margin-left': '20px'})], width='auto'),
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('학교 주소', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([address_table], width='auto'),
                 dbc.Col([dbc.Button("추가", id={'index': 0, 'type': 'add_school_address_list'}, color="primary",
                                     style={'margin-bottom': '10px'})
                          ],
                         width='auto'),
                 ],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col(html.Div(html.P(prompt, style={'font-size': '8px', 'whiteSpace': 'pre-line'})),
                         width={'size': 5, 'offset': 1})],
                align='center',
                className='custom-row')
    ],
        className='custom-col')

    return layer


def sub_tab_general_status_establishment_operation(school):
    school_establishment_type = getattr(school, '설립유형')
    school_establishment_name = getattr(school, '설립주체_법인명', None)
    school_establishment_year = getattr(school, '설립주체_법인설립연도', None)
    school_establishment_representative = getattr(school, '설립주체_법인설립당시대표자명', None)
    school_current_name = getattr(school, '운영주체_법인명', None)
    school_current_representative = getattr(school, '운영주체_현재법인대표자명', None)

    layer = dbc.Col([
        dbc.Row([dbc.Col([html.H6('설립 유형', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'school_establishment_type'},
                                         options=[{'label': ' 국립', 'value': '국립'}, {'label': ' 사립', 'value': '사립'}],
                                         value=school_establishment_type,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=3)
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('법인 설립 당시 법인명', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'school_establishment_name'},
                                    value=school_establishment_name,
                                    size="10px")],
                         width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('법인 설립 연도', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'school_establishment_year'},
                                    value=school_establishment_year,
                                    size="10px")],
                         width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('법인 설립 당시 대표자명', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'school_establishment_representative'},
                                    value=school_establishment_representative,
                                    size="10px")],
                         width=3)],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('현재 법인명', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'school_current_name'},
                                    value=school_current_name,
                                    size="10px")],
                         width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('현재 법인 대표자명', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'school_current_representative'},
                                    value=school_current_representative,
                                    size="10px")],
                         width=3)],
                align='center',
                className='custom-row'),
    ],
        className='custom-col')
    return layer


def sub_tab_general_status_ideology_mission_vision(school):
    school_founding_philisophy = getattr(school, '건학이념', None)

    school_mission_present = getattr(school, '사명_유무', "없음")
    school_mission_year = getattr(school, '사명_제정연도', None)
    school_mission_recent_year = getattr(school, '사명_최근개정연도', None)
    school_mission_organization = getattr(school, '사명_관리기구', None)
    school_mission_content = getattr(school, '사명_내용', None)

    school_vision_present = getattr(school, '비전_유무', None)
    school_vision_year = getattr(school, '비전_제정연도', None)
    school_vision_recent_year = getattr(school, '비전_최근개정연도', None)
    school_vision_organization = getattr(school, '비전_관리기구', None)
    school_vision_content = getattr(school, '비전_내용', None)

    layer = dbc.Col([
        dbc.Row([dbc.Col([html.H6('건학이념', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Textarea(id={'index': 0, 'type': 'school_founding_philisophy'},
                                       value=school_founding_philisophy,
                                       )])
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('사명(미션)', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'school_mission_present'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'}],
                                         value=school_mission_present,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('제정연도', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'school_mission_year'},
                                    value=school_mission_year,
                                    size="10px")], width=3),
                 dbc.Col([html.P('년', style={'text-align': 'left', 'margin-top': '12px'})]),
                 dbc.Col([html.H6('최근개정연도', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'school_mission_recent_year'},
                                    value=school_mission_recent_year,
                                    size="10px")], width=3),
                 dbc.Col([html.P('년', style={'text-align': 'left', 'margin-top': '12px'})])
                 ],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('관리기구', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'school_mission_organization'},
                                    value=school_mission_organization,
                                    size="10px")], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('내용', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Textarea(id={'index': 0, 'type': 'school_mission_content'},
                                       value=school_mission_content,
                                       size="10px")])],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('비전', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'school_vision_present'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'}],
                                         value=school_vision_present,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('제정연도', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'school_vision_year'},
                                    value=school_vision_year,
                                    size="10px")], width=3),
                 dbc.Col([html.P('년', style={'text-align': 'left', 'margin-top': '12px'})]),
                 dbc.Col([html.H6('최근개정연도', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'school_vision_recent_year'},
                                    value=school_vision_recent_year,
                                    size="10px")], width=3),
                 dbc.Col([html.P('년', style={'text-align': 'left', 'margin-top': '12px'})])
                 ],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('관리기구', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'school_vision_organization'},
                                    value=school_vision_organization,
                                    size="10px")], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('내용', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Textarea(id={'index': 0, 'type': 'school_vision_content'},
                                       value=school_vision_content,
                                       size="10px")])],
                align='center',
                className='custom-row'),
    ],
        className='custom-col')
    return layer


def sub_tab_general_status_education_objective(school):
    premedical_education_objective_presence = getattr(school, '교육목적_의예과_유무', '없음')
    premedical_education_objective_year = getattr(school, '교육목적_의예과_제정연도', None)
    premedical_education_objective_recent_year = getattr(school, '교육목적_의예과_최근개정연도', None)
    premedical_education_objective_organization = getattr(school, '교육목적_의예과_관리기구', None)
    premedical_education_objective_content = getattr(school, '교육목적_의예과_내용', None)
    medical_education_objective_presence = getattr(school, '교육목적_의학과_유무', '없음')
    medical_education_objective_year = getattr(school, '교육목적_의학과_제정연도', None)
    medical_education_objective_recent_year = getattr(school, '교육목적_의학과_최근개정연도', None)
    medical_education_objective_organization = getattr(school, '교육목적_의학과_관리기구', None)
    medical_education_objective_content = getattr(school, '교육목적_의학과_내용', None)

    layer = dbc.Col([
        dbc.Row([dbc.Col([html.H6('의예과', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'premedical_education_objective_presence'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'}],
                                         value=premedical_education_objective_presence,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('제정연도', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'premedical_education_objective_year'},
                                    value=premedical_education_objective_year,
                                    size="10px")], width=3),
                 dbc.Col([html.P('년', style={'text-align': 'left', 'margin-top': '12px'})]),
                 dbc.Col([html.H6('최근개정연도', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'premedical_education_objective_recent_year'},
                                    value=premedical_education_objective_recent_year,
                                    size="10px")], width=3),
                 dbc.Col([html.P('년', style={'text-align': 'left', 'margin-top': '12px'})])
                 ],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('관리기구', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'premedical_education_objective_organization'},
                                    value=premedical_education_objective_organization,
                                    size="10px")], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('내용', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Textarea(id={'index': 0, 'type': 'premedical_education_objective_content'},
                                       value=premedical_education_objective_content,
                                       size="10px")])],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('의학과', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'medical_education_objective_presence'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'}],
                                         value=medical_education_objective_presence,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('제정연도', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'medical_education_objective_year'},
                                    value=medical_education_objective_year,
                                    size="10px")], width=3),
                 dbc.Col([html.P('년', style={'text-align': 'left', 'margin-top': '12px'})]),
                 dbc.Col([html.H6('최근개정연도', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'medical_education_objective_recent_year'},
                                    value=medical_education_objective_recent_year,
                                    size="10px")], width=3),
                 dbc.Col([html.P('년', style={'text-align': 'left', 'margin-top': '12px'})])
                 ],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('관리기구', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'medical_education_objective_organization'},
                                    value=medical_education_objective_organization,
                                    size="10px")], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('내용', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Textarea(id={'index': 0, 'type': 'medical_education_objective_content'},
                                       value=medical_education_objective_content,
                                       size="10px")])],
                align='center',
                className='custom-row'),
    ],
        className='custom-col')
    return layer


def sub_tab_general_status_graduation_outcome(school):
    graduation_outcome_presence = getattr(school, '졸업성과_유무', '없음')
    graduation_outcome_year = getattr(school, '졸업성과_제정연도', None)
    graduation_outcome_recent_year = getattr(school, '졸업성과_최근개정연도', None)
    graduation_outcome_organization = getattr(school, '졸업성과_관리기구', None)
    graduation_outcome_content = getattr(school, '졸업성과_내용', None)

    phase_outcome_presence = getattr(school, '시기성과_유무', '없음')
    phase_outcome_year = getattr(school, '시기성과_제정연도', None)
    phase_outcome_recent_year = getattr(school, '시기성과_최근개정연도', None)
    phase_outcome_organization = getattr(school, '시기성과_관리기구', None)
    phase_outcome_open = getattr(school, '시기성과_공개범위', None)
    phase_outcome_content = getattr(school, '시기성과_파일명', None)

    layer = dbc.Col([
        dbc.Row([dbc.Col([html.H6('졸업성과', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'graduation_outcome_presence'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'}],
                                         value=graduation_outcome_presence,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('제정연도', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'graduation_outcome_year'},
                                    value=graduation_outcome_year,
                                    size="10px")], width=3),
                 dbc.Col([html.P('년', style={'text-align': 'left', 'margin-top': '12px'})]),
                 dbc.Col([html.H6('최근개정연도', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'graduation_outcome_recent_year'},
                                    value=graduation_outcome_recent_year,
                                    size="10px")], width=3),
                 dbc.Col([html.P('년', style={'text-align': 'left', 'margin-top': '12px'})])
                 ],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('관리기구', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'graduation_outcome_organization'},
                                    value=graduation_outcome_organization,
                                    size="10px")], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('내용', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Textarea(id={'index': 0, 'type': 'graduation_outcome_content'},
                                       value=graduation_outcome_content,
                                       size="10px")])],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('시기성과', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'phase_outcome_presence'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'}],
                                         value=phase_outcome_presence,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('제정연도', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'phase_outcome_year'},
                                    value=phase_outcome_year,
                                    size="10px")], width=3),
                 dbc.Col([html.P('년', style={'text-align': 'left', 'margin-top': '12px'})]),
                 dbc.Col([html.H6('최근개정연도', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'phase_outcome_recent_year'},
                                    value=phase_outcome_recent_year,
                                    size="10px")], width=3),
                 dbc.Col([html.P('년', style={'text-align': 'left', 'margin-top': '12px'})])
                 ],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('관리기구', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'phase_outcome_organization'},
                                    value=phase_outcome_organization,
                                    size="10px")], width=3),
                 dbc.Col([html.H6('공개범위', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Checklist(id={'index': 0, 'type': 'phase_outcome_open'},
                                        options=[{'label': ' 교내', 'value': '교내'},
                                                 {'label': ' 교외', 'value': '교외'}],
                                        value=phase_outcome_open,
                                        inline=True,
                                        labelStyle={'margin-right': '20px',
                                                    'margin-left': '10px'})], width=3)
                 ],
                align='center',
                className='custom-row'),
        html.Img(src='assets/phase_outcome_1.jpeg', style={'margin-left': '10vw', 'width': '50vw', 'height': '50vh'})
    ],
        className='custom-col')
    return layer


def sub_tab_general_status_appointment_procedure(school):
    department_president_name = getattr(school, '학장_성명', None)
    department_president_inauguration_day = getattr(school, '학장_취임일', None)
    department_president_term_ox = getattr(school, '학장_임기유무', "없음")
    department_president_term = getattr(school, '학장_임기', None)
    department_president_reappointment_ok = getattr(school, '학장_연임가능여부', "불가능")
    department_president_reappointment_ok_etc = getattr(school, '학장_연임가능여부_기타', None)
    department_president_reappointment_number = getattr(school, '학장_연임가능횟수', None)
    department_president_reappointment_constraint = [getattr(school, '학장_연임가능제한여부', [])]
    department_president_appointing_authority = getattr(school, '학장_임명권자', None)
    department_president_appointment_method = getattr(school, '학장_선임방법', "직접선거")
    department_president_appointment_method_etc = getattr(school, '학장_선임방법_기타', None)
    vice_president_system_ok = getattr(school, '학장_의무부총장_제도', "없음")
    vice_president_term = getattr(school, '학장_의무부총장_임기', None)

    layer = dbc.Col([
        dbc.Row([dbc.Col([html.H6('학(원)장 성명', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'department_president_name'},
                                    value=department_president_name,
                                    size="10px")], width=3),
                 dbc.Col([html.H6('취임일', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'department_president_inauguration_day'},
                                    value=department_president_inauguration_day,
                                    size="10px")], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('학(원)장 임기유무', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'department_president_term_ox'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'}],
                                         value=department_president_term_ox,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=3),
                 dbc.Col([html.H6('학(원)장 임기', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'department_president_term'},
                                    value=department_president_term,
                                    size="10px")], width=3),
                 dbc.Col([html.P('년', style={'text-align': 'left', 'margin-top': '12px'})])],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('연임가능여부', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'department_president_reappointment_ok'},
                                         options=[{'label': ' 가능', 'value': '가능'},
                                                  {'label': ' 불가능', 'value': '불가능'},
                                                  {'label': ' 기타', 'value': '기타'}],
                                         value=department_president_reappointment_ok,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=3),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'department_president_reappointment_ok_etc'},
                                    value=department_president_reappointment_ok_etc,
                                    size="10px")], width='auto')
                 ],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('연임가능횟수', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'department_president_reappointment_number'},
                                    value=department_president_reappointment_number,
                                    size="10px")], width=3),
                 dbc.Col([dcc.Checklist(id={'index': 0, 'type': 'department_president_reappointment_constraint'},
                                        options=[{'label': ' 제한 없음', 'value': 'O'}],
                                        value=department_president_reappointment_constraint,
                                        inline=True,
                                        labelStyle={'margin-right': '20px',
                                                    'margin-left': '10px'})], width=3)
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('임명권자', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'department_president_appointing_authority'},
                                    value=department_president_appointing_authority,
                                    size="10px")], width=3)],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('선임방법', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'department_president_appointment_method'},
                                         options=[{'label': ' 직접선거', 'value': '직접선거'},
                                                  {'label': ' 간접선거', 'value': '간접선거'},
                                                  {'label': ' 총장 임명', 'value': '총장임명'},
                                                  {'label': ' 학교법인 이사장 임명', 'value': '학교법인이사장임명'},
                                                  {'label': ' 기타', 'value': '기타'}],
                                         value=department_president_appointment_method,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})],
                         width='auto'),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'department_president_appointment_method_etc'},
                                    value=department_president_appointment_method_etc,
                                    size="10px")], width='auto')
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('의무부총장 제도', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'radio_committee_exists'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'}],
                                         value=vice_president_system_ok,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=3),
                 dbc.Col([html.H6('의무부총장 임기', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'input_mission_year'},
                                    value=vice_president_term,
                                    size="10px")], width=3),
                 dbc.Col([html.P('년', style={'text-align': 'left', 'margin-top': '12px'})])],
                align='center',
                className='custom-row'),
    ],
        className='custom-col')
    return layer


def sub_tab_general_status_appointment_power(school):
    professor_appointment_recommendation = getattr(school, '학장_교수_신규임용_추천권', "있음")
    professor_promotion_reappointment_recommendation = getattr(school, '학장_교수_승진재임용_추천권', "있음")
    professor_guaranteed_retirement_recommendation = getattr(school, '학장_교수_정년보장_추천권', "있음")
    professor_appointment_veto = getattr(school, '학장_교수_신규임용_거부권', "있음")
    professor_promotion_reappointment_veto = getattr(school, '학장_교수_승진재임용_거부권', "있음")
    professor_guaranteed_retirement_veto = getattr(school, '학장_교수_정년보장_거부권', "있음")
    administrative_hiring_recommendation = getattr(school, '학장_행정직원_신규채용_추천권', "있음")
    administrative_promotion_recommendation = getattr(school, '학장_행정직원_승진_추천권', "있음")
    administrative_hiring_veto = getattr(school, '학장_행정직원_신규채용_거부권', "있음")
    administrative_promotion_veto = getattr(school, '학장_행정직원_승진_거부권', "있음")

    professor_appointment_etc = getattr(school, '학장_교수_신규임용_기타', None)
    professor_promotion_reappointment_etc = getattr(school, '학장_교수_승진재임용_기타', None)
    professor_guaranteed_retirement_etc = getattr(school, '학장_교수_정년보장_기타', None)
    administrative_hiring_etc = getattr(school, '학장_행정직원_신규채용_기타', None)
    administrative_promotion_etc = getattr(school, '학장_행정직원_승진_기타', None)

    layer = dbc.Col([
        dbc.Row([dbc.Col([html.H6('', style={'text-align': 'center', 'margin-top': '5px'})], width=3),
                 dbc.Col([html.H6('추천권', style={'margin-top': '5px', 'margin-left': '3vw'})], width=2),
                 dbc.Col([html.H6('거부권', style={'margin-top': '5px', 'margin-left': '3vw'})], width=2),
                 dbc.Col([html.H6('기타', style={'margin-top': '5px', 'margin-left': '3vw', 'text-align': 'center',
                                               })], width={'size': 1})],
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('교수', style={'text-align': 'center', 'margin-top': '5px'})], width=1),
                 dbc.Col([html.H6('신규 임용', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'professor_appointment_recommendation'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'}],
                                         value=professor_appointment_recommendation,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})],
                         align='center', width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'professor_appointment_veto'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'}],
                                         value=professor_appointment_veto,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})],
                         align='center', width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'professor_appointment_etc'},
                                    value=professor_appointment_etc,
                                    size="10px")], width='auto')
                 ],
                align='center',
                className='custom-row'),

        dbc.Row([dbc.Col([html.H6('', style={'text-align': 'center', 'margin-top': '5px'})], width=1),
                 dbc.Col([html.H6('승진/재임용', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'professor_promotion_reappointment_recommendation'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'}],
                                         value=professor_promotion_reappointment_recommendation,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'professor_promotion_reappointment_veto'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'}],
                                         value=professor_promotion_reappointment_veto,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})],
                         align='center', width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'professor_promotion_reappointment_etc'},
                                    value=professor_promotion_reappointment_etc,
                                    size="10px")], width='auto')],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('', style={'text-align': 'center', 'margin-top': '5px'})], width=1),
                 dbc.Col([html.H6('정년 보장', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'professor_guaranteed_retirement_recommendation'},
                                         options=[{'label': ' 있음', 'value': 'O'},
                                                  {'label': ' 없음', 'value': 'X'}],
                                         value=professor_guaranteed_retirement_recommendation,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'professor_guaranteed_retirement_veto'},
                                         options=[{'label': ' 있음', 'value': 'O'},
                                                  {'label': ' 없음', 'value': 'X'}],
                                         value=professor_guaranteed_retirement_veto,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})],
                         align='center', width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'professor_guaranteed_retirement_etc'},
                                    value=professor_guaranteed_retirement_etc,
                                    size="10px")], width='auto')
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('행정직원', style={'text-align': 'center', 'margin-top': '5px'})], width=1),
                 dbc.Col([html.H6('신규 채용', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'administrative_hiring_recommendation'},
                                         options=[{'label': ' 있음', 'value': 'O'},
                                                  {'label': ' 없음', 'value': 'X'}],
                                         value=administrative_hiring_recommendation,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})],
                         align='center', width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'administrative_hiring_veto'},
                                         options=[{'label': ' 있음', 'value': 'O'},
                                                  {'label': ' 없음', 'value': 'X'}],
                                         value=administrative_hiring_veto,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})],
                         align='center', width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'administrative_hiring_etc'},
                                    value=administrative_hiring_etc,
                                    size="10px")], width='auto')
                 ],
                align='center',
                className='custom-row'),

        dbc.Row([dbc.Col([html.H6('', style={'text-align': 'center', 'margin-top': '5px'})], width=1),
                 dbc.Col([html.H6('승진', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'administrative_promotion_recommendation'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'}, ],
                                         value=administrative_promotion_recommendation,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'administrative_promotion_veto'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'}],
                                         value=administrative_promotion_veto,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})],
                         align='center', width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'administrative_promotion_etc'},
                                    value=administrative_promotion_etc,
                                    size="10px")], width='auto')
                 ],
                align='center',
                className='custom-row'),
    ],
        className='custom-col')
    return layer


def sub_tab_general_status_appointment_finance_power(school):
    budget_writing_authority = getattr(school, '학장_예산작성권', "있음")
    budget_execution_authority = getattr(school, '학장_예산집행권', "있음")
    budget_writing_authority_etc = getattr(school, '학장_예산작성권_기타', None)
    budget_execution_authority_etc = getattr(school, '학장_예산집행권_기타', None)
    budget_amount = getattr(school, '학장_1회전결가능_금액', 0)
    budget_opinion_collection_regulation = getattr(school, '학장_예산의견수렴규정', "있음")

    layer = dbc.Col([
        dbc.Row([dbc.Col([html.H6('예산 작성권', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'budget_writing_authority'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'},
                                                  {'label': ' 기타', 'value': '기타'}],
                                         value=budget_writing_authority,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'}),
                          ],
                         align='center', width=3),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'budget_writing_authority_etc'},
                                    value=budget_writing_authority_etc,
                                    size="10px")], width='auto')
                 ],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('예산 집행권', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'budget_execution_authority'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'},
                                                  {'label': ' 기타', 'value': '기타'}],
                                         value=budget_execution_authority,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})],
                         align='center', width=3),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'budget_execution_authority_etc'},
                                    value=budget_execution_authority_etc,
                                    size="10px")], width='auto')
                 ],
                align='center',
                className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('1회 전결가능 금액', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dbc.Input(id={'index': 0, 'type': 'budget_amount'},
                                    value=budget_amount,
                                    size="10px")],
                         align='center', width=3),
                 dbc.Col([html.P('천원', style={'margin-top': '12px'})], align='center', width=1),
                 ],
                align='center',
                className='custom-row'),
        dbc.Row([dbc.Col([html.H6('예산 편성 시 의견수렴 규정', style={'text-align': 'center', 'margin-top': '5px'})], width=2),
                 dbc.Col([dcc.RadioItems(id={'index': 0, 'type': 'budget_opinion_collection_regulation'},
                                         options=[{'label': ' 있음', 'value': '있음'},
                                                  {'label': ' 없음', 'value': '없음'}],
                                         value=budget_opinion_collection_regulation,
                                         inline=True,
                                         labelStyle={'margin-right': '20px',
                                                     'margin-left': '10px'})],
                         align='center', width=3),
                 ],
                align='center',
                className='custom-row'),
    ],
        className='custom-col')
    return layer


def sub_tab_general_status_administrative_structure(school):
    administrative_structure = json.loads(getattr(school, '행정구조', "[]"))
    administrative_structure_table = dash_table.DataTable(
        id={'index': 0, 'type': 'administrative_structure'},
        columns=(
            [{'id': '업무분야', 'name': ['', '업무 분야']},
             {'id': '담당부서명', 'name': ['', '담당 부서명']},
             {'id': '책임보직명', 'name': ['', '책임 보직명']},
             {'id': '보직수당_있음', 'name': ['보직수당 유무', '있음']},
             {'id': '보직수당_없음', 'name': ['보직수당 유무', '없음']},
             {'id': '정규직', 'name': ['행정직원 수 (명)', '정규직']},
             {'id': '무기계약직', 'name': ['행정직원 수 (명)', '무기계약직']},
             {'id': '단기계약직', 'name': ['행정직원 수 (명)', '단기계약직']},
             {'id': '기타', 'name': ['행정직원 수 (명)', '기타']},
             {'id': '합계', 'name': ['행정직원 수 (명)', '합계']},
             ]
        ),
        data=administrative_structure,
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
            'font-size': '12px',
            'minWidth': '5vw'
        },
        style_table={
            'border': '0px'
        },
        fill_width=False,
        merge_duplicate_headers=True,
    )
    layer = dbc.Col([
        dbc.Row([dbc.Col([administrative_structure_table], width='auto'),
                 dbc.Col([dbc.Button("추가", id={'index': 0, 'type': 'add_administrative_structure'}, color="primary",
                                     style={'margin-bottom': '10px'}),
                          dbc.Button("시각화",
                                     id={'index': 0, 'type': 'visualize_administrative_structure'},
                                     color="primary",
                                     style={'margin-bottom': '10px', 'margin-left': '20px'})],
                         width='auto'),
                 ],
                align='center',
                className='custom-row')],
        className='custom-col'
    )
    return layer


def sub_tab_general_status_organization(school):
    img_size = Image.open('assets/organizational_structure_1.png').size
    img_ratio = img_size[0] / img_size[1]
    height = 50
    width = int(height * img_ratio)
    layer = dbc.Col([
        html.Img(src='assets/organizational_structure_1.png',
                 style={'margin-left': '10vw', 'width': f'{width}vh', 'height': f'{height}vh'}), ],
        className='custom-col')
    return layer


def tab_db_extraction(school):
    notice_list = [{
        '제목': '공지사항 제목 1',
        '작성일': '2021-01-01',
        '내용': '공지사항 내용 1',
    },
        {
            '제목': '공지사항 제목 2',
            '작성일': '2021-01-01',
            '내용': '공지사항 내용 2',
        }
        ,
        {
            '제목': '공지사항 제목 3',
            '작성일': '2021-01-01',
            '내용': '공지사항 내용 3',
        }
    ]

    layer = dbc.Col([
        dbc.Row([dbc.Col([html.H6('DB를 엑셀로 추출하기')], width='auto')]),
        dbc.Row([
            dbc.Col([dbc.Button('DB 추출',
                                id={'index': 0, 'type': 'db_extraction'},
                                color='primary')],
                    width='auto',
                    align='center'),
        ],
            align='center',
            className='custom-row'),
        html.Hr(),
        dbc.Row([dbc.Col([html.H6('공지사항')], width='auto')]),
        dbc.Row([
            dbc.Col([
                dbc.ListGroup(
                    [dbc.ListGroupItem(
                        [
                            html.Div(notice['제목'], className="mb-1"),
                            dbc.Collapse(
                                dbc.Card(dbc.CardBody(notice['내용'])),
                                id={'index': i, 'type': 'collapse'},
                            ),
                        ],
                        id={'index': i, 'type': 'toggle'},
                    ) for i, notice in enumerate(notice_list)]
                )
            ], width=12)
        ], className='custom-row')
    ],
        className='custom-col')
    return layer
