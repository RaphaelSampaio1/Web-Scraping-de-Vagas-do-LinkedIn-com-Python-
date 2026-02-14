# Web-Scraping-de-Vagas-do-LinkedIn-com-Python

Este projeto faz o scraping de vagas de emprego do LinkedIn (modo público, sem login) e salva os resultados em um arquivo CSV **linha a linha**, em tempo real, usando:

- `requests`
- `BeautifulSoup`
- `pandas`
- `time`
- `os`

O objetivo é ser **didático para iniciantes** e, ao mesmo tempo, mostrar boas práticas de automação como:
- Uso de `User-Agent` para evitar bloqueios
- Delay entre requisições
- Salvamento incremental em CSV (não perder dados se o script parar)

> 🔴 Todo o passo a passo está explicado em vídeo no meu canal do YouTube:  
> 👉 [SampaioDev](https://www.youtube.com/@SampaioDev)

> 👨‍💻 Me acompanhe também no LinkedIn:  
> 👉 [Raphael Sampaio](https://www.linkedin.com/in/raphaelssampaio/)

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- `requests`
- `beautifulsoup4`
- `pandas`

---

## 📦 Instalação

```bash
pip install requests beautifulsoup4 pandas

⚙️ Como funciona
Acessa a URL pública de vagas do LinkedIn (sem login) para a busca por python:
https://www.linkedin.com/jobs/search/?keywords=python
Usa um User-Agent customizado para simular um navegador real.
Faz o parsing do HTML com BeautifulSoup.
Encontra os cards de vagas por meio das classes:
div.base-card
h3.base-search-card__title (título da vaga)
h4.base-search-card__subtitle (empresa)
span.job-search-card__location (localização)
a.base-card__full-link (link da vaga)
time (data de postagem, quando disponível)
A cada vaga extraída, adiciona imediatamente uma linha no CSV:
vagas_linkedin_incremental.csv
Usa time.sleep(1) entre cada extração para reduzir risco de bloqueio e deixar o processo mais transparente para fins didáticos/vídeo.
🧾 Estrutura do CSV

O arquivo vagas_linkedin_incremental.csv possui as seguintes colunas:

titulo
empresa
localizacao
link
data_postagem
📉 Performance e Limitações

Este script foi desenhado com foco em didática e segurança, não em máxima performance.

Pontos fortes ✅
Salvamento incremental: se o script for interrompido, os dados já extraídos não são perdidos.
Baixo acoplamento: código simples, fácil de adaptar para outros sites.
Transparência: logs no console mostram o que está sendo extraído em tempo real.
Limitações ⚠️
O LinkedIn muda frequentemente a estrutura do HTML e as classes CSS.
Se as classes base-card, base-search-card__title etc. mudarem, será necessário atualizar os seletores.
O site utiliza carregamento dinâmico (infinite scroll) para mais vagas:
Este exemplo trabalha apenas com a primeira leva de resultados do HTML inicial.
Para scraping avançado/paginação infinita, o ideal seria usar Selenium, Playwright ou soluções mais robustas.
O LinkedIn tem proteções contra automação:
Mesmo com User-Agent e delay, acessos excessivos podem causar bloqueios temporários (429 ou 403).

Este projeto é ideal como material educacional e prova de conceito, não como coletor massivo de dados em produção.

▶️ Como executar
python linkedin_scraper.py


Ao rodar o script, você verá no console algo como:

--- Iniciando acesso ao LinkedIn ---
Arquivo criado: vagas_linkedin_incremental.csv
Vagas encontradas na página: 15
[1] Salvando: Python Developer | Empresa X | Lisboa, Portugal
     Link: https://www.linkedin.com/jobs/view/123456789/
[2] Salvando: Data Engineer | Empresa Y | Porto, Portugal
     Link: ...
...
--- Finalizado. Confira o arquivo: vagas_linkedin_incremental.csv ---


Enquanto o script roda, você pode abrir o CSV no Excel/LibreOffice/Google Sheets e ver as linhas sendo preenchidas em tempo real.

📺 Conteúdo em Vídeo

Todo esse conteúdo, com explicação passo a passo, está disponível no meu canal:

YouTube: SampaioDev

Se este projeto te ajudou, deixa um like no vídeo e se inscreve no canal. Isso me ajuda muito a continuar produzindo conteúdo prático sobre:

Automação
Python
RPA
Carreira em tecnologia
🌐 Autor

Raphael Sampaio

LinkedIn: https://www.linkedin.com/in/raphaelssampaio/
YouTube: https://www.youtube.com/@SampaioDev

---

### README em Inglês (para o mesmo repositório)

Você pode colocar logo abaixo do PT-BR no mesmo `README.md` ou em uma seção separada.

```markdown
---

# Web Scraping LinkedIn Jobs with Python 🐍💼

This project scrapes public LinkedIn job listings (no login required) and saves them to a CSV file **line by line**, in real time, using:

- `requests`
- `BeautifulSoup`
- `pandas`
- `time`
- `os`

The goal is to be **beginner-friendly** while still showing good automation practices such as:
- Using a custom `User-Agent` to reduce blocking
- Adding delay between requests
- Incremental CSV saving (so you don't lose data if the script stops)

> 🔴 The full step-by-step explanation is available on my YouTube channel:  
> 👉 [SampaioDev](https://www.youtube.com/@SampaioDev)

> 👨‍💻 Connect with me on LinkedIn:  
> 👉 [Raphael Sampaio](https://www.linkedin.com/in/raphaelssampaio/)

---

## 🚀 Tech Stack

- Python 3.x
- `requests`
- `beautifulsoup4`
- `pandas`

---

## 📦 Installation

```bash
pip install requests beautifulsoup4 pandas

⚙️ How it works
Accesses the public LinkedIn jobs URL (no login) for the python keyword:
https://www.linkedin.com/jobs/search/?keywords=python
Uses a custom User-Agent header to simulate a real browser.
Parses the HTML with BeautifulSoup.
Finds job cards using these CSS classes:
div.base-card (job card container)
h3.base-search-card__title (job title)
h4.base-search-card__subtitle (company name)
span.job-search-card__location (location)
a.base-card__full-link (job URL)
time (posting date, when available)
For each extracted job, immediately appends a new row to the CSV file:
vagas_linkedin_incremental.csv
Uses time.sleep(1) between each extraction to reduce the risk of being blocked and to make the process more transparent for educational/video purposes.
🧾 CSV Structure

The vagas_linkedin_incremental.csv file contains the following columns:

titulo (job title)
empresa (company)
localizacao (location)
link (job URL)
data_postagem (posting date)

You can easily rename these columns to English if you prefer; I kept them in Portuguese to match my YouTube audience.

📉 Performance & Limitations

This script is designed with education and safety in mind, not maximum performance.

Strengths ✅
Incremental saving: if the script crashes or is interrupted, all previously extracted data is already stored.
Simple and low-coupled: easy to understand and adapt for other websites.
Transparent: console logs show exactly what is being extracted in real time.
Limitations ⚠️
LinkedIn frequently changes its HTML structure and CSS classes.
If classes like base-card or base-search-card__title change, the selectors must be updated.
The site uses infinite scroll for more job results:
This script only handles the initial batch of results from the first HTML response.
For advanced scraping / full pagination, you would likely need tools like Selenium or Playwright.
LinkedIn has anti-bot protections:
Even with User-Agent and delays, heavy or frequent scraping may lead to temporary blocks (429 or 403).

This project is best used as educational material and a proof of concept, not as a high-scale data collector in production.

▶️ Usage
python linkedin_scraper.py


When running the script, you will see logs like:

--- Iniciando acesso ao LinkedIn ---
Arquivo criado: vagas_linkedin_incremental.csv
Vagas encontradas na página: 15
[1] Salvando: Python Developer | Empresa X | Lisboa, Portugal
     Link: https://www.linkedin.com/jobs/view/123456789/
[2] Salvando: Data Engineer | Empresa Y | Porto, Portugal
     Link: ...
...
--- Finalizado. Confira o arquivo: vagas_linkedin_incremental.csv ---


You can open the CSV file in Excel/LibreOffice/Google Sheets while the script is running and watch the rows being added in real time.

📺 Video Content

The complete tutorial, with live coding and detailed explanation, is available on my YouTube channel:

YouTube: SampaioDev

If this project helped you, please consider liking the video and subscribing to the channel. It really helps me keep producing practical content about:

Automation
Python
RPA
Tech career
🌐 Author

Raphael Sampaio

LinkedIn: https://www.linkedin.com/in/raphaelssampaio/
YouTube: https://www.youtube.com/@SampaioDev


Se quiser, no próximo passo eu escrevo também a descrição do vídeo do YouTube já com título, tags e call to action bem agressivo pra retenção.
