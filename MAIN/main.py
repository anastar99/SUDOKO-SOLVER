from secrets import PATH, nyTimesLink
from sudokoLogic import SudokoChecks
from setupGrid import SudokoSetup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import bs4
from seleniumSetup import BrowserSetup

def browserSetup():

    browser = webdriver.Chrome(PATH)
    browser.get(nyTimesLink)
    time.sleep(6)

    return browser

    
def actionSetup(browser):
    return ActionChains(browser)