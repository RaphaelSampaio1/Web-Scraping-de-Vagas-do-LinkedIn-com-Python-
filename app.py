from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import os
import requests

import requests

# Configurações
url = "https://www.linkedin.com/jobs/search/?keywords=python"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

csv_file = "linkedin_jobs.csv"

def initialize_csv():
    if not os.path.exists(csv_file):
        df = pd.DataFrame(columns=["Título", "Empresa", "Localização", "Data de Publicação"])
        df.to_csv(csv_file, index=False)
        print(f"Arquivo {csv_file} criado com sucesso.")

def append_row(job_dict):
    df = pd.DataFrame([job_dict])
    df.to_csv(csv_file, mode='a', header=False, index=False, encoding='utf-8')

def scrape_jobs():
    print("iniciando a raspagem de dados...")
    initialize_csv()

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Erro ao acessar a página: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, "html.parser")
    cards = soup.find_all("div", class_= "base-card" )

    print(f"Encontrados {len(cards)} empregos.")

    for i, card in enumerate(cards):
        try:
            title = card.find("h3", class_="base-search-card__title").get_text(strip=True)
            company = card.find("h4", class_="base-search-card__subtitle").get_text(strip=True)
            location = card.find("span", class_="job-search-card__location").get_text(strip=True)
            date_posted = card.find("time")["datetime"]

            job_dict = {
                "Título": title,
                "Empresa": company,
                "Localização": location,
                "Data de Publicação": date_posted
            }
            append_row(job_dict)
            print(f"Emprego {i+1} adicionado: {title} na {company}")
            sleep(0.5)  # Evita sobrecarregar o servidor
        except Exception as e:
            print(f"Erro ao processar o emprego {i+1}: {e}")

if __name__ == "__main__":
    scrape_jobs()