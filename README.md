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
