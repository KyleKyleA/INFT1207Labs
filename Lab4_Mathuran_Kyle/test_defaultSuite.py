"""
Name: Mathuran Chandramohan, Kyle Angeles
Course: INFT 1207
Date: July 12th, 2025
Description: Set of test cases for https://www.calculator.net/body-fat-calculator.html
             web elements
"""

#region IMPORTS
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
#endregion IMPORTS

#region TEST SUITE
class TestDefaultSuite(object):
  def setup_method(self, method):
    """Class setup - runs before all tests"""
    self.driver = webdriver.Edge()
    self.vars = {}

  def teardown_method(self, method):
    """Class teardown - runs after all tests"""
    self.driver.quit()

  def test_male_body_fat(self):
    """Simulates user input on body fat calculator site for male subject"""
    self.driver.get("https://www.calculator.net/body-fat-calculator.html")
    self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").send_keys("15")
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("220")
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("90")
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("18")
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("100")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 60.7%"
    print(str("Body Fat (Male): 60.7%"))
    self.driver.close()

  def test_female_body_fat(self):
    """Simulates user input on body fat calculator site for female subject"""
    self.driver.get("https://www.calculator.net/body-fat-calculator.html")
    self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2) > .rbmark").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").send_keys("40")
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("100")
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("189")
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("57")
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("98")
    self.driver.find_element(By.ID, "chipmeter").click()
    self.driver.find_element(By.ID, "chipmeter").send_keys("100")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 23.0%"
    print(str("Body Fat (Female): 23.0%"))
    self.driver.close()
#endregion TEST SUITE