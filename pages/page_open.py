from selene import browser, have


class OpenPage:

    def open(self):
        browser.open('/')

    def navigation_list(self, value):
        browser.element(f'//li/a[contains(text(),"{value}")]').click()
    # варианты: Курсы, Подкасты, Материалы, Журнал

    def navigation_menu(self):
        browser.element('.site-header__subnav-button').click()

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

    def select_course(self):
        browser.element('[href="/courses/181"]').click()

    def open_page_course(self, value):
        self.open()
        self.navigation_list('Курсы')
        self.select_type_filter_kind_courses(value)
        self.select_course()

    def select_podcast(self):
        browser.element('[href="/podcasts/330"]').click()

    def select_audio_material(self):
        browser.element('[href="/shorts/374"]').click()
