

class Url(object):
    def __init__(self):
        self.url = ""
        self.pagination = False
        self.pagination_pattern = {}
        self.config = None
        self.matches = []

    @staticmethod
    def paginate(dic):
        pages_list = []
        base_url = dic['url']
        position = dic['pagination_pattern']['position']
        for i in range(1, dic['pagination_pattern']['limit']):
            page = f"{dic['pagination_pattern']['string']}{str(i)}/"
            new_url = base_url[:position] + page + base_url[position:]

            url = {}
            url['url'] = new_url
            url['config'] = dic['config']
            pages_list.append(url)

        return pages_list



