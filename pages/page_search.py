from selene import browser, have


class Search:

    def type_search_text(self, value):
        browser.element('.site-header__search-input').type(value).press_enter()
        # value = Загадки Гоголя
    def check(self, value):
        browser.element('[href="/courses/180"]').should(have.no.text(value))
        # value = Загадки Гоголя
