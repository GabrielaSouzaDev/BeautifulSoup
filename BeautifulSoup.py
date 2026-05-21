# Autor: Gabriela Souza
# Projeto de Raspagem de Dados

# Importação da biblioteca que faz leitura de páginas web
from bs4 import BeautifulSoup 

# Abrir o arquivo HTML
with open('index.html', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

# Leitura do HTML
site = BeautifulSoup(conteudo, 'html.parser')

# Buscar todos os cards da página
produtos = site.find_all('div', class_='card')

# Loop para percorrer os produtos
for produto in produtos:

    nome = produto.find('div', class_='nome').text.strip()
    preco = produto.find('div', class_='preco').text.strip()

    print('===============================')
    print(f'Produto: {nome} \nPreço: {preco}')

    