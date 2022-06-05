from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests, re

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('HOME.html')

@app.route('/vagas')
def pag_vagas():
    url_TI = 'https://www.bne.com.br/vagas-de-emprego-na-area-de-informatica?Area=Inform%C3%A1tica&Sort=0&Page=1'
    i = 'https://www.bne.com.br'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79'} 
    site_1 = requests.get(url_TI, headers = headers)
    soup_1 = BeautifulSoup(site_1.content, 'html.parser')

    url_1 = 'https://www.bne.com.br/vagas-de-emprego-na-area-de-marketing?Area=Marketing&Sort=0&Page=1'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79'} 
    site_2 = requests.get(url_1, headers = headers)
    soup_2 = BeautifulSoup(site_2.content, 'html.parser')

    url_2 = 'https://www.bne.com.br/vagas-de-emprego'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79'} 
    site_3 = requests.get(url_2, headers = headers)
    soup_3 = BeautifulSoup(site_3.content, 'html.parser')

    url_3 = 'https://www.bne.com.br/vagas-de-emprego-na-area-de-mecanico?Area=Mec%C3%A2nico&Sort=0&Page=1'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79'} 
    site_4 = requests.get(url_3, headers = headers)
    soup_4 = BeautifulSoup(site_4.content, 'html.parser')

    url_TI_2 = 'https://www.bne.com.br/vagas-de-emprego/?Page=4&Area=Inform%C3%A1tica&Sort=0'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79'} 
    site_5 = requests.get(url_TI_2, headers = headers)
    soup_5 = BeautifulSoup(site_5.content, 'html.parser')

    vagas_TI = soup_1.find_all('div', {'id': re.compile('job-.*')})
    vagas_1 = soup_2.find_all('div', {'id': re.compile('job-.*')})
    vagas_2 = soup_3.find_all('div', {'id': re.compile('job-.*')})
    vagas_3 = soup_4.find_all('div', {'id': re.compile('job-.*')})
    vagas_TI_2 = soup_5.find_all('div', {'id': re.compile('job-.*')})
    
    return render_template('VAGAS.html', vagas_TI=vagas_TI, vagas_1=vagas_1, vagas_2=vagas_2, vagas_3=vagas_3, vagas_TI_2=vagas_TI_2, i=i)

@app.route('/cursos')
def pag_cursos():
    return render_template('CURSOS.html')

@app.route('/métricas')
def pag_métricas():
    return render_template('MÉTRICAS.html')

@app.route('/localização')
def pag_localização():
    url = 'https://www.bne.com.br/vagas-de-emprego-na-area-de-informatica?Area=Inform%C3%A1tica&Sort=0&Page=1'
    i = 'https://www.bne.com.br'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79'}
    site = requests.get(url, headers = headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    
    url_1 = 'https://www.bne.com.br/vagas-de-emprego-na-area-de-marketing?Area=Marketing&Sort=0&Page=1'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79'} 
    site_2 = requests.get(url_1, headers = headers)
    soup_2 = BeautifulSoup(site_2.content, 'html.parser')

    url_2 = 'https://www.bne.com.br/vagas-de-emprego'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79'} 
    site_3 = requests.get(url_2, headers = headers)
    soup_3 = BeautifulSoup(site_3.content, 'html.parser')

    url_3 = 'https://www.bne.com.br/vagas-de-emprego-na-area-de-mecanico?Area=Mec%C3%A2nico&Sort=0&Page=1'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79'} 
    site_4 = requests.get(url_3, headers = headers)
    soup_4 = BeautifulSoup(site_4.content, 'html.parser')

    url_TI_2 = 'https://www.bne.com.br/vagas-de-emprego/?Page=4&Area=Inform%C3%A1tica&Sort=0'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79'} 
    site_5 = requests.get(url_TI_2, headers = headers)
    soup_5 = BeautifulSoup(site_5.content, 'html.parser')

    vagas_TI = soup.find_all('div', {'id': re.compile('job-.*')})
    vagas_1 = soup_2.find_all('div', {'id': re.compile('job-.*')})
    vagas_2 = soup_3.find_all('div', {'id': re.compile('job-.*')})
    vagas_3 = soup_4.find_all('div', {'id': re.compile('job-.*')})
    vagas_TI_2 = soup_5.find_all('div', {'id': re.compile('job-.*')})
    
    return render_template('LOCALIZAÇÃO.html', vagas_TI=vagas_TI, vagas_1=vagas_1, vagas_2=vagas_2, vagas_3=vagas_3, vagas_TI_2=vagas_TI_2, i=i)

if __name__ == '__main__':
    app.run()