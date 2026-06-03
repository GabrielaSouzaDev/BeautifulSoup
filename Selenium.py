from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # aguarda o carregamento completo da página para não dar erro
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://www.amazon.com.br/Echo-Pop-Cor-Preta/dp/B09WXVH7WK/th=1"

driver.get(url)
print(driver.page_source)  # imprime o HTML da página recebida
time.sleep(5)

inteiro = driver.find_element(By.CLASS_NAME, "a-price-whole").text
decimal = driver.find_element(By.CLASS_NAME, "a-price-fraction").text

print(f'O preço do produto está em R${inteiro},{decimal}')

driver.quit()