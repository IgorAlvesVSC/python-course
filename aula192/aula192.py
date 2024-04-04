# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4
import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.uol.com.br/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

# if parsed_html.title is not None:
#     print(parsed_html.title.text)

example_selector_heading = parsed_html.select_one('#lu7gfbwz')

if example_selector_heading is not None:
    div = example_selector_heading.parent

    if div is not None:
        for d in div.select('div'):
            print(re.sub(r'\s{1,}', '', d.text).strip())
