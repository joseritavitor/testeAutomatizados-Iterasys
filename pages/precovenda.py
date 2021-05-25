from browser import Browser


class PrecoVenda(Browser):
    def get_value_sale(self):
        return self.driver.find_element_by_css_selector('.price-current').text