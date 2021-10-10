from model.abstract_web_scraper import AbstractWebScraper

class CountryScraper(AbstractWebScraper):

    def parse(self):
        country = {}

        # get title of page
        title = self.soup.find('header', class_=['mw-body-header']).find('h1')
        country['name'] = title.get_text(strip=True)

        # get table of page
        tables = self.soup.find_all('table')
        for table in tables:

            # get lines
            trs = table.tbody.find_all('tr')
            for tr in trs:

                # get columns and data
                th = tr.find('th')
                if(th):
                    if(th.get_text() == 'Fête nationale'):
                        td = tr.find('td')
                        country['national_day'] = td.get_text(strip=True)
                    if(th.get_text() == 'Code ISO 3166-1'):
                        td = tr.find('td')
                        country['code_iso'] = td.get_text(
                            strip=True).replace(u'\u200b', u'')
                    if(th.get_text() in ['Plus grandes villes', 'Plus grande ville']):
                        td = tr.find('td')
                        country['bigger_cities'] = str(
                            td.get_text(strip=True).encode('utf-8'))
                    if(th.get_text() == 'Domaine Internet'):
                        td = tr.find('td')
                        country['internet_domain'] = td.find(
                            'a').get_text(strip=True)

        # add country to the list
        self.data.append(country)
