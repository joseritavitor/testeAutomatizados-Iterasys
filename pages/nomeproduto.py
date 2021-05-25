from browser import Browser

class NomeProduto(Browser):
    def get_product_name(self):
        return self.driver.find_element_by_css_selector('.col-md-7 prod-info h1').text