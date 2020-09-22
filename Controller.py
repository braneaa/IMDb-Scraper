import requests
from bs4 import BeautifulSoup

from IMDbScraper import *
import re


class Controller:
    def __init__(self, scraper: IMDbScraper):
        self.scraper = scraper

    def signIn(self, email, password):
        self.scraper.driver.find_element_by_xpath('//*[@id="imdbHeader"]/div[2]/div[5]/a/div').click()
        self.scraper.implicitlyWait(10)
        self.scraper.driver.find_element_by_xpath('//*[@id="signin-options"]/div/div[1]/a[1]/span[2]').click()

        self.scraper.implicitlyWait(10)

        email_box = self.scraper.driver.find_element_by_name("email")
        email_box.send_keys(email)
        self.scraper.implicitlyWait(10)
        password_box = self.scraper.driver.find_element_by_name("password")
        password_box.send_keys(password)
        self.scraper.implicitlyWait(10)

        self.scraper.driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()

    def setPageIncognito(self):
        if not self.scraper.getIsIncognito():
            self.scraper.changeIncognito()

    def goToMoviePage(self):
        self.scraper.goToMoviePage()

    def getMovieRating(self):
        return self.makeSoup().find("div", {"class": "ratingValue"}).find("strong").find("span").text

    def getMovieStoryline(self):
        return self.makeSoup().find("div", {"class": "inline canwrap"}).find("p").text

    def getMovieDescription(self):
        return self.makeSoup().find("div", {"class": "summary_text"}).text

    def goToCastList(self):
        return self.scraper.driver.find_element_by_class_name('quicklink').click()

    def getCastList(self):
        soup = self.makeSoup()
        table = soup.find("table", {"class": "cast_list"})
        castListOdd = table.find_all("tr", {"class": "odd"})
        castListEven = table.find_all("tr", {"class": "even"})

        actors = []
        if len(castListEven) != len(castListOdd):
            for i in range(len(castListEven)):
                actors.append(castListOdd[i].text)
                actors.append(castListEven[i].text)
            actors.append(len(castListOdd) - 1)
        else:
            for i in range(len(castListEven)):
                actors.append(castListOdd[i].text)
                actors.append(castListEven[i].text)

        for i in range(len(actors)):
            actors[i] = str(actors[i]).strip()
            actors[i] = re.sub('\n', '', str(actors[i]))
            actors[i] = re.sub(' {6}', '', str(actors[i]))

        return actors

    def goToUserReviews(self):
        return self.scraper.driver.find_element_by_xpath('//*[@id="titleUserReviewsTeaser"]/div/a[2]').click()

    def hideSpoilers(self):
        return self.scraper.driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[1]/form/div/div['
                                                         '1]/label/span[1]').click()

    def getUserReviews(self):
        self.goToUserReviews()
        self.hideSpoilers()
        soup = self.makeSoup()
        reviews = soup.find("div", {"class": "lister-list"}).find_all("div", {"class": "lister-item-content"})
        ratings = []
        titles = []
        authors = []
        date = []
        comment = []
        for review in reviews:
            try:
                ratings.append(review.find("div", {"class": "ipl-ratings-bar"}).text)
            except:
                ratings.append("No rating for this review")

            try:
                titles.append(review.find("a", {"class": "title"}).text)
            except:
                titles.append("Can't get the name of this review")

            try:
                authors.append(review.find("span", {"class": "display-name-link"}).text)
            except:
                authors.append("Can't get the name of this author")

            try:
                date.append(review.find("span", {"class": "review-date"}).text)
            except:
                date.append("Can't get the date of this review")

            try:
                comment.append(review.find("div", {"class": "text show-more__control"}).text)
            except:
                comment.append("Can't get this review")

        for i in range(len(ratings)):
            ratings[i] = str(ratings[i]).strip()
            ratings[i] = re.sub('\n', '', str(ratings[i]))
            titles[i] = str(titles[i]).strip()
            titles[i] = re.sub('\n', '', str(titles[i]))
            authors[i] = str(authors[i]).strip()
            authors[i] = re.sub('\n', '', str(authors[i]))
            date[i] = str(date[i]).strip()
            date[i] = re.sub('\n', '', str(date[i]))
            comment[i] = str(comment[i]).strip()
            comment[i] = re.sub('\n', '', str(comment[i]))

        return ratings, titles, authors, date, comment

    def makeSoup(self):
        return BeautifulSoup(requests.get(self.scraper.getPageCurrentUrl(), headers=headers).text, 'html.parser')

    def getRealMovieName(self):
        return self.makeSoup().find("div", {"class": "title_wrapper"}).find("h1").text

    def giveReview(self, rating, title, comment, containsSpoilers):
        self.goToUserReviews()
        self.scraper.implicitlyWait(10)
        self.scraper.driver.find_element_by_xpath('//*[@id="main"]/section/div[1]/div/a').click()

        self.scraper.implicitlyWait(10)
        if rating == 1:
            self.scraper.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[3]/div[1]/div/a[1]').click()
        elif rating == 2:
            self.scraper.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[3]/div[1]/div/a[2]').click()
        elif rating == 3:
            self.scraper.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[3]/div[1]/div/a[3]').click()
        elif rating == 4:
            self.scraper.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[3]/div[1]/div/a[4]').click()
        elif rating == 5:
            self.scraper.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[3]/div[1]/div/a[5]').click()
        elif rating == 6:
            self.scraper.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[3]/div[1]/div/a[6]').click()
        elif rating == 7:
            self.scraper.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[3]/div[1]/div/a[7]').click()
        elif rating == 8:
            self.scraper.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[3]/div[1]/div/a[8]').click()
        elif rating == 9:
            self.scraper.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[3]/div[1]/div/a[9]').click()
        elif rating == 10:
            self.scraper.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[3]/div[1]/div/a[10]').click()

        self.scraper.implicitlyWait(10)
        title_box = self.scraper.driver.find_element_by_xpath('//*[@id="react-entry-point"]/div/div/div[1]/div[5]/div[1]/input')
        title_box.send_keys(title)

        self.scraper.implicitlyWait(10)
        comment_box = self.scraper.driver.find_element_by_xpath('//*[@id="react-entry-point"]/div/div/div[1]/div[5]/div[2]/textarea')
        comment_box.send_keys(comment)

        self.scraper.implicitlyWait(10)
        if containsSpoilers:
            self.scraper.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[5]/div[3]/div/ul/li[1]/span[1]').click()
        else:
            self.scraper.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[5]/div[3]/div/ul/li[2]/span[1]').click()

