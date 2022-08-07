from pathlib import Path

from generic_scraper.scraper import Scraper
from generic_scraper.extractor import Extractor
from generic_scraper.config import scraper_config


def main():
    config_file = Path.joinpath(Path.cwd(), "test.yml")
    scraper_config.config_from_file(config_file)
    scraper = Scraper(scraper_config)
    scraper.scrape()
    extractor = Extractor(scraper_config)
    extractor.extract()
    data = extractor.serialize()

    print(data)


if __name__ == "__main__":
    main()
