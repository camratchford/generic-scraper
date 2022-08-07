
class Extractor(object):
    def __init__(self, config):
        self.app_config = config.app_config
        self.urls = config.urls
        self.extracted_pages = []

    def extract_page(self, list_index):
        import re
        config = self.urls[list_index].config
        elements = self.urls[list_index].matches

        extract_list = []
        for i, el in enumerate(elements):
            extracted_item = {}
            for item in config.extract_items:

                if not isinstance(item, dict):
                    extracted_item[item.name] = el.find(name=item.tag, attrs={item.attr: re.compile(f"{item.val}")})

                    if extracted_item[item.name]:
                        extracted_item[item.name] = extracted_item[item.name].text
                    else:
                        extracted_item[item.name] = el.findNext(name=item.tag, attrs={item.attr: re.compile(f"{item.val}")})
                    if item.attr == "href":

                        link = el.attrs['href']
                        extracted_item[item.name] = link

            extract_list.append(extracted_item)

        self.extracted_pages.append(extract_list)


    def extract(self):
        for i, url in enumerate(self.urls):
            self.extract_page(i)

    def serialize(self):
        new_list = []
        for page in self.extracted_pages:
            new_list.extend(page)
        return new_list
