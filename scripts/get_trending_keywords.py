# 인기키워드 수집 스크립트

import requests
from bs4 import BeautifulSoup
import re

def get_nate_pann_trending_keywords():
    url = 'https://www.nate.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    raw_keywords = [item.text.strip() for item in soup.select('.isKeyword')]
    keywords = [re.sub(r'\s+', ' ', kw) for kw in raw_keywords if kw]
    return keywords

if __name__ == "__main__":
    trending_keywords = get_nate_pann_trending_keywords()
    print(trending_keywords)
