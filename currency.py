import requests as rq
from bs4 import BeautifulSoup as bs
import time

class Currency:

    DOLLAR_RUB = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&aqs=chrome..69i57j0i512l9.2143j1j7&sourceid=chrome&ie=UTF-8'
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    
    currentConvertedPrice = 0
    difference = 5
    
    def __init__(self):
        self.currentConvertedPrice = float(self.getCurrencyPrice())
    
    def getCurrencyPrice(self):
        full_page = rq.get(self.DOLLAR_RUB, headers=self.headers)
        soup = bs(full_page.content, 'html.parser')
        convert = soup.findAll('span', {'class' : 'DFlfde', 'class' : 'SwHCTb', 'data-precision' : 2})
        return convert[0].text
    
    def checkCurrency(self):
        currency = float(self.getCurrencyPrice().replace(',', '.'))
        if currency >= self.currentConvertedPrice + self.difference:
            print('Курс сильно вырос')
        elif currency <= self.currentConvertedPrice + self.difference:
            print('Курс сильно упал')
        print('Сейчас 1 доллар = ', currency)
        time.sleep(3)
        self.checkCurrency()
    
# RUN
currency = Currency()
currency.checkCurrency()