from bs4 import BeautifulSoup
import requests

class Exchange:
    def __init__(self):
        self.__exchange_rate = self.__parse_data()

    def __parse_data(self) -> list:
        html = requests.get('https://finance.naver.com/marketindex/exchangeList.naver').text
        soup=BeautifulSoup(html,'html.parser')
        data=soup.find_all('td', attrs={'class':'sale'})
        result =[]
        for i in range(4):
             result.append(float(data[i].text.replace(',','')))
        result[2] /= 100#엔화 보정
        return result
        
    def calc_excange(self, amount:int, currency:int) -> int:
        if currency == 0:
            return amount
        else:
            return int(amount * self.__exchange_rate[currency-1])


if __name__ == "__main__":
    e=Exchange()
    e.calc_excange(10000, 3)