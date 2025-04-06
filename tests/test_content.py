import allure

from pages.page_main import OpenPage, Courses, Search

open_page = OpenPage()
courses = Courses()
search = Search()


@allure.story('Проверка отображения карточки курса')
def test_courses_content():

    with allure.step('Открыть Главную страницу'):
        open_page.open()

    with allure.step('В меню хедера нажать на кнопку "Курсы"'):
        open_page.navigation_list('Курсы')

    with allure.step('Выбрать вид курса'):
        open_page.select_type_filter_kind_courses('Мировая история')

    with allure.step('Открыть курс "Гай Юлий Цезарь покоряет мир"'):
        open_page.select_course()

    with allure.step('Проверка отображения заголовка курса'):
        open_page.check_tytle_content_page('Гай Юлий Цезарь покоряет мир')


@allure.story('Проверка покупки курса без авторизации на сайте')
def test_buy_course_no_auth():
    with allure.step('Открыть страницу курса'):
        open_page.open_page_course('Мировая история')

    with allure.step('Нажать на кнопку "Купить"'):
        courses.click_button_pay_course()

    with allure.step('Проверка отображения окна авторизации с заголовком "Вход"'):
        courses.check_auth_page('Вход')


def test_pogcast_content():
    with allure.step('Открыть Главную страницу'):
        open_page.open()

    with allure.step('В меню хедера нажать на кнопку "Подкасты"'):
        open_page.navigation_list('Подкасты')

    with allure.step('Выбрать вид подкаста'):
        open_page.select_type_filter_kind_courses('История России')

    with allure.step('Открыть подкаст "Проверка связей"'):
        open_page.select_podcast()

    with allure.step('Проверка отображения заголовка подкаста'):
        open_page.check_tytle_content_page('Проверка связей')


def test_audio_materials():
    with allure.step('Открыть Главную страницу'):
        open_page.open()

    with allure.step('В меню хедера нажать на кнопку "Материалы"'):
        open_page.navigation_list('Материалы')

    with allure.step('Выбрать вид подкаста'):
        open_page.select_type_filter_kind_courses('Антропология')

    with allure.step('Открыть аудиоматериал "Краткая история вещей"'):
        open_page.select_audio_material()

    with allure.step('Проверка отображения заголовка аудиоматериала'):
        open_page.check_tytle_content_page('Краткая история вещей')
