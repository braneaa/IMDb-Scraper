from util import *

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/71.0.3578.98 Safari/537.36 "
}


class IMDbScraper:
    def __init__(self, isIncognito=False, movieName=""):
        self.isIncognito = isIncognito
        if self.isIncognito:
            setPageIncognito()
        self.driver = webdriver.Chrome("D:\WebScraping\webdriver\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.imdb.com/")
        self.movieName = movieName

    def getMovieName(self):
        return self.movieName

    def setMovieName(self, newName):
        self.movieName = newName

    def getIsIncognito(self):
        return self.isIncognito

    def getDriver(self):
        return self.driver

    def changeIncognito(self):
        self.isIncognito = not self.isIncognito

    def writeInSearchBox(self):
        search_box = self.driver.find_element_by_name('q')
        search_box.send_keys(self.movieName)

    def implicitlyWait(self, waitTime):
        self.driver.implicitly_wait(waitTime)

    def clickSearchButton(self):
        search_button = self.driver.find_element_by_id('suggestion-search-button')
        search_button.click()

    def getPageCurrentUrl(self):
        return self.driver.current_url

    def clickOnDesiredMovie(self):
        movie = self.driver.find_element_by_class_name("primary_photo")
        movie.click()

    def goToMoviePage(self):
        self.writeInSearchBox()
        self.implicitlyWait(10)
        self.clickSearchButton()
        self.implicitlyWait(10)
        self.clickOnDesiredMovie()
