from selene import browser, have




class Open_page_header:

    def navigation_list(self, value):
        browser.element(f'//li/a[contains(text(),"{value}")]').click()
    # варианты: Курсы, Подкасты, Материалы, Журнал

    def navigation_menu(self):
        browser.element('.site-header__subnav-button ').click()

    def navigation_menu_point(self, value):
        browser.element(f'//nav//span[contains(text(),"{value}")]').click()
    # варианты value: Автор среди нас, Еврейский музей, Новая Третьяковка, Онлайн-университет, Запад и Восток: история культур
    # Видеоистория русской культуры, Русский язык от «гой еси» до «лол кек», Что такое античность, Русское искусство XX века
    # Русская литература XX века, Детская комната

    def button_arzoom(self):
        browser.element('.site-header__arzroom-link').click()

    def button_goosegoose(self):
        browser.element('.site-header__goosegoose-link').click()

    def button_download_app(self):
        browser.element('.site-header__arzamas-app-link').click()

    def button_gift_certificate(self):
        browser.element('.site-header__get-gift-certificate').click()

    def button_login(self):
        browser.element('.site-header__login-button').click()

    def button_search(self):
        browser.element('.site-header__search-button').click()

    def select_type_filter_kind_courses(self, value):
        browser.element(f'//main/div/div/div/button[contains(text(),"{value}")]').click()
    # варианты value: Все, Искусство, Мировая история, История России, Литература, Антропология, Кино, Театр,
    # Музыка, Архитектура, Философия, Экономика

    def check_tytle_content_page(self, value):
        browser.element('.course-title').should(have.text(value))



class Courses:

    def select_course(self):
        browser.element('[href="/courses/181"]').click()
    # Тут узнать как можно найти локатор подругому, чтобы не через href, а по названию курса.
    # Там <h2 class="card__title">Гай Юлий Цезарь покоряет мир</h2>. Как бы объединить классы и contains(text()

    def click_button_pay(self):
        browser.element('.product-notice__button').click()

    def check_auth_page(self, value):
        browser.element('.az-form__title').should(have.text(value))
        # value == Войти


class Podcast:
# в тестах перед тем как перейти на подкаст выбрать другую тематику в def select_type_filter_kind_courses
    def select_podcast(self):
        browser.element('[href="/podcasts/330"]').click()
    # История россии

    # check_tytle_content_page Проверка связей


class Audio_materials:

    def select_audio_material(self):
        browser.element('[href="/shorts/374"]').click()
        #антропология

        # check_tytle_content_page Краткая история вещей


class Special:
    def select_special(self):
        browser.element('[href="/shorts/364"]').click()
        #кино

        # check_tytle_content_page Рождественские фильмы

# т.к переход на страницу контента по ссылке href, можно сделать так:
# class ContentPage:
#
#     def click_content_page(self, value):
#         browser.element(f'[href="{value}"]').click()
#         # value = /shorts/364
#     # Взято из класса Open_page_header последний метод
#     def check_tytle_content_page(self, value):
#         browser.element('.course-title').should(have.text(value))

# И удалить все классы, которые над этим вариантом, т.к они повторяются


class Search:

    def type_search_text(self, value):
        browser.element('.site-header__search-input').type(value).press_enter()
        # value = Загадки Гоголя
    def check(self, value):
        browser.element('[href="/courses/180"]').should(have.no.text(value))
        # value = Загадки Гоголя


class GoosegooseKids:
    pass