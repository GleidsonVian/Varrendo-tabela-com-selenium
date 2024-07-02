from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Inicie o navegador
driver = webdriver.Chrome()

# Navegue para a página
driver.get("https://br.investing.com/commodities/crude-oil-historical-data")

# Aguarde até que a tabela esteja presente na página
wait = WebDriverWait(driver, 10)
tabela_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'freeze-column-w-1')))

# Encontre a tabela e extraia os dados
dadosTabela = tabela_element.find_element(By.TAG_NAME, 'tbody')
dados = []
for linha in dadosTabela.find_elements(By.TAG_NAME, 'tr'):
    linhaDados = []
    for coluna in linha.find_elements(By.TAG_NAME, 'td'):
        linhaDados.append(coluna.text)
    dados.append(linhaDados)

# Crie o DataFrame
df = pd.DataFrame(dados)

# Defina a primeira linha como cabeçalho
df.columns = df.iloc[0]
df = df[1:]
# Definindo as colunas da tabela
df.columns = ['Data', 'Ultimo', 'Abertura', 'Maxima', 'Minima', 'Vol', 'Var%']

df.to_excel('dados.xlsx')

# Feche o navegador
driver.quit()
