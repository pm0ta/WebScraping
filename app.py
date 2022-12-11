# Web Scraping
from playwright.sync_api import sync_playwright
import time
import requests
from bs4 import BeautifulSoup

search = input('Produto: ') # vai perguntar para o usuário qual produto ele deseja pesquisar para obter informações, e vai guardar esse nome do produto na variável "search"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False); #não te interessa
    page = browser.new_page(); #não te interessa
    url = page.goto(f'https://www.pichau.com.br/search?q={search}') # vai entrar no site da PICHAU e vai pesquisar pelo produto que o cliente pesquisou logo acima
    page.locator('xpath=/html/body/div[1]/main/div[2]/div/div[1]/div[2]/div[1]/a/div/div[3]').click()
    time.sleep(3) # vai esperar 3s para executar os códigos da linha de baixo:

    requestpage = requests.get(url) # está fazendo uma requisição para pegar informações do site da pichau
    soup = BeautifulSoup(requestpage.content, 'html.parser') # não interessa
    title = soup.find('h1', {'data-cy': 'product-page-title'}).text # vai entrar 
    print(title)

    time.sleep(60)

# url = 'https://www.pichau.com.br/teclas-para-teclado-mecanico-redragon-preta-a106' 
# page = requests.get(url)
# soup = BeautifulSoup(page.content, 'html.parser')
# time.sleep(2)
# title = soup.find('h1', {'data-cy':'product-page-title'}).text