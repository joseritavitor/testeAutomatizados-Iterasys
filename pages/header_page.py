from browser import Browser
from time import sleep

class HeaderPage(Browser):
    def preenche_imput_busca(self, texto):
        self.driver.find_element_by_css_selector('#search').send_keys(texto)
        sleep(3)

    def button_click_get(self):
        self.driver.find_element_by_css_selector('.button-search').click()
