from model.abstract_web_scraper import AbstractWebScraper
from model.country_scraper import CountryScraper

class EuropeanCountriesScraper(AbstractWebScraper):

    def parse(self):
        # get table of countries
        table = self.soup.find(
            'table', class_=['wikitable ', 'sortable', 'jquery-tablesorter'])

        # get lines
        trs = table.tbody.find_all('tr')

        for tr in trs:
            country = {}
            country['link'] = ''
            country_detailed = {}
            columnNumber = 0
            country_merged = {}

            # get columns and data
            tds = tr.find_all('td')
            for td in tds:
                columnNumber += 1
                if (columnNumber == 3):
                    nameLink = td.find('a')
                    country['name'] = nameLink.get_text()
                    country['link'] = AbstractWebScraper.DOMAIN + \
                        nameLink['href']
                elif (columnNumber == 6):
                    country['population'] = td.get_text(
                        strip=True).replace(u'\xa0', u' ')
                elif (columnNumber == 7):
                    country['area'] = td.get_text(
                        strip=True).replace(u'\xa0', u' ')

            if(self.data_detailed == AbstractWebScraper.DATA_DETAILED and country['link'] != ''):
                # get country detailed
                country_scraping = CountryScraper(country['link'])
                country_scraping.scrape()
                country_detailed = country_scraping.data[len(
                    country_scraping.data)-1]

                # merge
                country_merged = country | country_detailed
            else:
                country_merged = country

            # add country to the list
            self.data.append(country_merged)
