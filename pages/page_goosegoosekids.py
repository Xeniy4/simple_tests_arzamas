from selene import browser, have


class GoosegooseKids:

    def navigation_list_kids(self,value):
        browser.element(f'.kids-courses__filters-button[data-kind="{value}"]').click()
        # value = all, courses, podcasts, audio_materials,

    def select_course_kids(self):
        browser.element('[href="/kids/480"]').click()
        # Съедобное/несъедобное

    def select_podcast_kids(self):
        browser.element('[href="/kids/416"]').click()

    def select_audio_material_kids(self):
        browser.element('[href="/kids/474"]').click()

    def check_tutle_content_page_kids(self, value):
        browser.element('.card__title').should(have.text(value))



