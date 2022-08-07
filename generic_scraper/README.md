<h1 align="center">Generic Scraper</h1>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/camratchford/generic_scraper.svg)](https://github.com/camratchford/pymetrics/pulls)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> A simple metrics client enabling fetching of metrics via http requests.<br>Limitless utility through Python user scipts.</p>
<br>

> This role is currently in early developement and is highly (possibly completely) unstable.
> 
> Use at your own risk. Or preferably, wait until it's "done".


## Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Configuration Options](./pymetrics/docs/CONFIGURATION_OPTIONS.md)
- [Script Modules](./pymetrics/docs/SCRIPT_MODULES.md)
- [SSL](./pymetrics/docs/SSL.md)
- [Built Using](#built_using)
- [TODO](./pymetrics/docs/TODO.md)
- [Contributing](./pymetrics/docs/CONTRIBUTING.md)
- [Authors](#authors)

## About <a name = "about"></a>
Generic Scraper is a low code basic web scraper driven by yaml/json config files

## Getting Started <a name = "getting_started"></a>


Clone the repo
```shell
 cd /opt/
 git clone https://github.com/camratchford/generic_scraper.git
 ```

Set up your venv  
```shell
cd ./generic_scraper
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install .
```

Create a yaml config file, filling the variables with your own

```yaml
# Will scrape job postings from a level.co job board
scraper_configs:
  level:
    container_el: div
    container_attr: class
    container_val: postings-wrapper
    list_item_el: a
    list_item_attr: "class"
    list_item_val:
      - posting-title
    href: True
    extract_items:
      - name: title
        tag: h5
        attr: data-qa
        val: posting-name
      - name: link
        tag: a
        attr: href
        val:
      - name: location
        tag: span
        attr: class
        val: sort-by-location
      - name: team
        tag: span
        attr: class
        val: sort-by-team

scraper_urls:
  - url: https://jobs.lever.co/imperfectfoods
    pagination: False
    config: level

  - url: https://jobs.lever.co/cfsenergy
    pagination: False
    config: level


```

Using the generic_scraper module

```python
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

```


## Running the tests <a name = "tests"></a>
There are no tests

### Coding Style
PEP-8 

##  Usage <a name="usage"></a>
All items are susceptible to change at any moment. Don't use it.

## Deployment <a name = "deployment"></a>
As yet untested in production. Use at your own risk.

## Built Using <a name = "built_using"></a>
- [FastAPI](https://fastapi.tiangolo.com/) - ASGI based asynchronous Python web framework 
- [Uvicorn](https://www.uvicorn.org/) - ASGI Web Server

## Authors <a name = "authors"></a>
- [@camratchford](https://github.com/camratchford) - Putting the pieces together

See also the list of [contributors](https://github.com/camratchford/blogsite/contributors) who participated in this project