# 🕷️ Raspagem de Dados

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green?style=flat-square&logo=selenium)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-4.x-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=flat-square)

> Sistema Inteligente de Raspagem e Monitoramento de Dados Web com Python

---

## 📖 Sobre o Projeto

O **WebScraper Monitor** é um projeto de raspagem de dados (_web scraping_) desenvolvido em Python, que combina duas abordagens distintas de coleta de informações:

- **Leitura local com BeautifulSoup:** análise e extração de dados diretamente de um arquivo HTML local, processando a estrutura da página do próprio projeto.
- **Monitoramento dinâmico com Selenium:** acesso automatizado a um e-commerce real na internet para rastrear variações de preço de produtos específicos ao longo do tempo.

Este projeto foi desenvolvido com foco em:

- Raspagem de dados (_Web Scraping_)
- Automação de navegadores
- Processamento e análise de HTML
- Monitoramento de preços em tempo real
- Engenharia da Computação
- Internet das Coisas e coleta de dados

---

## 🎯 Objetivos

- Demonstrar o uso prático de BeautifulSoup para leitura e parsing de HTML local;
- Automatizar a navegação em páginas web dinâmicas com Selenium;
- Monitorar alterações de preço de produtos em e-commerces;
- Registrar e comparar os dados coletados ao longo do tempo;
- Servir como projeto acadêmico e educacional na área de coleta de dados;
- Possibilitar futuras expansões, como alertas automáticos e dashboards.

---

## ⚙️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.10+ | Linguagem de Programação |
| BeautifulSoup4 | Parsing de HTML/XML |
| Selenium | Automação de Navegador |
| WebDriver (Chrome/Firefox) | Controle do Navegador |
| Requests | Requisições HTTP |

---

## 🏗️ Arquitetura do Sistema

```
         ┌────────────────────────────┐
         │      Entrada de Dados      │
         └────────────┬───────────────┘
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
  ┌───────────────┐     ┌──────────────────┐
  │  HTML Local   │     │  E-commerce Web  │
  │  (Arquivo)    │     │  (Internet)      │
  └───────┬───────┘     └────────┬─────────┘
          │                      │
          ▼                      ▼
  ┌───────────────┐     ┌──────────────────┐
  │ BeautifulSoup │     │    Selenium      │
  │  (Parsing)    │     │  (Navegação)     │
  └───────┬───────┘     └────────┬─────────┘
          │                      │
          └──────────┬───────────┘
                     │
                     ▼
          ┌──────────────────────┐
          │  Extração dos Dados  │
          └──────────┬───────────┘
                     │
          ┌──────────┴───────────┐
          │                      │
          ▼                      ▼
  ┌───────────────┐     ┌──────────────────┐
  │  Exibição no  │     │  Armazenamento   │
  │   Terminal    │     │  (JSON / CSV)    │
  └───────────────┘     └──────────────────┘
                            futuramente...
```

---

## ✨ Funcionalidades

### 🔵 Módulo 1 — BeautifulSoup (HTML Local)

- ✅ Leitura de arquivo HTML local diretamente do projeto
- ✅ Parsing completo da estrutura da página
- ✅ Extração de títulos, textos, links e outros elementos
- ✅ Navegação pela árvore de tags HTML
- ✅ Exportação dos dados extraídos

### 🟢 Módulo 2 — Selenium (E-commerce Web)

- ✅ Acesso automatizado a página de produto em e-commerce
- ✅ Localização dinâmica do preço na página
- ✅ Detecção e registro de variações de preço
- ✅ Comparação com valores previamente registrados
- ✅ Histórico de monitoramento com data e hora
- ✅ Compatibilidade com Chrome e Firefox via WebDriver

---

## 📂 Estrutura do Projeto

```
raspagem-de-dados/
│
├── beautifulSoup.py
│
├── selenuim.py
│
├── index.html   
│
├── images/
│   ├── mouse.png
│   ├── notebook.png
│   └── teclado.png
│
└── README.md
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.10 ou superior instalado
- Google Chrome ou Firefox instalado
- ChromeDriver ou GeckoDriver compatível com seu navegador
- Pip para instalação das dependências

### Instalação

**1. Clone o repositório:**

```bash
git clone https://github.com/GabrielaSouzaDev/raspagem-de-dados.git
cd raspagem-de-dados
```

**2. Instale as bibliotecas necessárias**
```
pip install beautifulsoup4
pip install selenium
pip install requests
pip install webdriver-manager
```

**3. Execute o projeto:**

```bash
# Executa apenas o módulo BeautifulSoup (local)
python beautifulSoup.py

# Executa apenas o módulo Selenium (web)
python selenium.py
```

---

## 📊 Exemplo de Saída

### Módulo BeautifulSoup — HTML Local

```
===== LEITURA LOCAL (BeautifulSoup) =====
Arquivo: index.html
Título da Página : Loja Virtual 
===============================
Produto: Notebook Gamer 
Preço: R$ 4500
===============================
Produto: Mouse RGB 
Preço: R$ 120
===============================
Produto: Teclado USB 
Preço: R$ 350
```

### Módulo Selenium — Monitoramento de Preço

```
===== MONITORAMENTO DE PREÇO (Selenium) =====
Produto    : Notebook Dell Inspiron 15
URL        : https://www.ecommerce.com.br/produto/notebook-dell

Preço Atual    : R$ 3.499,90
```

---

## 🔄 Como Funciona — Passo a Passo

### BeautifulSoup (Módulo Local)

1. O script lê o arquivo `index.html` presente no diretório do projeto
2. O BeautifulSoup faz a analise do conteúdo HTML
3. São extraídos os elementos desejados (tags, textos, atributos)
4. Os dados são exibidos no terminal e exportados

### Selenium (Módulo Web)

1. O Selenium abre um navegador automaticamente (Chrome ou Firefox)
2. Acessa a URL do produto no e-commerce configurado
3. Aguarda o carregamento completo da página (incluindo JavaScript)
4. Localiza o elemento de preço via seletor CSS ou XPath
5. Compara o valor atual com o último registrado
6. Salva o novo valor com data e hora no histórico

---

## 🔮 Melhorias Futuras

- Integração com envio de alertas por e-mail ou Telegram
- Dashboard Web para visualização do histórico de preços
- Suporte a múltiplos produtos e múltiplos e-commerces simultaneamente
- Agendamento automático de execuções periódicas
- Armazenamento em banco de dados (SQLite / PostgreSQL)
- Relatórios automáticos em PDF
- Detecção de captcha e estratégias de contorno
- Integração com Inteligência Artificial para previsão de preços

---

## 🎓 Aplicações Educacionais

Este projeto pode ser utilizado em disciplinas como:

- Web Scraping e Coleta de Dados
- Automação com Python
- Análise e Processamento de HTML
- Internet das Coisas (IoT) e Monitoramento


## ⚠️ Aviso Legal

Este projeto foi desenvolvido para fins **educacionais e acadêmicos**. Ao utilizar técnicas de web scraping, o usuário deve:

- Verificar os **Termos de Uso** do site alvo antes de realizar qualquer raspagem
- Respeitar o arquivo **`robots.txt`** dos sites
- Não sobrecarregar servidores com requisições excessivas
- Utilizar os dados coletados de forma ética e responsável

---

## 📜 Licença

Este projeto é distribuído sob a licença **MIT**.


---

## 👨‍💻 **Autor**

Projeto desenvolvido por Gabriela Souza.

O sistema foi criado com o objetivo de aplicar conceitos de programação, raspagem de dados, automação de navegadores e análise de HTML através do desenvolvimento de um sistema de monitoramento de preços utilizando Python.

---

> 🚀 **Projeto Acadêmico**
