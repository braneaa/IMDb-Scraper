from selenium import webdriver


def setPageIncognito():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")


def maximize():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
