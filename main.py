from model.european_countries_scraper import EuropeanCountriesScraper
from model.country_scraper import CountryScraper
from model.abstract_web_scraper import AbstractWebScraper

FRANCE_URL = AbstractWebScraper.DOMAIN + '/wiki/France'
FRANCE_OUTPUT_FILENAME = 'france'

EUROPE_URL = AbstractWebScraper.DOMAIN + '/wiki/Liste_des_pays_d%27Europe'
EUROPE_OUTPUT_FILENAME = 'europeans_countries'

# scraping a country
CountryScraper(
    FRANCE_URL,
    AbstractWebScraper.DATA_DETAILED,
    AbstractWebScraper.OUTPUTS,
    FRANCE_OUTPUT_FILENAME
).scrape()

# scraping european countries (detailed)
EuropeanCountriesScraper(
    EUROPE_URL,
    AbstractWebScraper.DATA_DETAILED,
    AbstractWebScraper.OUTPUTS,
    EUROPE_OUTPUT_FILENAME
).scrape()
