from abc import ABC, abstractmethod
from typing import final
import requests
from bs4 import BeautifulSoup

class AbstractWebScraper(ABC):

    DOMAIN = 'https://fr.wikipedia.org'
    DEFAULT_PARSER = 'html.parser'
    DATA_DETAILED = True
    DATA_NOT_DETAILED = False
    OUTPUTS = ['print', 'txt']
    OUTPUT_DIRECTORY = 'output/'

    @final
    def __init__(self, url, data_detailed=DATA_NOT_DETAILED, outputs=[], outputFileName='output'):
        self.url = url
        self.data_detailed = data_detailed
        self.soup = ''
        self.data = []
        self.outputs = outputs
        self.outputFileName = outputFileName

    @final
    def scrape(self):
        self.makeSoup()
        self.parse()
        self.sendData()

    @final
    def makeSoup(self):
        response = requests.get(self.url)
        if(response.ok):
            self.soup = BeautifulSoup(response.text, self.DEFAULT_PARSER)
            self.soup.prettify()
        else:
            print('### ERROR : ' + str(response))

    @abstractmethod
    def parse(self):
        pass

    @final
    def sendData(self):
        if len(self.data) != 0:

            # display data
            if('print' in self.outputs):
                print(*self.data, sep='\n')

            # store data in .txt file
            if('txt' in self.outputs):
                with open(self.OUTPUT_DIRECTORY + self.outputFileName + '.txt', 'w') as file:
                    for row in self.data:
                        file.write(str(row) + '\n')
