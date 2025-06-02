import allure
from pages.page_goosegoosekids import GoosegooseKids
from pages.page_open import OpenPage

open_page = OpenPage()
kigs = GoosegooseKids()


@allure.epic("Web UI тесты")
@allure.story('Проверка отображения заголовка курса')
def test_courses_kids():

    with allure.step('Открыть Главную страницу'):
        open_page.open()

    with allure.step('Нажать на кнопку в хедер меню "Гусьгусь"'):
        open_page.button_goosegoose()

    with allure.step('Открыть раздел "Курсы"'):
        kigs.navigation_list_kids('courses')

    with allure.step('Открыть курс "Съедобное/несъедобное"'):
        kigs.select_course_kids()

    with allure.step('Проверка отображения заголовка курса'):
        kigs.check_tutle_content_page_kids('Съедобное/несъедобное')


@allure.epic("Web UI тесты")
@allure.story('Проверка отображения заголовка подкаста')
def test_podcast_kids():
    with allure.step('Открыть Главную страницу'):
        open_page.open()

    with allure.step('Нажать на кнопку в хедер меню "Гусьгусь"'):
        open_page.button_goosegoose()

    with allure.step('Открыть раздел "Подкасты"'):
        kigs.navigation_list_kids('podcasts')

    with allure.step('Открыть подкаст "Это вам не сказки"'):
        kigs.select_podcast_kids()

    with allure.step('Проверка отображения заголовка подкаста'):
        kigs.check_tutle_content_page_kids('Это вам не сказки')


@allure.epic("Web UI тесты")
@allure.story('Проверка отображения заголовка аудиокниги')
def test_audio_kids():
    with allure.step('Открыть Главную страницу'):
        open_page.open()

    with allure.step('Нажать на кнопку в хедер меню "Гусьгусь"'):
        open_page.button_goosegoose()

    with allure.step('Открыть раздел "Аудиокниги"'):
        kigs.navigation_list_kids('audio_materials')

    with allure.step('Открыть аудиокнигу "Мифы звездного неба"'):
        kigs.select_audio_material_kids()

    with allure.step('Проверка отображения заголовка аудиокниги'):
        kigs.check_tutle_content_page_kids('Мифы звездного неба')



