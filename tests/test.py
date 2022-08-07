from generic_scraper.scraper import Scraper
from generic_scraper.extractor import Extractor
from generic_scraper.config import scraper_config

def main():
    scraper_config.config_from_file(r"C:\Users\cameron\PyCharm Projects\level_scraper\tests\test.yml")
    scraper = Scraper(scraper_config)
    scraper.scrape()
    extractor = Extractor(scraper_config)
    extractor.extract()
    data = extractor.serialize()

    print(data)


if __name__ == "__main__":
    main()
