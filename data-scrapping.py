from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
# from collections import Counter

driver = webdriver.Chrome()
target_word = 'Injury'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}

# f = open('inj2021-22.txt','w')

for x in range(2013,2023):
    season_inj = 0
    f = open('inj{}.txt'.format(str(x+1)),'w')
    for i in range(1,39):
        url = 'https://www.transfermarkt.us/premier-league/spieltag/wettbewerb/GB1/plus/?saison_id={}&spieltag={}'.format(str(x),str(i))
        driver.get(url)
        match_report_links = driver.find_elements(By.XPATH, '//a[@title="Match report" and @class="liveLink"]')
        tot = 0

        for match_report_link in match_report_links:
            href_value = match_report_link.get_attribute('href')
            # print("Match Report link:", href_value)
            response = requests.get(href_value,headers=headers, allow_redirects=True)
            response.raise_for_status() 
            soup = BeautifulSoup(response.text, 'html.parser')
            for k in soup.find_all('span',class_='hide-for-small'):
                if target_word in k.text:
                    tot += 1
        season_inj += tot
        # print('Matchday {}: {}'.format(str(i),str(tot)))
        f.write('Matchday {}: {}\n'.format(str(i),str(tot)))
    # print('\nSeason Injury: {}\n'.format(str(season_inj)))
    f.write('\nSeason Injury: {}\n'.format(str(season_inj)))
    f.close()