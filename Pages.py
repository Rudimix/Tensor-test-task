from BaseApp import BasePage
from selenium.webdriver.common.by import By

class TensorSearchLocators:
    LOCATOR_CONTACTS = (By.XPATH, '//a[text()="Контакты"]')
    LOCATOR_TENSOR_ICON = (By.XPATH, '//a[@href="https://tensor.ru/"]/img[1]')
    LOCATOR_STRENGTH_IN_PEOPLE_BANNER = (By.XPATH, '//div/p[contains(text(), "Сила в людях")]')
    LOCATOR_ABOUT = (By.XPATH, '//a[contains(@href,"/about")]')
    LOCATOR_BLOCK_WORKING = (By.XPATH, '//div[contains(@class, "tensor_ru-About__block3")]')
    LOCATOR_IMAGES=(By.CLASS_NAME, 'tensor_ru-About__block3-image-wrapper')

class SearchHelper(BasePage):

    """ def enter_word(self, word):
        search_field = self.find_element(TensorSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field """

    def find_block_working(self):
        return self.find_element(TensorSearchLocators.LOCATOR_BLOCK_WORKING)

    def find_block_strength_in_people(self):
        return self.find_element(TensorSearchLocators.LOCATOR_STRENGTH_IN_PEOPLE_BANNER)
    
    def click_contacts(self):
        return self.find_element(TensorSearchLocators.LOCATOR_CONTACTS).click()
    
    def click_about(self):
        block=self.find_block_strength_in_people()
        return block.find_element(TensorSearchLocators.LOCATOR_ABOUT).click()
    
    def switch_to_second_page(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])
    
    def click_tensor_icon(self):
        return self.find_element(TensorSearchLocators.LOCATOR_TENSOR_ICON).click()

    def check_photos(self):
        blockWorking = self.find_element(TensorSearchLocators.LOCATOR_BLOCK_WORKING)
        images = blockWorking.find_elements(TensorSearchLocators.LOCATOR_IMAGES)
        sizes=[[],[]]
        for image in images:
            size= [image.size['width'], image.size['height']]
            sizes[0].append(size[0])
            sizes[1].append(size[1])
        if len(set(sizes[0]))==1 and len(set(sizes[1]))==1:
            return True
        else:
            return False