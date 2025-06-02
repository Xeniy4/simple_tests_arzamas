import enum


class NavigationListValue(enum.Enum):

    courses_nav_list = 'Курсы'
    podcast_nav_list = 'Подкасты'
    audio_material_nav_list = 'Материалы'
    mag_nav_list = 'Журнал'


class ItemCourseValue(enum.Enum):
    item_course_all = 'Все'
    item_course_art = 'Искусство'
    item_course_world_history = 'Мировая история'
    item_course_russian_history = 'История России'
    item_course_literature = 'Литература'
    item_course_anthropology = 'Антропология'
    item_course_cinema = 'Кино'
    item_course_theatre = 'Театр'
    item_course_music = 'Музыка'
    item_course_architecture = 'Архитектура'
    item_course_philosophy = 'Философия'
    item_course_economic = 'Экономика'


class ItemPodcastValue(enum.Enum):
    item_podcast_all = ''