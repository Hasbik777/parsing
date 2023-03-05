from config.utils import RequestTranslator


class Paginations(RequestTranslator):
    def find_button_next(self) -> bool:
        pagination = self._get_soup().find('div', class_='pagination')
        return 'Next' in pagination.text