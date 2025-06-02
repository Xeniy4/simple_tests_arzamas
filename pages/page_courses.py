from selene import browser, have


class Courses:

    def click_button_pay_course(self):
        browser.element('.product-notice__button').click()

    def check_auth_page(self, value):
        browser.element('.az-form__title').should(have.text(value))
        # value == Вход
