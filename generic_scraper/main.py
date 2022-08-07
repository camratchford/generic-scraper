from scraper import Scraper
from extractor import Extractor

from config import scraper_config


if __name__ == "__main__":

    scraper_config.config_from_file(r"C:\Users\cameron\PyCharm Projects\level_scraper\config.yml")

    scraper = Scraper(scraper_config)
    scraper.scrape()
    extractor = Extractor(scraper_config)
    extractor.extract()
    print(extractor.serialize())

