import dash_bootstrap_components as dbc
from dash import html, dcc


class LoginPage:

    def __init__(self):
        self.prompt_list = [
            '이 사이트는 한국 의과대학, 의학전문대학원의 교육과 관련된 주요 현황 데이터를 축적하여',
            '대한민국 의학교육의 틀을 이해하고 향후 제반 연구 및 정책수립을 위해 개발된 현황 조사 시스템입니다. ',
            '대학에서 입력한 정보는 한국 기본의학교육 데이터베이스 구축, 의과대학 평가인증 활용, 의과대학 정책 수립,',
            '의학교육 관련 연구에 기초가 되는 데이터로 활용될 수 있습니다.',
            '아이디, 패스워드가 제3자에게 유출되지 않도록 유의하여주시길 바랍니다.', '원활한 사이트 이용을 위해 웹 브라우저는 크롬이나 엣지 사용을 권장합니다.',
            '사이트 이용 문의: 02-6952-9623, 9625, kamc@kamc.kr'
        ]

    def get_layer(self):
        layer = html.Div([
            html.H2('기본의학교육 데이터베이스',
                    style={"margin-top": "5vh",
                           "text-align": "center"}),
            dbc.Col([html.Plaintext(p, style={'margin': '1vh'}) for p in self.prompt_list],
                    style={'border': '1px solid white',
                           "margin-top": "5vh",
                           "margin-left": "24vw",
                           'margin-right': '24vw', }),
            dbc.Row(
                children=[
                    dbc.Col([dbc.Input(id={'index': 0, 'type': "login_id"},
                                       placeholder="아이디 입력",
                                       style={"width": "20vw",
                                              "margin-top": "3vh",
                                              "margin-left": "50vw",
                                              'transform': 'translate(-50%, 0%)',
                                              })]),
                    dbc.Col([dbc.Input(id={'index': 0, 'type': "login_password"},
                                       type="password",
                                       placeholder="비밀번호 입력",
                                       style={"width": "20vw",
                                              "margin-top": "3vh",
                                              "margin-left": "50vw",
                                              'transform': 'translate(-50%, 0%)', })]),
                    dbc.Col([dbc.Button('로그인',
                                        id={'index': 0, 'type': 'login_password_submit'},
                                        color='primary',
                                        style={'margin-left': '50vw',
                                               'margin-top': '3vh',
                                               'width': '5vw',
                                               'transform': 'translate(-50%, 0%)'})])])]
        )
        return layer
