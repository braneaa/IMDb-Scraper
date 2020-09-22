from UI import *

if __name__ == '__main__':
    scraper = IMDbScraper(True, "Shrek")
    ctrl = Controller(scraper)
    ui = UI(ctrl)
    ui.start()
