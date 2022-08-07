import json
import yaml

from pathlib import Path
from os import environ

from generic_scraper.scraper.urls import Url
from generic_scraper.scraper.config import Config
from generic_scraper.extractor.items import Item


class ScraperConfig(object):
    def __init__(self):
        self.app_config = dict()
        self.scraper_urls = dict()
        self.scraper_configs = dict()
        self.urls = None
        self.config_path = Path.joinpath(Path.cwd(), "")

    def config_from_file(self, file=""):
        if not file:
            file = environ.get('SCRAPER_CONFIG_PATH', None)
        loaded_config = {}
        if file:
            self.config_path = file
        if Path(self.config_path):
            if ".yaml" in str(self.config_path) or ".yml" in str(self.config_path):
                with open(self.config_path, "r") as file:
                    loaded_config = yaml.safe_load(file)
            elif ".json" in str(self.config_path):
                with open(self.config_path, "r") as file:
                    loaded_config = json.load(file)
            for attr in loaded_config.keys():

                if hasattr(self, attr):
                    setattr(self, attr, loaded_config[attr])

        self.urls = self.build_urls(self.scraper_urls)
        print(self.urls[0].config.href)


    def build_config(self, config_dict):
        config = config_dict
        object_config = Config()

        for attr in config.keys():
            if hasattr(object_config, attr):
                setattr(object_config, attr, config[attr])
            if attr == "extract_items":
                for item in config["extract_items"]:
                    if isinstance(item, dict):

                        config_item = Item()
                        config_item.attr = item['attr']
                        config_item.name = item['name']
                        config_item.tag = item['tag']
                        config_item.val = item['val']

                        object_config.extract_items.append(config_item)

        return object_config

    def build_urls(self, urls):


        urls_list = []
        for url in urls:
            if url['pagination']:
                pagination_list = Url.paginate(url)
                for page in pagination_list:
                    object_url = Url()
                    for attr in page.keys():
                        if hasattr(object_url, attr):
                            setattr(object_url, attr, page[attr])
                            if attr == "config":
                                setattr(object_url, attr, self.build_config(self.scraper_configs[url["config"]]))

                    urls_list.append(object_url)
            else:
                object_url = Url()
                for attr in url.keys():
                    if hasattr(object_url, attr):
                        setattr(object_url, attr, url[attr])
                        if attr == "config":
                            setattr(object_url, attr, self.build_config(self.scraper_configs[url["config"]]))
                urls_list.append(object_url)

        return urls_list


scraper_config = ScraperConfig()

