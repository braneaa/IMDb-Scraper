from Controller import *
from tkinter import *
import subprocess


class UI:
    def __init__(self, controller: Controller):
        self._ctrl = controller
        self.root = Tk()
        self.root.configure(background="black")
        self.root.title("IMDb Scraper")
        self.welcomeLabel = Label(self.root, text="Welcome", bg="black", fg="white", font="none 14 bold")
        self.opt1 = Label(self.root, text="Name of the movie ", bg="black", fg="white", font="none 10 bold")
        self.opt2 = Label(self.root, text="Give review ", bg="black", fg="white", font="none 10 bold")
        self.opt3 = Label(self.root, text="See some user reviews ", bg="black", fg="white", font="none 10 bold")
        self.opt4 = Label(self.root, text="See IMDb rating ", bg="black", fg="white", font="none 10 bold")
        self.opt5 = Label(self.root, text="See the full cast ", bg="black", fg="white", font="none 10 bold")
        self.opt6 = Label(self.root, text="See the description of the movie", bg="black", fg="white",
                          font="none 10 bold")
        self.opt7 = Label(self.root, text="See the storyline of the movie", bg="black", fg="white",
                          font="none 10 bold")
        self.space = Label(self.root, text="         ", bg="black")
        self.entry = Entry(self.root, width=40, bg="white")
        self.openMoviePageBtn = Button(self.root, text="Open", width=4, command=self.goToMoviePage)
        self.openRatingWindowBtn = Button(self.root, text="See Rating", width=14, command=self.openRatingWindow)
        self.openDescriptionWindowBtn = Button(self.root, text="See Description", width=14,
                                               command=self.openDescriptionWindow)
        self.openCastWindowBtn = Button(self.root, text="See Cast List", width=14,
                                        command=self.openCastWindow)
        self.openStorylineBtn = Button(self.root, text="See The Storyline", width=14,
                                       command=self.openStorylineWindow)
        self.openUserReviewsBtn = Button(self.root, text="User Reviews", width=14,
                                         command=self.openUserReviewsWindow)
        self.quitBtn = Button(self.root, text="Quit", width=5, command=self.quitApp)
        self.signInBtn = Button(self.root, text="Sign In", width=10, command=self.signIn)
        self.giveReviewBtn = Button(self.root, text="Review", width=14, command=self.giveReview)

    def giveReview(self):
        giveReviewWindow = Toplevel(self.root)
        giveReviewWindow.title("Give Review")
        giveReviewWindow.configure(background="black")

        Label(giveReviewWindow, text="Give the rating: ", bg="black", fg="white",
              font="none 10 bold").grid(row=0, column=0)
        Label(giveReviewWindow, text="Review title: ", bg="black", fg="white",
              font="none 10 bold").grid(row=1, column=0)
        Label(giveReviewWindow, text="Comment: ", bg="black", fg="white",
              font="none 10 bold").grid(row=2, column=0)
        Label(giveReviewWindow, text="Does this review contain spoilers?: ", bg="black", fg="white",
              font="none 10 bold").grid(row=3, column=0)
        clicked = IntVar()
        clicked.set(1)
        drop = OptionMenu(giveReviewWindow, clicked, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        drop.grid(row=0, column=1)

        title = Entry(giveReviewWindow, width=30, bg="white")
        title.grid(row=1, column=1)
        comment = Entry(giveReviewWindow, width=100, bg="white")
        comment.grid(row=2, column=1)
        var = IntVar()
        spoiler = Checkbutton(giveReviewWindow, variable=var)
        spoiler.grid(row=3, column=1)
        if var.get() == 1:
            hasSpoilers = True
        else:
            hasSpoilers = False
        Button(giveReviewWindow, text="Send Review",
               command=lambda: self._ctrl.giveReview(clicked.get(), title.get(), comment.get(), hasSpoilers)).grid(
            row=4, column=1)

    def signIn(self):
        signInWindow = Toplevel(self.root)
        signInWindow.title("Sign In")
        signInWindow.configure(background="black")

        email = Entry(signInWindow, width=60, bg="white")
        email.grid(row=0, column=1)
        password = Entry(signInWindow, show="*", width=60, bg="white")
        password.grid(row=1, column=1, pady=10)

        Label(signInWindow, text="Email : ", bg="black", fg="white").grid(row=0, column=0)
        Label(signInWindow, text="Password : ", bg="black", fg="white").grid(row=1, column=0)

        btn = Button(signInWindow, text="Sign In", width=10,
                     command=lambda: self._ctrl.signIn(email.get(), password.get()))
        btn.grid(row=2, column=1)

    def quitApp(self):
        self.root.destroy()

    def openUserReviewsWindow(self):
        ratings, titles, authors, date, comment = self.getUserReviews()
        f = open("user_reviews.txt", "w")
        f.write('These reviews are sorted by helpfulness: \n \n')
        for i in range(1, len(ratings)):
            try:
                f.write("Review " + str(i) + '\n')
                f.write("Rating : " + str(ratings[i]) + '\n')
                f.write("Title : " + str(titles[i]) + '\n')
                f.write("Author : " + str(authors[i]) + '\n')
                f.write("Date : " + str(date[i]) + '\n')
                f.write("Review : " + str(comment[i]) + '\n')
                f.write('\n')
            except:
                f.write('\n')

    def openStorylineWindow(self):
        storylineWindow = Toplevel(self.root)
        storylineWindow.title("Storyline")
        storylineWindow.configure(background="black")
        storyline = Label(storylineWindow, text=self.getMovieStoryline(), bg="black", fg="white", font="none 11 bold",
                          wraplength=200, width=50)
        storyline.pack()

    def getMovieRating(self):
        try:
            return self._ctrl.getMovieRating()
        except:
            return False

    def getMovieDescription(self):
        try:
            return self._ctrl.getMovieDescription()
        except:
            return ""

    def getMovieStoryline(self):
        try:
            return self._ctrl.getMovieStoryline()
        except:
            ""

    def goToCastList(self):
        return self._ctrl.goToCastList()

    def getCastList(self):
        return self._ctrl.getCastList()

    def getUserReviews(self):
        return self._ctrl.getUserReviews()

    def openDescriptionWindow(self):
        descriptionWindow = Toplevel(self.root)
        descriptionWindow.title("Description")
        descriptionWindow.configure(background="black")
        description = Label(descriptionWindow, text=self.getMovieDescription(), bg="black", fg="white", font="none 11 "
                                                                                                             "bold",
                            wraplength=200, width=50)
        description.grid(row=0, column=0)

    def openCastWindow(self):
        self.goToCastList()
        castWindow = Toplevel(self.root)
        castWindow.title("Cast List")
        castWindow.configure(background="black")
        listbox = Listbox(castWindow, width=70)
        listbox.grid(row=0, column=0)
        for actor in self.getCastList():
            listbox.insert(END, actor)

    def openRatingWindow(self):
        ratingWindow = Toplevel(self.root)
        ratingWindow.title("Rating")
        ratingWindow.configure(background="black")
        if self.getMovieRating():
            text = self._ctrl.getRealMovieName() + "'s grade is " + str(self.getMovieRating()) + " out of 10!"
        else:
            text = "You haven't selected any movie yet!"
        rating = Label(ratingWindow, text=text, bg="black", fg="white", font="none 11 bold")
        rating.grid(row=0, column=0)

    def addWidgetsToGrid(self):
        self.welcomeLabel.grid(row=0, column=1, sticky=N)
        self.opt1.grid(row=1, column=0, sticky=W)
        self.opt2.grid(row=2, column=0, sticky=W)
        self.opt3.grid(row=3, column=0, sticky=W)
        self.opt4.grid(row=4, column=0, sticky=W)
        self.opt5.grid(row=5, column=0, sticky=W)
        self.opt6.grid(row=6, column=0, sticky=W)
        self.opt7.grid(row=7, column=0, sticky=W)
        self.space.grid(row=1, column=4)
        self.entry.grid(row=1, column=3)
        self.openMoviePageBtn.grid(row=1, column=5)
        self.openRatingWindowBtn.grid(row=4, column=3)
        self.openDescriptionWindowBtn.grid(row=6, column=3)
        self.openCastWindowBtn.grid(row=5, column=3)
        self.openStorylineBtn.grid(row=7, column=3)
        self.openUserReviewsBtn.grid(row=3, column=3)
        self.quitBtn.grid(row=8, column=1)
        self.signInBtn.grid(row=0, column=0)
        self.giveReviewBtn.grid(row=2, column=3)

    def getMovieFromEntry(self):
        return self.entry.get()

    def start(self):
        self.addWidgetsToGrid()
        self.root.mainloop()

    def goToMoviePage(self):
        movieName = self.getMovieFromEntry()
        self._ctrl.scraper.setMovieName(movieName)
        self._ctrl.goToMoviePage()
