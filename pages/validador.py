from browser import Browser

class Validador(Browser):
    def get_text_provider(self):
        return self.driver.find_element_by_css_selector('.blue').text
