import requests
from bs4 import BeautifulSoup


class Scraper(object):
    def __init__(self, scraper_config):
        self.app_config = scraper_config.app_config
        self.url_list = scraper_config.urls

    def collect_matches(self, list_index, soup):
        config = self.url_list[list_index].config

        for container in soup.findAll(
                config.container_el, {config.container_attr: config.container_val}
        ):
            for list_item in container.find_all(
                    config.list_item_el, {config.list_item_attr: config.list_item_val}, href=config.href
            ):
                self.url_list[list_index].matches.append(list_item)



    def scrape_page(self, list_index):
        url = self.url_list[list_index].url
        result = requests.get(url)
        html = result.text
        soup = BeautifulSoup(html, 'html.parser')
        self.collect_matches(list_index, soup)
        soup.find().next

    def scrape(self):
        for i, url in enumerate(self.url_list):
            self.scrape_page(i)





