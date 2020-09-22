from UI import *

if __name__ == '__main__':
    scraper = IMDbScraper()
    ctrl = Controller(scraper)
    ui = UI(ctrl)
    ui.start()
