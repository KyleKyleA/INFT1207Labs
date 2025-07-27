"""
Name:
Course:
Date: July 25th, 2025
Description: Set of test cases for this link https://magento.softwaretestingboard.com/
"""

# regionImports
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
# EndRegion Imports


# Region TEST SUITE
class TestDefaultSuite(object):
    def setup_method(self, method):
        """Class Setup - runs before all tests"""
        self.driver = webdriver.Edge()
        self.vars = {}

    def teardown_method(self, method):
        """Class TearDown - runs after all test"""
        self.driver.quit()


def test_femaleShoppingSteps13(self):
    # Test name: FemaleShoppingSteps1-3
    # Step # | name | target | value | comment
    # 1 | open | https://magento.softwaretestingboard.com/ |  |
    self.driver.get("https://magento.softwaretestingboard.com/")
    # 2 | setWindowSize | 974x1080 |  |
    self.driver.set_window_size(974, 1080)
    # 3 | mouseOver | id=ui-id-5 |  |
    element = self.driver.find_element(By.ID, "ui-id-5")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 4 | mouseOut | id=ui-id-5 |  |
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 5 | mouseOver | css=#ui-id-4 > span:nth-child(2) |  |
    element = self.driver.find_element(By.CSS_SELECTOR, "#ui-id-4 > span:nth-child(2)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 6 | click | css=#ui-id-4 > span:nth-child(2) |  |
    self.driver.find_element(By.CSS_SELECTOR, "#ui-id-4 > span:nth-child(2)").click()
    # 7 | mouseOut | css=#ui-id-4 > span:nth-child(2) |  |
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 8 | selectFrame | index=8 |  |
    self.driver.switch_to.frame(8)
    # 9 | selectFrame | index=0 |  |
    self.driver.switch_to.frame(0)
    # 10 | selectFrame | relative=parent |  |
    self.driver.switch_to.default_content()
    # 11 | selectFrame | relative=parent |  |
    self.driver.switch_to.default_content()
    # 12 | mouseOver | css=.womens-main > img |  |
    element = self.driver.find_element(By.CSS_SELECTOR, ".womens-main > img")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 13 | mouseOut | css=.womens-main > img |  |
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 14 | mouseOver | id=ui-id-4 |  |
    element = self.driver.find_element(By.ID, "ui-id-4")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 15 | runScript | window.scrollTo(0,120) |  |
    self.driver.execute_script("window.scrollTo(0,120)")
    # 16 | click | css=#ui-id-12 > span |  |
    self.driver.find_element(By.CSS_SELECTOR, "#ui-id-12 > span").click()
    # 17 | click | css=.filter-options-item:nth-child(1) > .filter-options-title |  |
    self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(1) > .filter-options-title").click()
    # 18 | click | css=.allow .item:nth-child(1) > a |  |
    self.driver.find_element(By.CSS_SELECTOR, ".allow .item:nth-child(1) > a").click()
    # 19 | mouseOver | css=.item:nth-child(2) > .product-item-info .product-image-photo |  |
    element = self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(2) > .product-item-info .product-image-photo")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 20 | runScript | window.scrollTo(0,24) |  |
    self.driver.execute_script("window.scrollTo(0,24)")
    # 21 | mouseOut | css=.item:nth-child(2) .product-image-photo |  |
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 22 | click | css=.item:nth-child(1) .product-image-photo |  |
    self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) .product-image-photo").click()
    # 23 | runScript | window.scrollTo(0,49) |  |
    self.driver.execute_script("window.scrollTo(0,49)")
    # 24 | click | id=option-label-size-143-item-168 |  |
    self.driver.find_element(By.ID, "option-label-size-143-item-168").click()
    # 25 | click | id=option-label-color-93-item-53 |  |
    self.driver.find_element(By.ID, "option-label-color-93-item-53").click()
    # 26 | runScript | window.scrollTo(0,169) |  |
    self.driver.execute_script("window.scrollTo(0,169)")
    # 27 | click | css=#product-addtocart-button > span |  |
    self.driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button > span").click()
    # 28 | mouseOver | css=#product-addtocart-button > span |  |
    element = self.driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 29 | mouseOut | css=#product-addtocart-button > span |  |
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 30 | mouseOver | linkText=Hoodies & Sweatshirts |  |
    element = self.driver.find_element(By.LINK_TEXT, "Hoodies & Sweatshirts")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 31 | click | linkText=Hoodies & Sweatshirts |  |
    self.driver.find_element(By.LINK_TEXT, "Hoodies & Sweatshirts").click()
    # 32 | click | css=.filter-options-item:nth-child(1) > .filter-options-title |  |
    self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(1) > .filter-options-title").click()
    # 33 | click | css=.allow .item:nth-child(2) > a |  |
    self.driver.find_element(By.CSS_SELECTOR, ".allow .item:nth-child(2) > a").click()
    # 34 | runScript | window.scrollTo(0,74) |  |
    self.driver.execute_script("window.scrollTo(0,74)")
    # 35 | click | css=.item:nth-child(1) > .product-item-info .product-image-photo |  |
    self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) > .product-item-info .product-image-photo").click()
    # 36 | runScript | window.scrollTo(0,85) |  |
    self.driver.execute_script("window.scrollTo(0,85)")
    # 37 | click | id=option-label-size-143-item-168 |  |
    self.driver.find_element(By.ID, "option-label-size-143-item-168").click()
    # 38 | click | id=option-label-color-93-item-53 |  |
    self.driver.find_element(By.ID, "option-label-color-93-item-53").click()
    # 39 | click | css=#product-addtocart-button > span |  |
    self.driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button > span").click()
    # 40 | mouseOver | css=.magnify-wheel-loaded > .fotorama__img |  |
    element = self.driver.find_element(By.CSS_SELECTOR, ".magnify-wheel-loaded > .fotorama__img")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 41 | mouseOut | css=.magnify-wheel-loaded > .fotorama__img |  |
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 42 | click | linkText=Hoodies & Sweatshirts |  |
    self.driver.find_element(By.LINK_TEXT, "Hoodies & Sweatshirts").click()
    # 43 | mouseOver | css=#ui-id-28 > span |  |
    element = self.driver.find_element(By.CSS_SELECTOR, "#ui-id-28 > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 44 | mouseOut | css=#ui-id-28 > span |  |
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 45 | click | css=.filter-options-item:nth-child(1) > .filter-options-title |  |
    self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(1) > .filter-options-title").click()
    # 46 | click | css=.allow .item:nth-child(3) > a |  |
    self.driver.find_element(By.CSS_SELECTOR, ".allow .item:nth-child(3) > a").click()
    # 47 | mouseOver | css=.item:nth-child(3) .product-image-photo |  |
    element = self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(3) .product-image-photo")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 48 | click | css=.item:nth-child(3) .product-image-photo |  |
    self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(3) .product-image-photo").click()
    # 49 | click | id=option-label-size-143-item-168 |  |
    self.driver.find_element(By.ID, "option-label-size-143-item-168").click()
    # 50 | click | id=option-label-color-93-item-56 |  |
    self.driver.find_element(By.ID, "option-label-color-93-item-56").click()
    # 51 | click | css=#product-addtocart-button > span |  |
    self.driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button > span").click()
    # 52 | mouseOver | linkText=Hoodies & Sweatshirts |  |
    element = self.driver.find_element(By.LINK_TEXT, "Hoodies & Sweatshirts")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 53 | click | linkText=Hoodies & Sweatshirts |  |
    self.driver.find_element(By.LINK_TEXT, "Hoodies & Sweatshirts").click()
    # 54 | mouseOver | id=mode-list |  |
    element = self.driver.find_element(By.ID, "mode-list")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 55 | click | css=.filter-options-item:nth-child(1) |  |
    self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(1)").click()
    # 56 | click | css=.filter-options-item:nth-child(1) > .filter-options-title |  |
    self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(1) > .filter-options-title").click()
    # 57 | click | css=.allow .item:nth-child(4) > a |  |
    self.driver.find_element(By.CSS_SELECTOR, ".allow .item:nth-child(4) > a").click()
    # 58 | mouseOver | css=.item:nth-child(2) .product-image-photo |  |
    element = self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(2) .product-image-photo")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 59 | mouseOut | css=.item:nth-child(2) > .product-item-info .product-image-photo |  |
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 60 | runScript | window.scrollTo(0,372) |  |
    self.driver.execute_script("window.scrollTo(0,372)")
    # 61 | click | css=.item:nth-child(6) .product-image-photo |  |
    self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(6) .product-image-photo").click()
    # 62 | mouseOver | css=.view > span:nth-child(2) |  |
    element = self.driver.find_element(By.CSS_SELECTOR, ".view > span:nth-child(2)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 63 | click | id=option-label-size-143-item-168 |  |
    self.driver.find_element(By.ID, "option-label-size-143-item-168").click()
    # 64 | click | id=option-label-color-93-item-57 |  |
    self.driver.find_element(By.ID, "option-label-color-93-item-57").click()
    # 65 | click | css=#product-addtocart-button > span |  |
    self.driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button > span").click()

# EndRegion TEST SUITE
