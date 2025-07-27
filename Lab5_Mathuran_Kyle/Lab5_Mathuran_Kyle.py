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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#EndRegion imports


class TestFinalRecording(object):
    def setup_method(self):
        self.driver = webdriver.Edge()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_finalRecording(self):
        self.driver.get("https://magento.softwaretestingboard.com/")
        self.driver.set_window_size(974, 1080)
        element = self.driver.find_element(By.LINK_TEXT, "Women")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "#ui-id-4 > span:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#ui-id-4 > span:nth-child(2)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.ID, "ui-id-4")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.ID, "ui-id-4")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#ui-id-12 > span").click()
        element = self.driver.find_element(By.ID, "mode-list")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(1) > .filter-options-title").click()
        self.driver.execute_script("window.scrollTo(0,120)")
        self.driver.find_element(By.CSS_SELECTOR, ".allow .item:nth-child(1) > a").click()
        self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(1) > .filter-options-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swatch-option-link-layered:nth-child(3) > .text").click()
        self.driver.execute_script("window.scrollTo(0,85)")
        self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(2) > .filter-options-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swatch-option-link-layered:nth-child(3) > .swatch-option").click()
        self.driver.execute_script("window.scrollTo(0,84)")
        self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(4) > .filter-options-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".active .item:nth-child(2) > a").click()
        self.driver.find_element(By.CSS_SELECTOR, ".product > .product-image-container .product-image-photo").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(8)
        self.driver.switch_to.frame(0)
        self.driver.execute_script("window.scrollTo(0,64)")
        assert (self.vars["css=#product-addtocart-button > span"] == "hoodie")
        self.driver.switch_to.default_content()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.LINK_TEXT, "Hoodies & Sweatshirts").click()
        self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(1) > .filter-options-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".allow .item:nth-child(2) > a").click()
        self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(1) > .filter-options-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swatch-option-link-layered:nth-child(2) > .text").click()
        self.driver.execute_script("window.scrollTo(0,136)")
        self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(2) > .filter-options-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swatch-option-link-layered:nth-child(4) > .swatch-option").click()
        self.driver.execute_script("window.scrollTo(0,230)")
        self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(4) > .filter-options-title").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".active .item:nth-child(4) > a")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".active .item:nth-child(4) > a").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".item:nth-child(1) > .product-item-info .product-image-photo")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".item:nth-child(1) > .product-item-info .product-image-photo").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".fotorama__img")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.ID, "option-label-size-143-item-167").click()
        self.driver.find_element(By.ID, "option-label-color-93-item-56").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

# EndRegion TEST SUITE
