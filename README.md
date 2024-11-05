# Baixador de Imagens com Flask

Este projeto é uma aplicação web em Flask que permite ao usuário buscar e baixar todas as imagens de uma página da web. Além disso, a aplicação exibe uma barra de progresso em tempo real, indicando o status de download de cada imagem.

## Funcionalidades

- **Busca de Imagens**: A aplicação obtém automaticamente todos os URLs das imagens em uma página web fornecida.
- **Download das Imagens**: Baixa cada imagem encontrada e armazena na pasta `imagens_baixadas`.
- **Barra de Progresso**: Exibe o progresso do download em tempo real.
- **Tratamento de Nomes de Arquivo**: Os nomes das imagens são processados para remover caracteres inválidos.

## Requisitos

- Python 3.6 ou superior
- Flask
- Requests
- BeautifulSoup4

## Para instalar as dependências, execute:

```bash
pip install flask requests beautifulsoup4
pip install -r requirements.txt

## Execute o aplicativo Flask:
python app.py

## Estrutura do Projeto
- app.py: Código principal da aplicação Flask.
- templates/index.html: Página HTML para interface do usuário.
- static/: Pasta onde podem ser armazenados arquivos estáticos, como CSS para estilização da barra de progresso.
- imagens_baixadas/: Pasta gerada automaticamente para armazenar as imagens baixadas.


Esse `README.md` está formatado para o GitHub e fornece uma visão clara do projeto e de como usá-lo. Edite o link do repositório e o autor conforme necessário.
https://github.com/acfarias81/DownloadsFotosPy.git

## Desenvolvido por Antonio Farias
