import allure
from pages.page_search import Search
from pages.page_courses import Courses
from pages.page_open import OpenPage

open_page = OpenPage()
courses = Courses()
search = Search()


@allure.epic("Web UI тесты")
@allure.story('Проверка отображения карточки курса1')
def test_mapping_courses_content():

    with allure.step('Открыть Главную страницу'):
        open_page.open()

    with allure.step('В меню хедера нажать на кнопку "Курсы"'):
        open_page.navigation_list('Курсы')

    with allure.step('Выбрать вид курса'):
        open_page.select_type_filter_kind_courses('Мировая история')

    with allure.step('Открыть курс "Гай Юлий Цезарь покоряет мир"'):
        open_page.select_course()

    with allure.step('Проверка отображения заголовка курса'):
        open_page.check_title_content_page('Гай Юлий Цезарь покоряет мир')


@allure.epic("Web UI тесты")
@allure.story('Проверка покупки курса без авторизации на сайте')
def test_buy_course_no_auth():
    with allure.step('Открыть страницу курса'):
        open_page.open_page_course('Мировая история')

    with allure.step('Нажать на кнопку "Купить"'):
        courses.click_button_pay_course()

    with allure.step('Проверка отображения окна авторизации с заголовком "Вход"'):
        courses.check_auth_page('Вход')


@allure.epic("Web UI тесты")
@allure.story('Проверка отображения заголовка подкаста')
def test_mapping_pogcast_content():
    with allure.step('Открыть Главную страницу'):
        open_page.open()

    with allure.step('В меню хедера нажать на кнопку "Подкасты"'):
        open_page.navigation_list('Подкасты')

    with allure.step('Выбрать вид подкаста'):
        open_page.select_type_filter_kind_courses('История России')

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
        open_page.navigation_list('Материалы')

    with allure.step('Выбрать вид подкаста'):
        open_page.select_type_filter_kind_courses('Антропология')

    with allure.step('Открыть аудиоматериал "Краткая история вещей"'):
        open_page.select_audio_material()

    with allure.step('Проверка отображения заголовка аудиоматериала'):
        open_page.check_title_content_page('Краткая история вещей')
