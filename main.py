import requests
from bs4 import BeautifulSoup
from config import URL
import psycopg2


url = URL

try:
    conn = psycopg2.connect(database="babos", user="postgres",password="12345678", host="127.0.0.2", port=5432)
    print("success")
except Exception as ex:
    print("fail")
    print(ex)

def stat():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    league_parce = soup.find_all('td',class_='tleague')
    home_team = soup.find_all('td', class_='thome')
    away_team = soup.find_all('td', class_='taway')
    odds_ = soup.find_all('td', class_='odds_col')
    tvol = soup.find_all('td', class_='tvol')
    i = 0
    while i != len(tvol):
        odds_prepare = odds_[int(i)].text
        odds_prepare_2 = odds_[int(i) + 2].text
        odds_durty, odds_clear = odds_prepare.split('€')
        odds_durty_2, odds_clear_2 = odds_prepare_2.split('€')

        result = league_parce[int(i)].text + ' ' + home_team[int(i) + 4].text + ' = ' + odds_clear + ' ' + away_team[int(i)].text + ' = ' + odds_clear_2
        print(result)
        i += 1
    return len(tvol)
print(stat())