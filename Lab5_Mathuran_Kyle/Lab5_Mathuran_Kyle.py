"""
Name:
Course:
Date: July 25th, 2025
Description: Set of test cases for this link https://magento.softwaretestingboard.com/
"""

#regionImports
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#EndRegion Imports


#Region TEST SUITE
class TestDefaultSuite(object):
    def setup_method(self, method):
        """Class Setup - runs before all tests"""
        self.driver = webdriver.Edge()
        self.vars = {}

    def teardown_method(self, method):
        """Class TearDown - runs after all test"""
        self.driver.quit()

    def test_shopingSteps(self):
    # Test name: ShopingSteps
    # Step # | name | target | value
            # 1 | open | / |
            self.driver.get("https://magento.softwaretestingboard.com/")
            # 2 | setWindowSize | 1256x891 |
            self.driver.set_window_size(1256, 891)
            # 3 | mouseOver | linkText=Create an Account |
            element = self.driver.find_element(By.LINK_TEXT, "Create an Account")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            # 4 | mouseOver | id=ui-id-8 |
            element = self.driver.find_element(By.ID, "ui-id-8")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            # 5 | click | id=ui-id-9 |
            self.driver.find_element(By.ID, "ui-id-9").click()
            # 6 | click | css=#ui-id-12 > span |
            self.driver.find_element(By.CSS_SELECTOR, "#ui-id-12 > span").click()
            # 7 | click | css=.filter-options-item:nth-child(1) > .filter-options-title |
            self.driver.find_element(By.CSS_SELECTOR,
                                     ".filter-options-item:nth-child(1) > .filter-options-title").click()
            # 8 | click | css=.allow .item:nth-child(1) > a |
            self.driver.find_element(By.CSS_SELECTOR, ".allow .item:nth-child(1) > a").click()
            # 9 | mouseOver | linkText=Tops |
            element = self.driver.find_element(By.LINK_TEXT, "Tops")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            # 10 | mouseOut | linkText=Tops |
            element = self.driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(element, 0, 0).perform()
            # 11 | click | css=.item:nth-child(1) .actions-primary span |
            self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) .actions-primary span").click()
            # 12 | mouseOver | id=ui-id-9 |
            element = self.driver.find_element(By.ID, "ui-id-9")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            # 13 | mouseOut | id=ui-id-9 |
            element = self.driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(element, 0, 0).perform()
            # 14 | mouseOver | css=.fotorama__img |
            element = self.driver.find_element(By.CSS_SELECTOR, ".fotorama__img")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            # 15 | mouseOut | css=.fotorama__active > .fotorama__img |
            element = self.driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(element, 0, 0).perform()
            # 16 | click | css=#product-addtocart-button > span |
            self.driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button > span").click()
            # 17 | click | id=option-label-size-143-item-168 |
            self.driver.find_element(By.ID, "option-label-size-143-item-168").click()
            # 18 | click | id=option-label-color-93-item-53 |
            self.driver.find_element(By.ID, "option-label-color-93-item-53").click()
            # 19 | mouseOver | id=product-addtocart-button |
            element = self.driver.find_element(By.ID, "product-addtocart-button")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            # 20 | mouseOut | id=product-addtocart-button |
            element = self.driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(element, 0, 0).perform()
            # 21 | mouseOver | css=#product-addtocart-button > span |
            element = self.driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button > span")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            # 22 | click | css=#product-addtocart-button > span |
            self.driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button > span").click()
            # 23 | mouseOut | css=#product-addtocart-button > span |
            element = self.driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(element, 0, 0).perform()
            # 24 | runScript | window.scrollTo(0,48) |
            self.driver.execute_script("window.scrollTo(0,48)")
            # 25 | click | linkText=Hoodies & Sweatshirts |
            self.driver.find_element(By.LINK_TEXT, "Hoodies & Sweatshirts").click()
            # 26 | click | css=.filter-options-item:nth-child(1) > .filter-options-title |
            self.driver.find_element(By.CSS_SELECTOR,
                                     ".filter-options-item:nth-child(1) > .filter-options-title").click()
            # 27 | click | css=.allow .item:nth-child(2) > a |
            self.driver.find_element(By.CSS_SELECTOR, ".allow .item:nth-child(2) > a").click()
            # 28 | runScript | window.scrollTo(0,248) |
            self.driver.execute_script("window.scrollTo(0,248)")
            # 29 | click | css=.item:nth-child(1) > .product-item-info .product-image-photo |
            self.driver.find_element(By.CSS_SELECTOR,
                                     ".item:nth-child(1) > .product-item-info .product-image-photo").click()
            # 30 | mouseOver | linkText=Men |
            element = self.driver.find_element(By.LINK_TEXT, "Men")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            # 31 | mouseOut | id=ui-id-5 |
            element = self.driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(element, 0, 0).perform()
            # 32 | mouseOver | id=ui-id-4 |
            element = self.driver.find_element(By.ID, "ui-id-4")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            # 33 | mouseOut | id=ui-id-4 |
            element = self.driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(element, 0, 0).perform()
            # 34 | mouseOver | id=ui-id-5 |
            element = self.driver.find_element(By.ID, "ui-id-5")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            # 35 | mouseOver | css=#ui-id-18 > span:nth-child(2) |
            element = self.driver.find_element(By.CSS_SELECTOR, "#ui-id-18 > span:nth-child(2)")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            # 36 | mouseOut | css=#ui-id-18 > span:nth-child(2) |
            element = self.driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(element, 0, 0).perform()
            # 37 | click | id=option-label-size-143-item-168 |
            self.driver.find_element(By.ID, "option-label-size-143-item-168").click()
            # 38 | click | css=#product-addtocart-button > span |
            self.driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button > span").click()
            # 39 | mouseOver | css=#product-addtocart-button > span |
            element = self.driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button > span")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            # 40 | mouseOut | css=#product-addtocart-button > span |
            element = self.driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(element, 0, 0).perform()
            # 41 | click | id=option-label-color-93-item-52 |
            self.driver.find_element(By.ID, "option-label-color-93-item-52").click()
            # 42 | click | id=product-addtocart-button |
            self.driver.find_element(By.ID, "product-addtocart-button").click()
            # 43 | mouseOver | id=product-addtocart-button |
            element = self.driver.find_element(By.ID, "product-addtocart-button")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            # 44 | mouseOut | id=product-addtocart-button |
            element = self.driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(element, 0, 0).perform()
            # 45 | click | linkText=Hoodies & Sweatshirts |
            self.driver.find_element(By.LINK_TEXT, "Hoodies & Sweatshirts").click()
            # 46 | click | css=.filter-options-item:nth-child(1) > .filter-options-title |
            self.driver.find_element(By.CSS_SELECTOR,
                                     ".filter-options-item:nth-child(1) > .filter-options-title").click()
            # 47 | click | css=.allow .item:nth-child(3) > a |
            self.driver.find_element(By.CSS_SELECTOR, ".allow .item:nth-child(3) > a").click()
            # 48 | runScript | window.scrollTo(0,275) |
            self.driver.execute_script("window.scrollTo(0,275)")
            # 49 | click | linkText=Tops |
            self.driver.find_element(By.LINK_TEXT, "Tops").click()
            # 50 | runScript | window.scrollTo(0,9) |
            self.driver.execute_script("window.scrollTo(0,9)")
            # 51 | click | css=.filter-options-item:nth-child(1) > .filter-options-title |
            self.driver.find_element(By.CSS_SELECTOR,
                                     ".filter-options-item:nth-child(1) > .filter-options-title").click()
            # 52 | click | css=.allow .item:nth-child(2) > a |
            self.driver.find_element(By.CSS_SELECTOR, ".allow .item:nth-child(2) > a").click()
            # 53 | runScript | window.scrollTo(0,51) |
            self.driver.execute_script("window.scrollTo(0,51)")
            # 54 | click | css=.filter-options-item:nth-child(1) > .filter-options-title |
            self.driver.find_element(By.CSS_SELECTOR,
                                     ".filter-options-item:nth-child(1) > .filter-options-title").click()
            # 55 | click | css=.allow .item:nth-child(4) > a |
            self.driver.find_element(By.CSS_SELECTOR, ".allow .item:nth-child(4) > a").click()
            # 56 | runScript | window.scrollTo(0,3) |
            self.driver.execute_script("window.scrollTo(0,3)")
            # 57 | click | css=.item:nth-child(3) .product-image-photo |
            self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(3) .product-image-photo").click()
            # 58 | mouseOver | linkText=Be the first to review this product |
            element = self.driver.find_element(By.LINK_TEXT, "Be the first to review this product")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            # 59 | mouseOut | linkText=Be the first to review this product |
            element = self.driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(element, 0, 0).perform()
            # 60 | runScript | window.scrollTo(0,5) |
            self.driver.execute_script("window.scrollTo(0,5)")
            # 61 | click | id=option-label-size-143-item-168 |
            self.driver.find_element(By.ID, "option-label-size-143-item-168").click()
            # 62 | click | id=option-label-color-93-item-57 |
            self.driver.find_element(By.ID, "option-label-color-93-item-57").click()
            # 63 | click | css=#product-addtocart-button > span |
            self.driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button > span").click()
            # 64 | mouseOver | css=#product-addtocart-button > span |
            element = self.driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button > span")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            # 65 | mouseOut | css=#product-addtocart-button > span |
            element = self.driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(element, 0, 0).perform()
            # 66 | runScript | window.scrollTo(0,381.5666809082031) |
            self.driver.execute_script("window.scrollTo(0,381.5666809082031)")



#EndRegion TEST SUITE