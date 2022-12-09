import requests
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0' } 
    url = 'https://order.subway.com/en-US/restaurant/2911-0/menu'
    url = 'https://order.subway.com/en-US/restaurant/23554-0/menu/category/1'
    url ='https://order.subway.com/en-US/restaurant/23554-0/customizer/productSummary/4259/category/812'
    #url = 'https://order.subway.com/en-US'
    response = requests.get(url, allow_redirects=False, timeout=1000, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    #options = webdriver.ChromeOptions()
    #options.add_argument("start-maximized")
    #driver = webdriver.Chrome(options=options)
    
    #response = driver.get(url)
    #time.sleep(5)
    print(soup)
    sandwiches = soup.find_all('div', class_ ='cs-card-title')
    #print(response)
    #driver.close()
    return render_template('index.html', sandwiches)

if __name__ == '__main__':
    app.run(debug=True)