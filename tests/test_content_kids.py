import allure
from pages.page_goosegoosekids import GoosegooseKids
from pages.page_open import OpenPage

open_page = OpenPage()
kids = GoosegooseKids()


@allure.epic("Web UI тесты")
@allure.story('Проверка отображения заголовка курса')
def test_mapping_courses_kids():

    with allure.step('Открыть Главную страницу'):
        open_page.open()

    with allure.step('Нажать на кнопку в хедер меню "Гусьгусь"'):
        open_page.button_goosegoose()

    with allure.step('Открыть раздел "Курсы"'):
        kids.navigation_list_kids('courses')

    with allure.step('Открыть курс "Съедобное/несъедобное"'):
        kids.select_course_kids()

    with allure.step('Проверка отображения заголовка курса'):
        kids.check_tutle_content_page_kids('Съедобное/несъедобное')


@allure.epic("Web UI тесты")
@allure.story('Проверка отображения заголовка подкаста')
def test_mapping_podcast_kids():
    with allure.step('Открыть Главную страницу'):
        open_page.open()

    with allure.step('Нажать на кнопку в хедер меню "Гусьгусь"'):
        open_page.button_goosegoose()

    with allure.step('Открыть раздел "Подкасты"'):
        kids.navigation_list_kids('podcasts')

    with allure.step('Открыть подкаст "Это вам не сказки"'):
        kids.select_podcast_kids()

    with allure.step('Проверка отображения заголовка подкаста'):
        kids.check_tutle_content_page_kids('Это вам не сказки')


@allure.epic("Web UI тесты")
@allure.story('Проверка отображения заголовка аудиокниги')
def test_mapping_audio_kids():
    with allure.step('Открыть Главную страницу'):
        open_page.open()

    with allure.step('Нажать на кнопку в хедер меню "Гусьгусь"'):
        open_page.button_goosegoose()

    with allure.step('Открыть раздел "Аудиокниги"'):
        kids.navigation_list_kids('audio_materials')

    with allure.step('Открыть аудиокнигу "Мифы звездного неба"'):
        kids.select_audio_material_kids()

    with allure.step('Проверка отображения заголовка аудиокниги'):
        kids.check_tutle_content_page_kids('Мифы звездного неба')



