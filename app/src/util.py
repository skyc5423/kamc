from general_status import *
from curriculum import *
from student import *
from professor import *
from facility import *
from management_finance import *
from dash import dcc, html, callback, MATCH, State, ALL, Input, Output
import pandas as pd
import plotly.express as px
import numpy as np


def get_header(main_tab, sub_tab):
    tab = [tab for tab in TAB_ARGS if tab['value'] == main_tab][0]
    selected_sub_tab = [sub for sub in tab['sub_tabs'] if sub['value'] == sub_tab][0]
    layer = dbc.Row([
        dbc.Col([html.H4(selected_sub_tab['name']), ])],
        style={'margin-bottom': '2vw', })
    return layer


def get_page_content(main_tab, sub_tab, school_list, school_name):
    head = get_header(main_tab, sub_tab)
    matched_school_list = [school for school in school_list if getattr(school, '대학명') == school_name]
    if len(matched_school_list) == 0:
        return html.Div('해당 학교의 정보가 없습니다.')
    school = matched_school_list[0]
    if main_tab == 'tab_general_status':
        if sub_tab == 'sub_tab_general_status_basic_info':
            body = sub_tab_general_status_basic_info(school)
        elif sub_tab == 'sub_tab_general_status_establishment_operation':
            body = sub_tab_general_status_establishment_operation(school)
        elif sub_tab == 'sub_tab_general_status_ideology_mission_vision':
            body = sub_tab_general_status_ideology_mission_vision(school)
        elif sub_tab == 'sub_tab_general_status_education_objective':
            body = sub_tab_general_status_education_objective(school)
        elif sub_tab == 'sub_tab_general_status_graduation_outcome':
            body = sub_tab_general_status_graduation_outcome(school)
        elif sub_tab == 'sub_tab_general_status_appointment_procedure':
            body = sub_tab_general_status_appointment_procedure(school)
        elif sub_tab == 'sub_tab_general_status_appointment_power':
            body = sub_tab_general_status_appointment_power(school)
        elif sub_tab == 'sub_tab_general_status_appointment_finance_power':
            body = sub_tab_general_status_appointment_finance_power(school)
        elif sub_tab == 'sub_tab_general_status_administrative_structure':
            body = sub_tab_general_status_administrative_structure(school)
        elif sub_tab == 'sub_tab_general_status_organization':
            body = sub_tab_general_status_organization(school)
    elif main_tab == 'tab_education_process':
        if sub_tab == 'sub_tab_education_process_curriculum_committee':
            body = sub_tab_education_process_curriculum_committee(school)
        elif sub_tab == 'sub_tab_education_process_curriculum_characteristics':
            body = sub_tab_education_process_curriculum_characteristics(school)
        elif sub_tab == 'sub_tab_education_process_curriculum_subject':
            body = sub_tab_education_process_curriculum_subject(school)
        elif sub_tab == 'sub_tab_education_process_curriculum_clinical_practice':
            body = sub_tab_education_process_curriculum_clinical_practice(school)
        elif sub_tab == 'sub_tab_education_process_curriculum_clinical_practice_time':
            body = sub_tab_education_process_curriculum_clinical_practice_time(school)
        elif sub_tab == 'sub_tab_education_process_student_evaluation':
            body = sub_tab_education_process_student_evaluation(school)
        elif sub_tab == 'sub_tab_education_process_educational_department':
            body = sub_tab_education_process_educational_department(school)
        elif sub_tab == 'sub_tab_education_process_medical_humanities':
            body = sub_tab_education_process_medical_humanities(school)
    elif main_tab == 'tab_student':
        if sub_tab == 'sub_tab_student_admission_system':
            body = sub_tab_student_admission_system(school)
        elif sub_tab == 'sub_tab_student_admission_student':
            body = sub_tab_student_admission_student(school)
        elif sub_tab == 'sub_tab_student_enrolled_student':
            body = sub_tab_student_enrolled_student(school)
        elif sub_tab == 'sub_tab_student_admission_student_structure':
            body = sub_tab_student_admission_student_structure(school)
        elif sub_tab == 'sub_tab_student_scholarship':
            body = sub_tab_student_scholarship(school)
        elif sub_tab == 'sub_tab_student_graduate_career':
            body = sub_tab_student_graduate_career(school)
        elif sub_tab == 'sub_tab_student_graduate_student':
            body = sub_tab_student_graduate_student(school)
        elif sub_tab == 'sub_tab_student_education_hospital':
            body = sub_tab_student_education_hospital(school)
        elif sub_tab == 'sub_tab_student_student_support':
            body = sub_tab_student_student_support(school)
        elif sub_tab == 'sub_tab_student_student_support_program':
            body = sub_tab_student_student_support_program(school)
        elif sub_tab == 'sub_tab_student_student_health_checkup':
            body = sub_tab_student_student_health_checkup(school)
        elif sub_tab == 'sub_tab_student_student_safety_management':
            body = sub_tab_student_student_safety_management(school)
        elif sub_tab == 'sub_tab_student_student_per_professor':
            body = sub_tab_student_student_per_professor(school)
        elif sub_tab == 'sub_tab_student_student_international_exchange':
            body = sub_tab_student_student_international_exchange(school)
    elif main_tab == 'tab_professor':
        if sub_tab == 'sub_tab_professor_professor':
            body = sub_tab_professor_professor(school)
        elif sub_tab == 'sub_tab_professor_full_time_professor':
            body = sub_tab_professor_full_time_professor(school)
        elif sub_tab == 'sub_tab_professor_medical_education_training':
            body = sub_tab_professor_medical_education_training(school)
        elif sub_tab == 'sub_tab_professor_professor_development_promotion_system':
            body = sub_tab_professor_professor_development_promotion_system(school)
    elif main_tab == 'tab_facility':
        if sub_tab == 'sub_tab_facility_education_basic_facility':
            body = sub_tab_facility_education_basic_facility(school)
        elif sub_tab == 'sub_tab_facility_medical_library':
            body = sub_tab_facility_medical_library(school)
        elif sub_tab == 'sub_tab_facility_student_small_group_discussion_room':
            body = sub_tab_facility_student_small_group_discussion_room(school)
        elif sub_tab == 'sub_tab_facility_dormitory':
            body = sub_tab_facility_dormitory(school)
        elif sub_tab == 'sub_tab_facility_student_self_study_space':
            body = sub_tab_facility_student_self_study_space(school)
        elif sub_tab == 'sub_tab_facility_student_welfare_facility':
            body = sub_tab_facility_student_welfare_facility(school)
        elif sub_tab == 'sub_tab_facility_education_information_system':
            body = sub_tab_facility_education_information_system(school)
        elif sub_tab == 'sub_tab_facility_student_research_laboratory':
            body = sub_tab_facility_student_research_laboratory(school)
    elif main_tab == 'tab_management_finance':
        if sub_tab == 'sub_tab_management_finance_professor_development':
            body = sub_tab_management_finance_professor_development(school)
        elif sub_tab == 'sub_tab_management_finance_student_education':
            body = sub_tab_management_finance_student_education(school)
        elif sub_tab == 'sub_tab_management_finance_student_tuition':
            body = sub_tab_management_finance_student_tuition(school)
    elif main_tab == 'tab_notice_db_extraction':
        body = tab_db_extraction(school)

    layer = dbc.Row([head, body],
                    style={'margin-top': '5vh',
                           'margin-left': '5vw'})
    return layer


total_add_button_dict = [
    {'state_key': 'add_school_address_list'},
    {'state_key': 'add_administrative_structure'},
    {'state_key': 'add_education_process_curriculum_committee_num'},
    {'state_key': 'add_education_process_curriculum_operation'},
    {'state_key': 'add_education_process_curriculum_week'},
    {'state_key': 'add_pre_medicine_class'},
    {'state_key': 'add_medicine_class'},
    {'state_key': 'add_education_process_curriculum_clinical_practice_week'},
    {'state_key': 'add_education_process_curriculum_clinical_practice_required'},
    {'state_key': 'add_education_process_curriculum_clinical_practice_optional'},
    {'state_key': 'add_education_process_curriculum_clinical_practice_intern'},
    {'state_key': 'add_introduction_to_clinical_practice_patient_interview_training_time'},
    {'state_key': 'add_treatment_performance_clinical_skill_training_time'},
    {'state_key': 'add_education_process_educational_department'},
    {'state_key': 'add_education_process_humanity_department'},
    {'state_key': 'add_rolling_student_admission_system_data'},
    {'state_key': 'add_regular_student_admission_system_data'},
    {'state_key': 'add_student_enrolled_student'},
    {'state_key': 'add_student_admission_student_structure'},
    {'state_key': 'add_student_scholarship'},
    {'state_key': 'add_student_graduate_career'},
    {'state_key': 'add_student_graduate_student_basic_domestic'},
    {'state_key': 'add_student_graduate_student_basic_foreigner'},
    {'state_key': 'add_student_graduate_student_clinical_domestic'},
    {'state_key': 'add_student_graduate_student_clinical_foreigner'},
    {'state_key': 'add_student_education_affiliated_hospital'},
    {'state_key': 'add_student_education_partner_hospital'},
    {'state_key': 'add_student_support_organization'},
    {'state_key': 'add_student_support_program'},
    {'state_key': 'add_student_per_professor'},
    {'state_key': 'add_student_international_exchange'},
    {'state_key': 'add_professor_professor_basic'},
    {'state_key': 'add_professor_professor_clinical'},
    {'state_key': 'add_professor_full_time_new_basic_professor_data'},
    {'state_key': 'add_professor_full_time_retire_basic_professor_data'},
    {'state_key': 'add_professor_full_time_new_clinical_professor_data'},
    {'state_key': 'add_professor_full_time_retire_clinical_professor_data'},
    {'state_key': 'add_professor_medical_education_training'},
    {'state_key': 'add_clinical_center_equipment'},
    {'state_key': 'add_clinical_center_student_space'},
    {'state_key': 'add_clinical_center_education_facility'},
    {'state_key': 'add_medical_library_type'},
    {'state_key': 'add_facility_student_small_group_discussion_room'},
    {'state_key': 'add_dormitory_student_num'},
    {'state_key': 'add_dormitory_cost'},
    {'state_key': 'add_student_self_study_space'},
    {'state_key': 'add_facility_student_welfare_facility'},
    {'state_key': 'add_facility_student_welfare_convenient'},
    {'state_key': 'add_facility_education_management_system'},
    {'state_key': 'add_facility_education_evaluation_system'},
    {'state_key': 'add_facility_student_research_laboratory'},
    {'state_key': 'add_management_finance_student_education'},
    {'state_key': 'add_management_finance_student_tuition_medical_school'},
    {'state_key': 'add_management_finance_student_tuition_graduate_medicine'},
    {'state_key': 'add_student_admission_student'}
]

total_add_button_input = [Input({'type': d['state_key'], 'index': ALL}, 'n_clicks') for d in total_add_button_dict]
total_add_button_output = [Output({'type': d['state_key'], 'index': ALL}, 'n_clicks') for d in
                           total_add_button_dict] + [
                              Output({'type': "_".join(d['state_key'].split("_")[1:]), 'index': ALL}, 'data') for d in
                              total_add_button_dict]
total_add_button_state = []
for d in total_add_button_dict:
    total_add_button_state.append(State({'type': "_".join(d['state_key'].split("_")[1:]), 'index': ALL}, 'data'))
    total_add_button_state.append(State({'type': "_".join(d['state_key'].split("_")[1:]), 'index': ALL}, 'columns'))

total_state_key_dict = [
    {'state_key': 'school_sum_alumni', 'state_type': 'data', 'state_name': '누적졸업생수'},
    {'state_key': 'school_address_list', 'state_type': 'data', 'state_name': '학교주소_캠퍼스명'},
    {'state_key': 'input_school_name_korean', 'state_type': 'value', 'state_name': '국문대학명'},
    {'state_key': 'input_school_name_english', 'state_type': 'value', 'state_name': '영문대학명'},
    {'state_key': 'input_school_establish_year', 'state_type': 'value', 'state_name': '설립인가연도'},
    {'state_key': 'input_school_first_year', 'state_type': 'value', 'state_name': '최초입학연도'},
    {'state_key': 'input_school_sum_graduation', 'state_type': 'value', 'state_name': '누적졸업횟수'},
    {'state_key': 'school_establishment_type', 'state_type': 'value', 'state_name': '설립유형'},
    {'state_key': 'school_establishment_name', 'state_type': 'value', 'state_name': '설립주체_법인명'},
    {'state_key': 'school_establishment_year', 'state_type': 'value', 'state_name': '설립주체_법인설립연도'},
    {'state_key': 'school_establishment_representative', 'state_type': 'value', 'state_name': '설립주체_법인설립당시대표자명'},
    {'state_key': 'school_current_name', 'state_type': 'value', 'state_name': '운영주체_법인명'},
    {'state_key': 'school_current_representative', 'state_type': 'value', 'state_name': '운영주체_현대법인대표자명'},
    {'state_key': 'school_founding_philisophy', 'state_type': 'value', 'state_name': '건학이념'},
    {'state_key': 'school_mission_present', 'state_type': 'value', 'state_name': '사명_유무'},
    {'state_key': 'school_mission_year', 'state_type': 'value', 'state_name': '사명_제정연도'},
    {'state_key': 'school_mission_recent_year', 'state_type': 'value', 'state_name': '사명_최근개정연도'},
    {'state_key': 'school_mission_organization', 'state_type': 'value', 'state_name': '사명_관리기구'},
    {'state_key': 'school_mission_content', 'state_type': 'value', 'state_name': '사명_내용'},
    {'state_key': 'school_vision_present', 'state_type': 'value', 'state_name': '비전_유무'},
    {'state_key': 'school_vision_year', 'state_type': 'value', 'state_name': '비전_제정연도'},
    {'state_key': 'school_vision_recent_year', 'state_type': 'value', 'state_name': '비전_최근개정연도'},
    {'state_key': 'school_vision_organization', 'state_type': 'value', 'state_name': '비전_관리기구'},
    {'state_key': 'school_vision_content', 'state_type': 'value', 'state_name': '비전_내용'},
    {'state_key': 'premedical_education_objective_presence', 'state_type': 'value', 'state_name': '교육목적_의예과_유무'},
    {'state_key': 'premedical_education_objective_year', 'state_type': 'value', 'state_name': '교육목적_의예과_제정연도'},
    {'state_key': 'premedical_education_objective_recent_year', 'state_type': 'value', 'state_name': '교육목적_의예과_최근개정연도'},
    {'state_key': 'premedical_education_objective_organization', 'state_type': 'value', 'state_name': '교육목적_의예과_관리기구'},
    {'state_key': 'premedical_education_objective_content', 'state_type': 'value', 'state_name': '교육목적_의예과_내용'},
    {'state_key': 'medical_education_objective_presence', 'state_type': 'value', 'state_name': '교육목적_의학과_유무'},
    {'state_key': 'medical_education_objective_year', 'state_type': 'value', 'state_name': '교육목적_의학과_제정연도'},
    {'state_key': 'medical_education_objective_recent_year', 'state_type': 'value', 'state_name': '교육목적_의학과_최근개정연도'},
    {'state_key': 'medical_education_objective_organization', 'state_type': 'value', 'state_name': '교육목적_의학과_관리기구'},
    {'state_key': 'medical_education_objective_content', 'state_type': 'value', 'state_name': '교육목적_의학과_내용'},
    {'state_key': 'graduation_outcome_presence', 'state_type': 'value', 'state_name': '졸업성과_유무'},
    {'state_key': 'graduation_outcome_year', 'state_type': 'value', 'state_name': '졸업성과_제정연도'},
    {'state_key': 'graduation_outcome_recent_year', 'state_type': 'value', 'state_name': '졸업성과_최근개정연도'},
    {'state_key': 'graduation_outcome_organization', 'state_type': 'value', 'state_name': '졸업성과_관리기구'},
    {'state_key': 'graduation_outcome_content', 'state_type': 'value', 'state_name': '졸업성과_내용'},
    {'state_key': 'phase_outcome_presence', 'state_type': 'value', 'state_name': '시기성과_유무'},
    {'state_key': 'phase_outcome_year', 'state_type': 'value', 'state_name': '시기성과_제정연도'},
    {'state_key': 'phase_outcome_recent_year', 'state_type': 'value', 'state_name': '시기성과_최근개정연도'},
    {'state_key': 'phase_outcome_organization', 'state_type': 'value', 'state_name': '시기성과_관리기구'},
    {'state_key': 'department_president_name', 'state_type': 'value', 'state_name': '학장_성명'},
    {'state_key': 'department_president_inauguration_day', 'state_type': 'value', 'state_name': '학장_취임일'},
    {'state_key': 'department_president_term_ox', 'state_type': 'value', 'state_name': '학장_임기유무'},
    {'state_key': 'department_president_term', 'state_type': 'value', 'state_name': '학장_임기'},
    {'state_key': 'department_president_reappointment_ok', 'state_type': 'value', 'state_name': '학장_연임가능여부'},
    {'state_key': 'department_president_reappointment_ok_etc', 'state_type': 'value', 'state_name': '학장_연임가능여부_기타'},
    {'state_key': 'department_president_reappointment_number', 'state_type': 'value', 'state_name': '학장_연임가능횟수'},
    {'state_key': 'department_president_reappointment_constraint', 'state_type': 'value', 'state_name': '학장_연임가능제한여부'},
    {'state_key': 'department_president_appointing_authority', 'state_type': 'value', 'state_name': '학장_임명권자'},
    {'state_key': 'department_president_appointment_method', 'state_type': 'value', 'state_name': '학장_선임방법'},
    {'state_key': 'department_president_appointment_method_etc', 'state_type': 'value', 'state_name': '학장_선임방법_기타'},
    {'state_key': 'vice_president_system_ok', 'state_type': 'value', 'state_name': '학장_의무부총장_제도'},
    {'state_key': 'vice_president_term', 'state_type': 'value', 'state_name': '학장_의무부총장_임기'},
    {'state_key': 'professor_appointment_recommendation', 'state_type': 'value', 'state_name': '학장_교수_신규임용_추천권'},
    {'state_key': 'professor_promotion_reappointment_recommendation', 'state_type': 'value',
     'state_name': '학장_교수_승진재임용_추천권'},
    {'state_key': 'professor_guaranteed_retirement_recommendation', 'state_type': 'value',
     'state_name': '학장_교수_정년보장_추천권'},
    {'state_key': 'professor_appointment_veto', 'state_type': 'value', 'state_name': '학장_교수_신규임용_거부권'},
    {'state_key': 'professor_promotion_reappointment_veto', 'state_type': 'value', 'state_name': '학장_교수_승진재임용_거부권'},
    {'state_key': 'professor_guaranteed_retirement_veto', 'state_type': 'value', 'state_name': '학장_교수_정년보장_거부권'},
    {'state_key': 'administrative_hiring_recommendation', 'state_type': 'value', 'state_name': '학장_행정직원_신규채용_추천권'},
    {'state_key': 'administrative_promotion_recommendation', 'state_type': 'value', 'state_name': '학장_행정직원_승진_추천권'},
    {'state_key': 'administrative_hiring_veto', 'state_type': 'value', 'state_name': '학장_행정직원_신규채용_거부권'},
    {'state_key': 'administrative_promotion_veto', 'state_type': 'value', 'state_name': '학장_행정직원_승진_거부권'},
    {'state_key': 'professor_appointment_etc', 'state_type': 'value', 'state_name': '학장_교수_신규임용_기타'},
    {'state_key': 'professor_promotion_reappointment_etc', 'state_type': 'value', 'state_name': '학장_교수_승진재임용_기타'},
    {'state_key': 'professor_guaranteed_retirement_etc', 'state_type': 'value', 'state_name': '학장_교수_정년보장_기타'},
    {'state_key': 'administrative_hiring_etc', 'state_type': 'value', 'state_name': '학장_행정직원_신규채용_기타'},
    {'state_key': 'administrative_promotion_etc', 'state_type': 'value', 'state_name': '학장_행정직원_승진_기타'},
    {'state_key': 'budget_writing_authority', 'state_type': 'value', 'state_name': '학장_예산작성권'},
    {'state_key': 'budget_execution_authority', 'state_type': 'value', 'state_name': '학장_예산집행권'},
    {'state_key': 'budget_writing_authority_etc', 'state_type': 'value', 'state_name': '학장_예산작성권_기타'},
    {'state_key': 'budget_execution_authority_etc', 'state_type': 'value', 'state_name': '학장_예산집행권_기타'},
    {'state_key': 'budget_amount', 'state_type': 'value', 'state_name': '학장_1회전결가능_금액'},
    {'state_key': 'budget_opinion_collection_regulation', 'state_type': 'value', 'state_name': '학장_예산의견수렴규정'},
    {'state_key': 'administrative_structure', 'state_type': 'data', 'state_name': '행정구조'},
    {'state_key': 'administrative_structure_etc', 'state_type': 'value', 'state_name': '행정구조_기타'},
    {'state_key': 'education_process_curriculum_committee_presence', 'state_type': 'value', 'state_name': '교육과정위원회_유무'},
    {'state_key': 'education_process_curriculum_committee_name', 'state_type': 'value', 'state_name': '교육과정위원회_명칭'},
    {'state_key': 'education_process_curriculum_committee_education_process', 'state_type': 'value',
     'state_name': '교육과정위원회_담당교육과정'},
    {'state_key': 'education_process_curriculum_committee_head', 'state_type': 'value', 'state_name': '교육과정위원회_구성_위원장'},
    {'state_key': 'education_process_curriculum_committee_head_type', 'state_type': 'value',
     'state_name': '교육과정위원회_구성_당연직구분'},
    {'state_key': 'education_process_curriculum_committee_head_type_etc', 'state_type': 'value',
     'state_name': '교육과정위원회_구성_당연직구분_기타'},
    {'state_key': 'education_process_curriculum_committee_num', 'state_type': 'data', 'state_name': '교육과정위원회_위원수'},
    {'state_key': 'education_process_curriculum_committee_period', 'state_type': 'value', 'state_name': '교육과정위원회_위원임기'},
    {'state_key': 'education_process_curriculum_committee_opening_num', 'state_type': 'value',
     'state_name': '교육과정위원회_연간회의개최횟수'},
    {'state_key': 'education_process_curriculum_characteristics_operation', 'state_type': 'value',
     'state_name': '교육과정특성_학제'},
    {'state_key': 'education_process_curriculum_characteristics_advantages', 'state_type': 'value',
     'state_name': '교육과정특성_특장점'},
    {'state_key': 'education_process_curriculum_characteristics_principles', 'state_type': 'value',
     'state_name': '교육과정특성_편성원칙'},
    {'state_key': 'education_process_curriculum_operation', 'state_type': 'data', 'state_name': '행정구조_기타'},
    {'state_key': 'education_process_curriculum_week', 'state_type': 'data', 'state_name': '교육주수'},
    {'state_key': 'pre_medicine_class', 'state_type': 'data', 'state_name': '개설교과목_의예과'},
    {'state_key': 'medicine_class', 'state_type': 'data', 'state_name': '개설교과목_의학과'},
    {'state_key': 'pre_medicine_total_credit', 'state_type': 'value', 'state_name': '수료요건_의예과_총이수학점'},
    {'state_key': 'pre_medicine_required_major_credit', 'state_type': 'value', 'state_name': '수료요건_의예과_전공필수'},
    {'state_key': 'pre_medicine_optional_major_credit', 'state_type': 'value', 'state_name': '수료요건_의예과_전공선택'},
    {'state_key': 'pre_medicine_liberal_credit', 'state_type': 'value', 'state_name': '수료요건_의예과_교양'},
    {'state_key': 'pre_medicine_etc_credit', 'state_type': 'value', 'state_name': '수료요건_의예과_기타'},
    {'state_key': 'pre_medicine_etc_condition', 'state_type': 'value', 'state_name': '수료요건_의예과_기타요구조건'},
    {'state_key': 'pre_medicine_etc_condition_etc', 'state_type': 'value', 'state_name': '수료요건_의예과_기타요구조건_기타'},
    {'state_key': 'medicine_total_credit', 'state_type': 'value', 'state_name': '졸업요건_의학과_총이수학점'},
    {'state_key': 'medicine_required_major_credit', 'state_type': 'value', 'state_name': '졸업요건_의학과_전공필수'},
    {'state_key': 'medicine_optional_major_credit', 'state_type': 'value', 'state_name': '졸업요건_의학과_전공선택'},
    {'state_key': 'medicine_etc_credit', 'state_type': 'value', 'state_name': '졸업요건_의학과_기타'},
    {'state_key': 'medicine_etc_condition', 'state_type': 'value', 'state_name': '졸업요건_의학과_기타요구조건'},
    {'state_key': 'medicine_etc_condition_etc', 'state_type': 'value', 'state_name': '졸업요건_의학과_기타요구조건_기타'},
    {'state_key': 'education_process_curriculum_clinical_practice_week', 'state_type': 'data',
     'state_name': '임상실습_교육주수'},
    {'state_key': 'education_process_curriculum_clinical_practice_required', 'state_type': 'data',
     'state_name': '임상실습_개설과목_필수'},
    {'state_key': 'education_process_curriculum_clinical_practice_optional_ox', 'state_type': 'value',
     'state_name': '임상실습_개설과목_선택_운영여부'},
    {'state_key': 'education_process_curriculum_clinical_practice_optional', 'state_type': 'data',
     'state_name': '임상실습_개설과목_선택'},
    {'state_key': 'education_process_curriculum_clinical_practice_intern_ox', 'state_type': 'value',
     'state_name': '임상실습_학생인턴_운영여부'},
    {'state_key': 'education_process_curriculum_clinical_practice_intern', 'state_type': 'data',
     'state_name': '임상실습_학생인턴'},
    {'state_key': 'introduction_to_clinical_practice_patient_interview_training_time', 'state_type': 'data',
     'state_name': '임상실습입문_환자면담'},
    {'state_key': 'treatment_performance_clinical_skill_training_time', 'state_type': 'data',
     'state_name': '진료수행_임상술기'},
    {'state_key': 'pre_medicine_evaluation', 'state_type': 'value', 'state_name': '학생평가_의예과_평가방법'},
    {'state_key': 'pre_medicine_relative_evaluation_grade', 'state_type': 'value', 'state_name': '학생평가_의예과_상대평가_등급'},
    {'state_key': 'pre_medicine_absolute_evaluation_grade', 'state_type': 'value', 'state_name': '학생평가_의예과_절대평가_등급'},
    {'state_key': 'medicine_evaluation', 'state_type': 'value', 'state_name': '학생평가_의학과_평가방법'},
    {'state_key': 'medicine_relative_evaluation_grade', 'state_type': 'value', 'state_name': '학생평가_의학과_상대평가_등급'},
    {'state_key': 'medicine_absolute_evaluation_grade', 'state_type': 'value', 'state_name': '학생평가_의학과_절대평가_등급'},
    {'state_key': 'criteria_repeating', 'state_type': 'value', 'state_name': '학생평가_유급기준'},
    {'state_key': 'criteria_repeating_content', 'state_type': 'value', 'state_name': '학생평가_유급기준_내용'},
    {'state_key': 'criteria_expulsion', 'state_type': 'value', 'state_name': '학생평가_제적기준'},
    {'state_key': 'criteria_expulsion_content', 'state_type': 'value', 'state_name': '학생평가_제적기준_내용'},
    {'state_key': 'education_process_educational_department_ox', 'state_type': 'value', 'state_name': '의학교육_전문부서_유무'},
    {'state_key': 'education_process_educational_department', 'state_type': 'data', 'state_name': '의학교육_전문부서'},
    {'state_key': 'education_process_humanity_department_ox', 'state_type': 'value', 'state_name': '의료인문학_전문부서_유무'},
    {'state_key': 'education_process_humanity_department', 'state_type': 'data', 'state_name': '의료인문학_전문부서'},
    {'state_key': 'student_admission_system_manager', 'state_type': 'value', 'state_name': '입학업무_담당'},
    {'state_key': 'student_admission_system_manager_etc', 'state_type': 'value', 'state_name': '입학업무_담당_기타'},
    {'state_key': 'rolling_student_admission_system_data', 'state_type': 'data', 'state_name': '입학제도_수시모집'},
    {'state_key': 'regular_student_admission_system_data', 'state_type': 'data', 'state_name': '입학제도_정시모집'},
    {'state_key': 'student_admission_student', 'state_type': 'data', 'state_name': '입학학생수'},
    {'state_key': 'student_enrolled_student', 'state_type': 'data', 'state_name': '재적학생수'},
    {'state_key': 'student_admission_student_structure', 'state_type': 'data', 'state_name': '의예과입학학생구성'},
    {'state_key': 'student_scholarship', 'state_type': 'data', 'state_name': '장학금수혜현황'},
    {'state_key': 'student_graduate_career', 'state_type': 'data', 'state_name': '졸업생의진로'},
    {'state_key': 'student_graduate_student_basic_domestic', 'state_type': 'data',
     'state_name': '의학계열_대학원_학생_수_기초의학_내국인'},
    {'state_key': 'student_graduate_student_basic_foreigner', 'state_type': 'data',
     'state_name': '의학계열_대학원_학생_수_기초의학_외국인'},
    {'state_key': 'student_graduate_student_clinical_domestic', 'state_type': 'data',
     'state_name': '의학계열_대학원_학생_수_임상의학_내국인'},
    {'state_key': 'student_education_affiliated_hospital', 'state_type': 'data', 'state_name': '교육병원_부속병원'},
    {'state_key': 'student_education_partner_hospital', 'state_type': 'data', 'state_name': '교육병원_협력병원'},
    {'state_key': 'student_support_organization_ox', 'state_type': 'value', 'state_name': '학생지원전담기구_유무'},
    {'state_key': 'student_support_organization', 'state_type': 'data', 'state_name': '학생지원_전담기구'},
    {'state_key': 'student_support_program', 'state_type': 'data', 'state_name': '주요_학생지원_프로그램'},
    {'state_key': 'student_health_checkup_ox', 'state_type': 'value', 'state_name': '학생_건강검진_시행여부'},
    {'state_key': 'student_health_checkup_period', 'state_type': 'value', 'state_name': '학생_건강검진_시행시기'},
    {'state_key': 'student_health_checkup_period_etc', 'state_type': 'value', 'state_name': '학생_건강검진_시행시기_기타'},
    {'state_key': 'student_safety_guideline_ox', 'state_type': 'value', 'state_name': '학생_안전관리_지침_유무'},
    {'state_key': 'student_safety_education_ox', 'state_type': 'value', 'state_name': '학생_안전관리_교육_여부'},
    {'state_key': 'student_safety_education_period', 'state_type': 'value', 'state_name': '학생_안전관리_교육_시행_시기'},
    {'state_key': 'student_safety_education_period_etc', 'state_type': 'value', 'state_name': '학생_안전관리_교육_시행_시기_기타'},
    {'state_key': 'student_vaccination_ox', 'state_type': 'value', 'state_name': '학생_안전관리_교육_예방접종_여부'},
    {'state_key': 'student_school_life_insurance_ox', 'state_type': 'value', 'state_name': '학생_안전관리_교육_안전관련_보험가입_여부'},
    {'state_key': 'student_clinical_insurance_ox', 'state_type': 'value', 'state_name': '학생_안전관리_교육_임상실습_보험가입_여부'},
    {'state_key': 'student_per_professor', 'state_type': 'data', 'state_name': '지도교수당_평균학생수'},
    {'state_key': 'student_international_exchange', 'state_type': 'data', 'state_name': '학생_국제교류_현황'},
    {'state_key': 'professor_professor_basic', 'state_type': 'data', 'state_name': '교원수_기초의학'},
    {'state_key': 'professor_professor_clinical', 'state_type': 'data', 'state_name': '교원수_임상의학'},
    {'state_key': 'professor_full_time_new_basic_professor_data', 'state_type': 'data',
     'state_name': '전임교원수_변화_기초의학_신규임용'},
    {'state_key': 'professor_full_time_retire_basic_professor_data', 'state_type': 'data',
     'state_name': '전임교원수_변화_기초의학_정년퇴임'},
    {'state_key': 'professor_full_time_new_clinical_professor_data', 'state_type': 'data',
     'state_name': '전임교원수_변화_임상의학_신규임용'},
    {'state_key': 'professor_full_time_retire_clinical_professor_data', 'state_type': 'data',
     'state_name': '전임교원수_변화_임상의학_정년퇴임'},
    {'state_key': 'professor_medical_education_training', 'state_type': 'data', 'state_name': '의학교육_관련_연수'},
    {'state_key': 'professor_specialized_teaching_track', 'state_type': 'value', 'state_name': '교수개발_승진체계_교수트랙_운영_여부'},
    {'state_key': 'professor_specialized_teaching_track_etc', 'state_type': 'value',
     'state_name': '교수개발_승진체계_교수트랙_운영_여부_비고'},
    {'state_key': 'professor_evaluation_system_by_rank', 'state_type': 'value',
     'state_name': '교수개발_승진체계_직급별_평가제도_운영_여부'},
    {'state_key': 'professor_evaluation_system_by_rank_etc', 'state_type': 'value',
     'state_name': '교수개발_승진체계_직급별_평가제도_운영_여부_비고'},
    {'state_key': 'professor_evaluation_system_by_function', 'state_type': 'value',
     'state_name': '교수개발_승진체계_기능별_평가제도_운영_여부'},
    {'state_key': 'professor_evaluation_system_by_function_etc', 'state_type': 'value',
     'state_name': '교수개발_승진체계_기능별_평가제도_운영_여부_비고'},
    {'state_key': 'professor_educational_achievement_require', 'state_type': 'value',
     'state_name': '교수개발_승진체계_교육업적_요구_여부'},
    {'state_key': 'professor_educational_achievement_require_etc', 'state_type': 'value',
     'state_name': '교수개발_승진체계_교육업적_요구_여부_비고'},
    {'state_key': 'professor_new_faculty_training_require', 'state_type': 'value',
     'state_name': '교수개발_승진체계_신임교원_연수교육_여부'},
    {'state_key': 'professor_new_faculty_training_require_etc', 'state_type': 'value',
     'state_name': '교수개발_승진체계_신임교원_연수교육_여부_비고'},
    {'state_key': 'professor_new_faculty_number', 'state_type': 'value', 'state_name': '교수개발_승진체계_신임교원_연수교육_교원수'},
    {'state_key': 'professor_new_faculty_number_trained', 'state_type': 'value',
     'state_name': '교수개발_승진체계_신임교원_연수교육_이수완료수'},
    {'state_key': 'professor_full_time_faculty_training_require', 'state_type': 'value',
     'state_name': '교수개발_승진체계_전임교원_프로그램참여_여부'},
    {'state_key': 'professor_full_time_faculty_training_require_etc', 'state_type': 'value',
     'state_name': '교수개발_승진체계_전임교원_프로그램참여_여부_비고'},
    {'state_key': 'professor_full_time_faculty_number', 'state_type': 'value',
     'state_name': '교수개발_승진체계_전임교원_프로그램참여_교원수'},
    {'state_key': 'professor_full_time_faculty_number_trained', 'state_type': 'value',
     'state_name': '교수개발_승진체계_전임교원_프로그램참여_이수완료수'},
    {'state_key': 'facility_num_lecture_room', 'state_type': 'value', 'state_name': '교육기본시설_강의실수'},
    {'state_key': 'facility_num_laboratory', 'state_type': 'value', 'state_name': '교육기본시설_실험실습실수'},
    {'state_key': 'clinical_center_ox', 'state_type': 'value', 'state_name': '임상술기센터_센터유무'},
    {'state_key': 'clinical_center_where', 'state_type': 'value', 'state_name': '임상술기센터_센터위치'},
    {'state_key': 'clinical_center_practical_num', 'state_type': 'value', 'state_name': '임상술기센터_실습방수'},
    {'state_key': 'clinical_center_mock_test_num', 'state_type': 'value', 'state_name': '임상술기센터_모의시험가능장소'},
    {'state_key': 'clinical_center_lecture_num', 'state_type': 'value', 'state_name': '임상술기센터_강의실수'},
    {'state_key': 'clinical_center_equipment', 'state_type': 'data', 'state_name': '임상술기센터_구형장비'},
    {'state_key': 'clinical_center_student_space_ox', 'state_type': 'value', 'state_name': '교육병원내_학생전용공간_유무'},
    {'state_key': 'clinical_center_student_space', 'state_type': 'data', 'state_name': '교육병원내_학생전용공간'},
    {'state_key': 'clinical_center_education_facility_ox', 'state_type': 'value', 'state_name': '교육병원내_학생교육시설_유무'},
    {'state_key': 'clinical_center_education_facility', 'state_type': 'data', 'state_name': '교육병원내_학생교육시설'},
    {'state_key': 'medical_library_present', 'state_type': 'value', 'state_name': '의학도서관_유무'},
    {'state_key': 'medical_library_type', 'state_type': 'data', 'state_name': '의학도서관_종류'},
    {'state_key': 'medical_library_independent_academin_information_system', 'state_type': 'value',
     'state_name': '독립적_학술정보서비스_체제_구축_여부'},
    {'state_key': 'medical_library_annual_budget', 'state_type': 'value', 'state_name': '학술정보서비스_연간_예산액'},
    {'state_key': 'medical_library_annual_budget_execution', 'state_type': 'value', 'state_name': '학술정보서비스_연간_예산_집행액'},
    {'state_key': 'medical_library_professional_manpower', 'state_type': 'value', 'state_name': '학술정보서비스_전문인력'},
    {'state_key': 'facility_student_small_group_discussion_room', 'state_type': 'data', 'state_name': '학생_소그룹_토의실'},
    {'state_key': 'student_housing_status_survey', 'state_type': 'value', 'state_name': '학생_주거현황_조사_실시_여부'},
    {'state_key': 'dormitory_type', 'state_type': 'value', 'state_name': '기숙사_형태'},
    {'state_key': 'dormitory_type_etc', 'state_type': 'value', 'state_name': '기숙사_형태_기타'},
    {'state_key': 'dormitory_student_num', 'state_type': 'data', 'state_name': '입실_학생수'},
    {'state_key': 'student_satisfaction_survey', 'state_type': 'value', 'state_name': '학생_만족도_조사_실시_여부'},
    {'state_key': 'dormitory_cost', 'state_type': 'data', 'state_name': '학기별_기숙사비'},
    {'state_key': 'student_self_study_space', 'state_type': 'data', 'state_name': '학생_자율학습_공간'},
    {'state_key': 'student_self_study_space_ox', 'state_type': 'value', 'state_name': '학생_자율학습_공간_유무'},
    {'state_key': 'facility_student_welfare_facility', 'state_type': 'data', 'state_name': '학생_복지시설'},
    {'state_key': 'facility_student_welfare_convenient', 'state_type': 'data', 'state_name': '학생_편의시설'},
    {'state_key': 'information_manpower', 'state_type': 'value', 'state_name': '정보화_전담인력_유무'},
    {'state_key': 'facility_education_management_system', 'state_type': 'data', 'state_name': '교육관리시스템'},
    {'state_key': 'facility_education_evaluation_system', 'state_type': 'data', 'state_name': '교육평가시스템'},
    {'state_key': 'facility_student_research_laboratory_presence', 'state_type': 'value', 'state_name': '학생_연구실험실_유무'},
    {'state_key': 'facility_student_research_laboratory_number', 'state_type': 'value', 'state_name': '총_실험실_수'},
    {'state_key': 'facility_student_research_laboratory', 'state_type': 'data', 'state_name': '이용대상학년_이용실적'},
    {'state_key': 'educational_competency_enhancement_support_policy_presence', 'state_type': 'value',
     'state_name': '교육역량_강화지원_정책_유무'},
    {'state_key': 'professional_competency_enhancement_support_policy_presence', 'state_type': 'value',
     'state_name': '전문역량_강화지원_정책_유무'},
    {'state_key': 'management_finance_budget', 'state_type': 'value', 'state_name': '경영재정_역량개발_예산액'},
    {'state_key': 'management_finance_budget_execution', 'state_type': 'value', 'state_name': '경영재정_역량개발_집행액'},
    {'state_key': 'management_finance_student_education', 'state_type': 'data', 'state_name': '학생교육_관련_비용'},
    {'state_key': 'management_finance_student_tuition_medical_school', 'state_type': 'data',
     'state_name': '학생등록금_의과대학'},
    {'state_key': 'management_finance_student_tuition_graduate_medicine', 'state_type': 'data',
     'state_name': '학생등록금_의학전문대학원'},
]

total_state_list = [
    State({'type': d['state_key'], 'index': ALL}, d['state_type']) for d in total_state_key_dict
]


def combine_html(fig_list):
    html_list = [fig.to_html(full_html=False, include_plotlyjs='cdn') for fig in fig_list]
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>My Dashboard</title>
    </head>
    <body>
    <h1>My Dashboard</h1>
    {charts}
    </body>
    </html>
    """
    charts = ''
    for html in html_list:
        charts += html
    combined_html = html_template.format(charts=charts)
    return combined_html


def visualize_education_process_curriculum_committee_num(table_data):
    charts = []
    for indiv_data in table_data:
        df = pd.DataFrame([indiv_data])
        fig = px.pie(df,
                     values=df.drop(columns=['구분', '계']).values[0],
                     names=df.drop(columns=['구분', '계']).columns, title=f"구분: {indiv_data['구분']}")
        charts.append(fig)
    fig = px.pie(pd.DataFrame(table_data), values='계', names='구분')
    charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_school_sum_alumni(table_data):
    charts = []
    for indiv_data in table_data:
        df = pd.DataFrame([indiv_data])
        fig = px.pie(df,
                     values=df.drop(columns=['계']).values[0],
                     names=df.drop(columns=['계']).columns)
        charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_administrative_structure(table_data):
    charts = []
    total_drop_column = ['업무분야', '담당부서명', '책임보직명', '보직수당_있음', '보직수당_없음', '합계']
    for indiv_data in table_data:
        df = pd.DataFrame([indiv_data])
        drop_column = [col for col in total_drop_column if col in df.columns]
        fig = px.pie(df,
                     values=df.drop(columns=drop_column).values[0],
                     names=df.drop(columns=drop_column).columns,
                     title=f"구분: {indiv_data['업무분야']}")
        charts.append(fig)
    df = pd.DataFrame(table_data)
    df_filtered = df[df['업무분야'] != '합계']
    fig = px.pie(df_filtered, values='합계', names='업무분야')
    charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_education_process_curriculum_week(table_data):
    charts = []
    total_drop_column = ['학기']
    for indiv_data in table_data:
        df = pd.DataFrame([indiv_data])
        drop_column = [col for col in total_drop_column if col in df.columns]
        fig = px.pie(df,
                     values=df.drop(columns=drop_column).values[0],
                     names=df.drop(columns=drop_column).columns,
                     title=f"구분: {indiv_data['학기']}")
        charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_education_process_curriculum_clinical_practice_week(table_data):
    charts = []
    total_drop_column = ['학년', '합계']
    for indiv_data in table_data:
        df = pd.DataFrame([indiv_data])
        drop_column = [col for col in total_drop_column if col in df.columns]
        fig = px.pie(df,
                     values=df.drop(columns=drop_column).values[0],
                     names=df.drop(columns=drop_column).columns,
                     title=f"구분: {indiv_data['학년']}")
        charts.append(fig)
    df = pd.DataFrame(table_data)
    df_filtered = df[df['학년'] != '합계']
    fig = px.pie(df_filtered, values='합계', names='학년')
    charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_education_process_educational_department(table_data):
    charts = []
    total_drop_column = ['전문부서명', '합계']
    for indiv_data in table_data:
        df = pd.DataFrame([indiv_data])
        drop_column = [col for col in total_drop_column if col in df.columns]
        fig = px.pie(df,
                     values=df.drop(columns=drop_column).values[0],
                     names=df.drop(columns=drop_column).columns,
                     title=f"구분: {indiv_data['전문부서명']}")
        charts.append(fig)
    df = pd.DataFrame(table_data)
    df_filtered = df[df['전문부서명'] != '합계']
    fig = px.pie(df_filtered, values='합계', names='전문부서명')
    charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_education_process_humanity_department(table_data):
    charts = []
    total_drop_column = ['전문부서명', '합계']
    for indiv_data in table_data:
        df = pd.DataFrame([indiv_data])
        drop_column = [col for col in total_drop_column if col in df.columns]
        fig = px.pie(df,
                     values=df.drop(columns=drop_column).values[0],
                     names=df.drop(columns=drop_column).columns,
                     title=f"구분: {indiv_data['전문부서명']}")
        charts.append(fig)
    df = pd.DataFrame(table_data)
    df_filtered = df[df['전문부서명'] != '합계']
    fig = px.pie(df_filtered, values='합계', names='전문부서명')
    charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_student_admission_student(table_data):
    charts = []
    total_drop_column = ['구분', '성별', '합계']
    for indiv_data in table_data:
        df = pd.DataFrame([indiv_data])
        drop_column = [col for col in total_drop_column if col in df.columns]
        fig = px.pie(df,
                     values=df.drop(columns=drop_column).values[0],
                     names=df.drop(columns=drop_column).columns,
                     title=f"구분: {indiv_data['구분']}_{indiv_data['성별']}")
        charts.append(fig)
    df = pd.DataFrame(table_data)
    df_filtered = df[df['성별'] != '합']
    fig = px.pie(df_filtered, values='합계', names='구분')
    charts.append(fig)
    fig = px.pie(df_filtered, values='합계', names='성별')
    charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_student_enrolled_student(table_data):
    charts = []
    total_drop_column = ['구분', '성별', '합계']
    for indiv_data in table_data:
        df = pd.DataFrame([indiv_data])
        drop_column = [col for col in total_drop_column if col in df.columns]
        fig = px.pie(df,
                     values=df.drop(columns=drop_column).values[0],
                     names=df.drop(columns=drop_column).columns,
                     title=f"구분: {indiv_data['구분']}_{indiv_data['성별']}")
        charts.append(fig)
    df = pd.DataFrame(table_data)
    df['계'] = \
        pd.to_numeric(df['의예과_1학년_1학기']) + pd.to_numeric(df['의예과_1학년_2학기']) + pd.to_numeric(
            df['의예과_2학년_1학기']) + pd.to_numeric(df['의예과_2학년_2학기']) + pd.to_numeric(df['의학과_1학년_1학기']) + pd.to_numeric(
            df['의학과_1학년_2학기']) + pd.to_numeric(df['의학과_2학년_1학기']) + pd.to_numeric(df['의학과_2학년_2학기']) + pd.to_numeric(
            df['의학과_3학년_1학기']) + pd.to_numeric(df['의학과_3학년_2학기']) + pd.to_numeric(df['의학과_4학년_1학기']) + pd.to_numeric(
            df['의학과_4학년_2학기'])
    df_filtered = df[df['성별'] == '계']

    fig = px.pie(df_filtered, values='계', names='구분')
    charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_student_admission_student_structure(table_data):
    charts = []
    total_drop_column = ['입학전형', '총 입학생 대비 비율(%)']
    for indiv_data in table_data:
        df = pd.DataFrame([indiv_data])
        drop_column = [col for col in total_drop_column if col in df.columns]
        fig = px.pie(df,
                     values=df.drop(columns=drop_column).values[0],
                     names=df.drop(columns=drop_column).columns,
                     title=f"구분: {indiv_data['입학전형']}")
        charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_student_scholarship(table_data):
    charts = []
    df = []
    for indiv_data in table_data:
        for k, v in indiv_data.items():
            if isinstance(v, str) and v.isdigit():
                indiv_data[k] = int(v)
        df.append(indiv_data)
    df = pd.DataFrame(df)
    df_filtered = df[df['구분'] != '합계']
    for label in ['의예과_수혜금액', '의예과_수혜학생', '의학과_수혜금액', '의학과_수혜학생']:
        fig = px.bar(df_filtered,
                     x=label, color='구분')
        charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_student_graduate_career(table_data):
    charts = []
    df = []
    for indiv_data in table_data:
        for k, v in indiv_data.items():
            if isinstance(v, str) and v.isdigit():
                df.append({'구분': k, '수': int(v)})
    df = pd.DataFrame(df)
    df_filtered = df[df['구분'] != '합계']
    fig = px.bar(df_filtered,
                 x='구분', y='수', color='구분'
                 )
    charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_student_graduate_student_basic_domestic(table_data):
    charts = []
    drop_column = ['전공분야']
    dict_by_major = []
    for indiv_data in table_data:
        for k, v in indiv_data.items():
            if isinstance(v, str) and v.isdigit():
                indiv_data[k] = int(v)
        fig = px.pie(pd.DataFrame([indiv_data]),
                     values=pd.DataFrame([indiv_data]).drop(columns=drop_column).values[0],
                     names=pd.DataFrame([indiv_data]).drop(columns=drop_column).columns)
        charts.append(fig)
        sum_num = sum([indiv_data[col] for col in indiv_data if col not in drop_column])
        dict_by_major.append({"구분": indiv_data['전공분야'], "수": sum_num})
    df = pd.DataFrame(dict_by_major)
    fig = px.bar(df, x='구분', y='수', color='구분')
    charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_student_graduate_student_basic_foreigner(table_data):
    charts = []
    drop_column = ['전공분야']
    dict_by_major = []
    for indiv_data in table_data:
        for k, v in indiv_data.items():
            if isinstance(v, str) and v.isdigit():
                indiv_data[k] = int(v)
        fig = px.pie(pd.DataFrame([indiv_data]),
                     values=pd.DataFrame([indiv_data]).drop(columns=drop_column).values[0],
                     names=pd.DataFrame([indiv_data]).drop(columns=drop_column).columns)
        charts.append(fig)
        sum_num = sum([indiv_data[col] for col in indiv_data if col not in drop_column])
        dict_by_major.append({"구분": indiv_data['전공분야'], "수": sum_num})
    df = pd.DataFrame(dict_by_major)
    fig = px.bar(df, x='구분', y='수', color='구분')
    charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_student_graduate_student_clinical_domestic(table_data):
    charts = []
    drop_column = ['전공분야']
    dict_by_major = []
    for indiv_data in table_data:
        for k, v in indiv_data.items():
            if isinstance(v, str) and v.isdigit():
                indiv_data[k] = int(v)
        fig = px.pie(pd.DataFrame([indiv_data]),
                     values=pd.DataFrame([indiv_data]).drop(columns=drop_column).values[0],
                     names=pd.DataFrame([indiv_data]).drop(columns=drop_column).columns)
        charts.append(fig)
        sum_num = sum([indiv_data[col] for col in indiv_data if col not in drop_column])
        dict_by_major.append({"구분": indiv_data['전공분야'], "수": sum_num})
    df = pd.DataFrame(dict_by_major)
    fig = px.bar(df, x='구분', y='수', color='구분')
    charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_student_graduate_student_clinical_foreigner(table_data):
    charts = []
    drop_column = ['전공분야']
    dict_by_major = []
    for indiv_data in table_data:
        for k, v in indiv_data.items():
            if isinstance(v, str) and v.isdigit():
                indiv_data[k] = int(v)
        fig = px.pie(pd.DataFrame([indiv_data]),
                     values=pd.DataFrame([indiv_data]).drop(columns=drop_column).values[0],
                     names=pd.DataFrame([indiv_data]).drop(columns=drop_column).columns)
        charts.append(fig)
        sum_num = sum([indiv_data[col] for col in indiv_data if col not in drop_column])
        dict_by_major.append({"구분": indiv_data['전공분야'], "수": sum_num})
    df = pd.DataFrame(dict_by_major)
    fig = px.bar(df, x='구분', y='수', color='구분')
    charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_student_per_professor(table_data):
    # TODO
    charts = []
    graph_html = combine_html(charts)
    return graph_html


def visualize_student_international_exchange(table_data):
    # TODO
    charts = []
    graph_html = combine_html(charts)
    return graph_html


def visualize_professor_professor_basic(table_data):
    charts = []
    drop_column = ['소속교실', '구분']
    dict_by_major = []
    for indiv_data in table_data:
        for k, v in indiv_data.items():
            if isinstance(v, str) and v.isdigit():
                indiv_data[k] = int(v)
    for indiv_data in table_data:
        target_dict_1 = []
        target_dict_2 = []
        for k, v in indiv_data.items():
            if k.startswith('전임교원'):
                target_dict_1.append({"구분": k, "수": v})
            else:
                target_dict_2.append({"구분": k, "수": v})
        fig = px.bar(pd.DataFrame(target_dict_1),
                     x='구분', y='수', color='구분')
        charts.append(fig)
        fig = px.bar(pd.DataFrame(target_dict_2),
                     x='구분', y='수', color='구분')
        charts.append(fig)
        sum_num = sum([indiv_data[col] for col in indiv_data if col not in drop_column])
        dict_by_major.append({"구분": indiv_data['구분'], "수": sum_num})
    df = pd.DataFrame(dict_by_major)
    fig = px.bar(df, x='구분', y='수', color='구분')
    charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_professor_professor_clinical(table_data):
    charts = []
    drop_column = ['소속교실', '구분']
    dict_by_major = []
    for indiv_data in table_data:
        for k, v in indiv_data.items():
            if isinstance(v, str) and v.isdigit():
                indiv_data[k] = int(v)
    for indiv_data in table_data:
        target_dict_1 = []
        target_dict_2 = []
        for k, v in indiv_data.items():
            if k.startswith('전임교원'):
                target_dict_1.append({"구분": k, "수": v})
            else:
                target_dict_2.append({"구분": k, "수": v})
        fig = px.bar(pd.DataFrame(target_dict_1),
                     x='구분', y='수', color='구분')
        charts.append(fig)
        fig = px.bar(pd.DataFrame(target_dict_2),
                     x='구분', y='수', color='구분')
        charts.append(fig)
        sum_num = sum([indiv_data[col] for col in indiv_data if col not in drop_column])
        dict_by_major.append({"구분": indiv_data['구분'], "수": sum_num})
    df = pd.DataFrame(dict_by_major)
    fig = px.bar(df, x='구분', y='수', color='구분')
    charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_professor_full_time_new_basic_professor_data(table_data):
    charts = []
    drop_column = ['성별']
    for indiv_data in table_data:
        for k, v in indiv_data.items():
            if isinstance(v, str) and v.isdigit():
                indiv_data[k] = int(v)
        fig = px.pie(pd.DataFrame([indiv_data]),
                     values=pd.DataFrame([indiv_data]).drop(columns=drop_column).values[0],
                     names=pd.DataFrame([indiv_data]).drop(columns=drop_column).columns)
        charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_professor_full_time_retire_basic_professor_data(table_data):
    charts = []
    drop_column = ['성별']
    for indiv_data in table_data:
        for k, v in indiv_data.items():
            if isinstance(v, str) and v.isdigit():
                indiv_data[k] = int(v)
        fig = px.pie(pd.DataFrame([indiv_data]),
                     values=pd.DataFrame([indiv_data]).drop(columns=drop_column).values[0],
                     names=pd.DataFrame([indiv_data]).drop(columns=drop_column).columns)
        charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_professor_full_time_new_clinical_professor_data(table_data):
    charts = []
    drop_column = ['성별']
    for indiv_data in table_data:
        for k, v in indiv_data.items():
            if isinstance(v, str) and v.isdigit():
                indiv_data[k] = int(v)
        fig = px.pie(pd.DataFrame([indiv_data]),
                     values=pd.DataFrame([indiv_data]).drop(columns=drop_column).values[0],
                     names=pd.DataFrame([indiv_data]).drop(columns=drop_column).columns)
        charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_professor_full_time_retire_clinical_professor_data(table_data):
    charts = []
    drop_column = ['성별']
    for indiv_data in table_data:
        for k, v in indiv_data.items():
            if isinstance(v, str) and v.isdigit():
                indiv_data[k] = int(v)
        fig = px.pie(pd.DataFrame([indiv_data]),
                     values=pd.DataFrame([indiv_data]).drop(columns=drop_column).values[0],
                     names=pd.DataFrame([indiv_data]).drop(columns=drop_column).columns)
        charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_professor_medical_education_training(table_data):
    charts = []
    training_type_list = ['세미나', '학회', '워크숍', '연수']
    for indiv_data in table_data:
        for training_type in training_type_list:
            df = []
            for t in ['교내', '교외']:
                df.append({'구분': f'{training_type}_{t}', '수': indiv_data[f'{training_type}_{t}']})
            fig = px.pie(df, names='구분', values='수', title=f'{training_type}')
            charts.append(fig)

    graph_html = combine_html(charts)
    return graph_html


def visualize_management_finance_student_tuition_medical_school(table_data):
    anonymous = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    total_tuition_list = [{
        "이름": "서울의대",
        '등록금': 800,
        "구분": "서울의대"
    }]
    charts = []
    for i in range(10):
        total_tuition_list.append({"이름": anonymous[i], '등록금': np.random.randint(500, 1000),
                                   "구분": "타대학"})
    total_tuition_list = sorted(total_tuition_list, key=lambda x: x['등록금'])
    fig = px.bar(pd.DataFrame(total_tuition_list),
                 x='이름', y='등록금', color='구분')
    charts.append(fig)
    graph_html = combine_html(charts)
    return graph_html


def visualize_management_finance_student_tuition_graduate_medicine(table_data):
    # TODO
    charts = []
    graph_html = combine_html(charts)
    return graph_html


visualize_state_dict = [
    {'state_key': 'visualize_education_process_curriculum_committee_num',
     'function': visualize_education_process_curriculum_committee_num,
     'file_name': '교육과정위원회_위원수'
     },
    {'state_key': 'visualize_school_sum_alumni',
     'function': visualize_school_sum_alumni,
     'file_name': '누적_졸업생'
     },
    {'state_key': 'visualize_administrative_structure',
     'function': visualize_administrative_structure,
     'file_name': '행정구조'
     },
    {'state_key': 'visualize_education_process_curriculum_week',
     'function': visualize_education_process_curriculum_week,
     'file_name': '교육주수'
     },
    {'state_key': 'visualize_education_process_curriculum_clinical_practice_week',
     'function': visualize_education_process_curriculum_clinical_practice_week,
     'file_name': '임상실습_교육주수'
     },
    {'state_key': 'visualize_education_process_educational_department',
     'function': visualize_education_process_educational_department,
     'file_name': '의학교육_전문부서'
     },
    {'state_key': 'visualize_education_process_humanity_department',
     'function': visualize_education_process_humanity_department,
     'file_name': '의학인문_전문부서'
     },
    {'state_key': 'visualize_student_admission_student',
     'function': visualize_student_admission_student,
     'file_name': '입학학생수'
     },
    {'state_key': 'visualize_student_enrolled_student',
     'function': visualize_student_enrolled_student,
     'file_name': '재적학생수'
     },
    {'state_key': 'visualize_student_admission_student_structure',
     'function': visualize_student_admission_student_structure,
     'file_name': '의예과_입학학생_구성'
     },
    {'state_key': 'visualize_student_scholarship',
     'function': visualize_student_scholarship,
     'file_name': '장학금'
     },
    {'state_key': 'visualize_student_graduate_career',
     'function': visualize_student_graduate_career,
     'file_name': '졸업생의_진로'
     },
    {'state_key': 'visualize_student_graduate_student_basic_domestic',
     'function': visualize_student_graduate_student_basic_domestic,
     'file_name': '졸업생_기초의학_내국인'
     },
    {'state_key': 'visualize_student_graduate_student_basic_foreigner',
     'function': visualize_student_graduate_student_basic_foreigner,
     'file_name': '졸업생_기초의학_외국인'
     },
    {'state_key': 'visualize_student_graduate_student_clinical_domestic',
     'function': visualize_student_graduate_student_clinical_domestic,
     'file_name': '졸업생_임상의학_내국인'
     },
    {'state_key': 'visualize_student_graduate_student_clinical_foreigner',
     'function': visualize_student_graduate_student_clinical_foreigner,
     'file_name': '졸업생_임상의학_외국인'
     },
    {'state_key': 'visualize_student_per_professor',
     'function': visualize_student_per_professor,
     'file_name': '교수_1인당_학생수'
     },
    {'state_key': 'visualize_student_international_exchange',
     'function': visualize_student_international_exchange,
     'file_name': '국제교류현황'
     },
    {'state_key': 'visualize_professor_professor_basic',
     'function': visualize_professor_professor_basic,
     'file_name': '교원수_기초의학'
     },
    {'state_key': 'visualize_professor_professor_clinical',
     'function': visualize_professor_professor_clinical,
     'file_name': '교원수_임상의학'
     },
    {'state_key': 'visualize_professor_full_time_new_basic_professor_data',
     'function': visualize_professor_full_time_new_basic_professor_data,
     'file_name': '신규임용_기초의학'
     },
    {'state_key': 'visualize_professor_full_time_retire_basic_professor_data',
     'function': visualize_professor_full_time_retire_basic_professor_data,
     'file_name': '정년퇴임_기초의학'
     },
    {'state_key': 'visualize_professor_full_time_new_clinical_professor_data',
     'function': visualize_professor_full_time_new_clinical_professor_data,
     'file_name': '신규임용_임상의학'
     },
    {'state_key': 'visualize_professor_full_time_retire_clinical_professor_data',
     'function': visualize_professor_full_time_retire_clinical_professor_data,
     'file_name': '정년퇴임_임상의학'
     },
    {'state_key': 'visualize_professor_medical_education_training',
     'function': visualize_professor_medical_education_training,
     'file_name': '의학교육_연수'
     },
    {'state_key': 'visualize_management_finance_student_tuition_medical_school',
     'function': visualize_management_finance_student_tuition_medical_school,
     'file_name': '의과대학_등록금'
     },
    {'state_key': 'visualize_management_finance_student_tuition_graduate_medicine',
     'function': visualize_management_finance_student_tuition_graduate_medicine,
     'file_name': '의학전문대학원_등록금'
     }
]

visualize_output_list = [
    Output({'type': d['state_key'], 'index': ALL}, 'n_clicks') for d in visualize_state_dict
]

visualize_input_list = [
    Input({'type': d['state_key'], 'index': ALL}, 'n_clicks') for d in visualize_state_dict
]

visualize_state_list = [
    State({'type': '_'.join(d['state_key'].split('_')[1:]), 'index': ALL}, 'data') for d in visualize_state_dict
]

import io
import json
from openpyxl import Workbook

with open('excel_dict.json', 'r') as f:
    excel_dict = json.load(f)


def extract_school(school):
    output = io.BytesIO()

    wb = Workbook()

    df_dict = {
        k: [] for k in set(excel_dict.values())
    }
    for attr_name, sheet_name in excel_dict.items():
        try:
            data = getattr(school, attr_name)
            if isinstance(data, str) and data.startswith('['):
                data = data.replace('\'', "\"").replace('\x08', '')
                data = json.loads(data)
                df_dict[sheet_name].append({'항목': attr_name, '내용': data})
            else:
                data = data.replace('\'', "\"").replace('\x08', '')
                df_dict[sheet_name].append({'항목': attr_name, '내용': data})
        except Exception as e:
            print(e)
    for idx, (sheet_name, data_list) in enumerate(df_dict.items()):
        if idx == 0:
            ws = wb.active
            ws.title = sheet_name
        else:
            ws = wb.create_sheet(title=sheet_name)
        for row in data_list:
            if isinstance(row['내용'], list):
                for i, r in enumerate(row['내용']):
                    if isinstance(r, dict):
                        flat_key = []
                        flat_data = []
                        for k, v in r.items():
                            flat_key.append(k)
                            flat_data.append(v)
                        ws.append([row['항목']])
                        ws.append(flat_key)
                        ws.append(flat_data)
                    else:
                        if i == 0:
                            ws.append([row['항목'], r])
                        else:
                            ws.append(['', r])
                pass
            else:
                try:
                    ws.append([row['항목'], row['내용']])
                except Exception as ee:
                    print(ee)

    wb.save(output)
    output.seek(0)
    return dcc.send_bytes(output.getvalue(), f"{getattr(school, '대학명')}.xlsx")
