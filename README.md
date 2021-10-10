## Web-scraping with Beautiful Soup 4
*Retrieves data on European countries from [Wikipedia](https://fr.wikipedia.org/wiki/Liste_des_pays_d%27Europe):*
1. *by browsing the country list page*
2. *by browsing the page of each country for more information*

## Installation

__Requirements__
 - Python (>= 3.9.4)
 - pip (>= 21.2.4)

__Project__
```
    $ git clone https://github.com/francois-lp/python-web-scraping-bs4
```

__Dependencies__
```
	pip install requests
	pip install beautifulsoup4
```

## Getting started
```
    python main.py
```

## Options

1. The recovered data can be detailed or not
```py
    AbstractWebScraper.DATA_DETAILED = True
    AbstractWebScraper.DATA_NOT_DETAILED = False
``` 
2. The recovered data can also be displayed in console and / or written in .txt files in the 'output' directory
```py
    AbstractWebScraper.OUTPUTS = ['print', 'txt']
```

## Links
* [Beautiful Soup 4 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
