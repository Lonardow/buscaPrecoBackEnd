import psycopg2
from datetime import datetime, timezone
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as condicao_esperada
import schedule
from time import sleep

conexao = psycopg2.connect(
    database='railway',
    user='postgres',
    password='QUxLaUb4j71t4jE8JO3Q',
    port='5525',
    host='containers-us-west-129.railway.app',
)

sql = conexao.cursor()


def novo_produto(sql, conexao, nome, preco, site, data_cotacao, link_imagem):
    # verificar se existe um produto igual ja cadastrado
    query = 'SELECT * FROM app_buscapreco_produto WHERE nome=%s and preco=%s and site=%s'
    valores = (nome, preco, site)
    resultado = sql.execute(query, valores)
    dados = sql.fetchall()

    if len(dados) == 0:
        # se não houver dados iguais, gravar um novo produto
        query = 'INSERT INTO app_buscapreco_produto(nome, preco, site,data_cotacao, link_imagem) VALUES(%s,%s,%s,%s,%s)'
        valores = (nome, preco, site, data_cotacao, link_imagem)
        sql.execute(query, valores)

    # se ja houver dados iguais, nao gravar
    else:
        print('Dados já cadastrados anteriormente!')


# novo_produto(sql, conexao, 'iphone 15', '13000.50',
#              'apple.com/ihone15', datetime.now(), 'www.image.com/imagem1.jpg')
    conexao.commit()

# Criar web scraper(atraves do selenium)


def iniciar_driver():
    chrome_options = Options()

    arguments = ['--lang=en-US', '--window-size=1920,1080',
                 '--incognito',  # '--deadless'
                 ]

    for argument in arguments:
        chrome_options.add_argument(argument)

        chrome_options.add_experimental_option('prefs', {
            'download.prompt_for_download': False,
            'profile.default_content_settings_values.notifications': 2,
            'profile.default_content_values.automatic_downloads': 1
        })

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=chrome_options)
        wait = WebDriverWait(
            driver,
            10,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchAttributeException,
                ElementNotVisibleException,
            ]
        )
        return driver, wait


def varrer_site_1():
    # 1- Entrar no site https://site1produto.netlify.app
    driver, wait = iniciar_driver()
    driver.get('https://site1produto.netlify.app')
    # 2-  Anotar o nome do produto
    nomes = wait.until(condicao_esperada.visibility_of_all_elements_located(
        (By.XPATH, "//div[@class='detail-box']/a")))
    # 3- anotar preço
    precos = wait.until(condicao_esperada.visibility_of_all_elements_located(
        (By.XPATH, "//h6[@class='price_heading']")))
    # 4- anotar o link de onde foi extraído a info
    site = driver.current_url
    # 5- anotar o link da imagem
    links_imagem = wait.until(condicao_esperada.visibility_of_all_elements_located(
        (By.XPATH, "//div[@class='img-box']/img")))

    nome_iphone = nomes[0].text
    nome_gopro = nomes[1].text

    preco_iphone = precos[0].text.split(' ')[1]
    preco_gopro = precos[1].text.split(' ')[1]

    link_imagem_iphone = links_imagem[0].get_attribute('src')
    link_imagem_gopro = links_imagem[1].get_attribute('src')

    novo_produto(sql, conexao, nome_iphone, preco_iphone,
                 site, datetime.now(), link_imagem_iphone)
    novo_produto(sql, conexao, nome_gopro, preco_gopro,
                 site, datetime.now(), link_imagem_gopro)
    # 6- data da cotação


def varrer_site_2():
    # 1- Entrar no site https://site1produto.netlify.app
    driver, wait = iniciar_driver()
    driver.get(
        'https://www.kabum.com.br/cameras-e-drones/camera-digital/camera-de-acao/gopro')
    # 2-  Anotar o nome do produto
    nomes = wait.until(condicao_esperada.visibility_of_all_elements_located(
        (By.XPATH, "//span[@class='sc-d99ca57-0 cpPIRA sc-ff8a9791-16 dubjqF nameCard']")))
    # 3- anotar preço
    precos = wait.until(condicao_esperada.visibility_of_all_elements_located(
        (By.XPATH, "//span[@class='sc-3b515ca1-2 eqqhbT priceCard']")))
    # 4- anotar o link de onde foi extraído a info
    site = driver.current_url
    # 5- anotar o link da imagem
    links_imagem = wait.until(condicao_esperada.visibility_of_all_elements_located(
        (By.XPATH, "//img[@class='imageCard']")))

    nome_iphone = nomes[0].text
    nome_gopro = nomes[1].text

    preco_iphone = precos[0].text.split(' ')[1]
    preco_gopro = precos[1].text.split(' ')[1]

    link_imagem_iphone = links_imagem[0].get_attribute('src')
    link_imagem_gopro = links_imagem[1].get_attribute('src')

    novo_produto(sql, conexao, nome_iphone, preco_iphone,
                 site, datetime.now(), link_imagem_iphone)
    novo_produto(sql, conexao, nome_gopro, preco_gopro,
                 site, datetime.now(), link_imagem_gopro)


def varrer_site_3():
    pass


varrer_site_2()
# def rodar_tarefas():
#     varrer_site_1()


# # schedule.every().day.at('06:00').do(rodar_tarefas)
# schedule.every(30).seconds.do(rodar_tarefas)

# while True:
#     schedule.run_pending()
#     sleep(1)

# 3.33
