import allure
from pages.page_search import Search
from pages.page_courses import Courses
from pages.page_open import OpenPage
from pages.page_value_items import NavigationListValue, ItemCourseValue

open_page = OpenPage()
courses = Courses()
search = Search()
nav_list_value = NavigationListValue
item_course_value =  ItemCourseValue


@allure.epic("Web UI тесты")
@allure.story('Проверка отображения карточки курса.')
def test_mapping_courses_content():

    with allure.step('Открыть Главную страницу'):
        open_page.open()

    with allure.step('В меню хедера нажать на кнопку "Курсы"'):
        open_page.select_navigation_list(nav_list_value.courses_nav_list.value)

    with allure.step('Выбрать вид курса'):
        open_page.select_type_filter_kind_courses(item_course_value.item_course_world_history.value)

    with allure.step('Открыть курс "Гай Юлий Цезарь покоряет мир"'):
        open_page.select_course()

    with allure.step('Проверка отображения заголовка курса'):
        open_page.check_title_content_page('Гай Юлий Цезарь покоряет мир')


@allure.epic("Web UI тесты")
@allure.story('Проверка покупки курса без авторизации на сайте')
def test_buy_course_no_auth():
    with allure.step('Открыть страницу курса'):
        open_page.open_page_course(item_course_value.item_course_world_history.value)

    with allure.step('Нажать на кнопку "Купить"'):
        courses.click_button_pay_course()

    with allure.step('Проверка отображения окна авторизации с заголовком "Вход"'):
        courses.check_auth_page('Вход')


@allure.epic("Web UI тесты")
@allure.story('Проверка отображения заголовка подкаста')
def test_mapping_podcast_content():
    with allure.step('Открыть Главную страницу'):
        open_page.open()

    with allure.step('В меню хедера нажать на кнопку "Подкасты"'):
        open_page.select_navigation_list(nav_list_value.podcast_nav_list.value)

    with allure.step('Выбрать вид подкаста'):
        open_page.select_type_filter_kind_courses(item_course_value.item_course_russian_history.value)

    with allure.step('Открыть подкаст "Проверка связей"'):
        open_page.select_podcast()

    with allure.step('Проверка отображения заголовка подкаста'):
        open_page.check_title_content_page('Проверка связей')


@allure.epic("Web UI тесты")
@allure.story('Проверка отображения заголовка аудиоматериала')
def test_mapping_audio_materials():
    with allure.step('Открыть Главную страницу'):
        open_page.open()

    with allure.step('В меню хедера нажать на кнопку "Материалы"'):
        open_page.select_navigation_list(nav_list_value.audio_material_nav_list.value)

    with allure.step('Выбрать вид подкаста'):
        open_page.select_type_filter_kind_courses(item_course_value.item_course_anthropology.value)

    with allure.step('Открыть аудиоматериал "Краткая история вещей"'):
        open_page.select_audio_material()

    with allure.step('Проверка отображения заголовка аудиоматериала'):
        open_page.check_title_content_page('Краткая история вещей')
