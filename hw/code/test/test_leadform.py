import datetime
import time
from test.base import BaseCase
from ui.pages.leadfom import LeadformPage

TEXT_WITH_SHIFTS = "Вау\n\n\nТут два переноса"
NAME = "Лид-форма "
COMPANY_NAME = "Галерея"
TITLE = "Мастер-класс"
DESCRIP = "Акварель, пастель, масло"
UR_FACE = "ООО Галерея"
UR_ADDRESS = "ул.Тверская"
QUESTION = "Какой вид графики выберите?"
ANSWER1 = "Пастель"
ANSWER2 = "Карандаш"
MIN_FIELD= "Минимальное количество полей: 1"
PHONE_ALERT = "Телефон должен начинаться с + и содержать только цифры"
EMPTY_STR = " "
REQUIRED_FIELD = "Обязательное поле"
PHONE = "+79999999999"
CODE = "code10"

class TestAudience(BaseCase):

    # ok
    def test_decoration_required_fields(self, leadform_page: LeadformPage):
        leadform_page.click_create_button()
        elements = leadform_page.empty_required_fields()
        assert len(elements) == 5

    # ok
    def test_too_long_description(self, leadform_page: LeadformPage):
        leadform_page.click_create_button()
        leadform_page.enter_long_description_field(TEXT_WITH_SHIFTS)
        leadform_page.click_continue()
        assert leadform_page.find_text("Используйте перенос строки не больше 2 раз подряд")

    #ok
    def test_sale_limit(self, leadform_page: LeadformPage):
        leadform_page.click_create_button()
        leadform_page.select_lid_magnit()
        leadform_page.enter_sale_percent()
        leadform_page.click_continue()
        assert leadform_page.find_text("Укажите скидку не больше 100%")

    # ok
    def test_question_and_answer(self, leadform_page: LeadformPage):
        leadform_page.click_create_button()
        #оформление
        leadform_page.upload_logo()
        time.sleep(1)
        leadform_page.fill_company_name(COMPANY_NAME)
        leadform_page.fill_title(TITLE)
        leadform_page.fill_description(DESCRIP)
        leadform_page.click_continue()
        #вопросы
        leadform_page.add_question(QUESTION)
        leadform_page.add_answers(ANSWER1, ANSWER2)
        assert leadform_page.find_in_form(QUESTION) is not False
        assert leadform_page.find_in_form(ANSWER1) is not False
        assert leadform_page.find_in_form(ANSWER2) is not False

    # ok
    def test_title_in_result(self, leadform_page: LeadformPage):
        leadform_page.click_create_button()
        #оформление
        leadform_page.upload_logo()
        time.sleep(1)
        leadform_page.fill_company_name(COMPANY_NAME)
        leadform_page.fill_title(TITLE)
        leadform_page.fill_description(DESCRIP)
        leadform_page.click_continue()
        leadform_page.click_continue()
        #результат
        leadform_page.fill_title_result(EMPTY_STR)
        leadform_page.click_continue()
        assert leadform_page.find_text(REQUIRED_FIELD) is not False

    #ok
    def test_phone(self, leadform_page: LeadformPage):
        leadform_page.click_create_button()
        #оформление
        leadform_page.upload_logo()
        time.sleep(1)
        leadform_page.fill_company_name(COMPANY_NAME)
        leadform_page.fill_title(TITLE)
        leadform_page.fill_description(DESCRIP)
        leadform_page.click_continue()
        leadform_page.click_continue()
        #результат
        leadform_page.add_phone(EMPTY_STR)
        leadform_page.click_continue()
        assert leadform_page.find_text(PHONE_ALERT) is not False

    #ok
    def test_add_phone_code(self, leadform_page: LeadformPage):
        leadform_page.click_create_button()
        #оформление
        leadform_page.upload_logo()
        time.sleep(1)
        leadform_page.fill_company_name(COMPANY_NAME)
        leadform_page.fill_title(TITLE)
        leadform_page.fill_description(DESCRIP)
        leadform_page.click_continue()
        leadform_page.click_continue()
        #результат
        leadform_page.add_phone(PHONE)
        leadform_page.add_code(CODE)
        assert leadform_page.find_in_form(PHONE) is not False
        assert leadform_page.find_code_in_form(CODE) is not False

    # ok
    def test_emprty_ur_fields(self, leadform_page: LeadformPage):
        leadform_page.click_create_button()
        #оформление
        leadform_page.upload_logo()
        time.sleep(1)
        leadform_page.fill_company_name(COMPANY_NAME)
        leadform_page.fill_title(TITLE)
        leadform_page.fill_description(DESCRIP)
        leadform_page.click_continue()
        leadform_page.click_continue()
        leadform_page.click_continue()
        #настройки
        leadform_page.fill_ur_face(EMPTY_STR)
        leadform_page.fill_ur_address(EMPTY_STR)
        leadform_page.click_continue()
        elements = leadform_page.find_empty_required_fields()
        assert len(elements) == 2

    # ok
    def test_create_lead(self, leadform_page: LeadformPage):
        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        name = NAME + formatted_date
        leadform_page.click_create_button()
        #оформление
        leadform_page.upload_logo()
        time.sleep(1)
        leadform_page.fill_company_name(COMPANY_NAME)
        leadform_page.fill_title(TITLE)
        leadform_page.fill_description(DESCRIP)
        leadform_page.click_continue()
        #пропускаем Вопросы, так как они необязательны
        leadform_page.click_continue()
        #пропускаем Результат, так как обязательное поле по умолчанию заполнено
        leadform_page.click_continue()
        #настройки
        leadform_page.fill_ur_face(UR_FACE)
        leadform_page.fill_ur_address(UR_ADDRESS)
        leadform_page.click_continue()
        form = leadform_page.find_form(name)
        assert form.text == name

