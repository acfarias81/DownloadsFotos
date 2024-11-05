from flask import Flask, render_template, request, jsonify, Response
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import re

app = Flask(__name__)
progresso_atual = 0  # Variável global para rastrear o progresso

# Função para buscar URLs das imagens
def obter_urls_imagens(url):
    resposta = requests.get(url)
    if resposta.status_code != 200:
        return []

    sopa = BeautifulSoup(resposta.text, "html.parser")
    imagens = sopa.find_all("img")
    
    urls_imagens = [urljoin(url, img.get("src")) for img in imagens]
    return urls_imagens

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para obter URLs das imagens
@app.route('/obter_imagens', methods=['POST'])
def obter_imagens():
    global progresso_atual
    progresso_atual = 0  # Reseta o progresso a cada novo download
    url = request.form['url']
    urls_imagens = obter_urls_imagens(url)
    return jsonify(urls_imagens)

# Rota para baixar cada imagem e atualizar o progresso
@app.route('/baixar_imagens', methods=['POST'])
def baixar_imagens():
    global progresso_atual
    urls_imagens = request.json['urls_imagens']
    total = len(urls_imagens)
    pasta = "imagens_baixadas"
    
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    for i, img_url in enumerate(urls_imagens):
        try:
            img_resposta = requests.get(img_url)
            img_resposta.raise_for_status()
            
            # Limpa o nome do arquivo removendo caracteres inválidos
            nome_arquivo = os.path.join(pasta, re.sub(r'[\\/*?:"<>|]', "", img_url.split("/")[-1]))
            with open(nome_arquivo, "wb") as file:
                file.write(img_resposta.content)
            
            progresso_atual = ((i + 1) / total) * 100  # Atualiza o progresso
            
        except requests.exceptions.RequestException:
            continue

    progresso_atual = 100  # Garante que o progresso chega a 100% no final
    return jsonify({"status": "completo"})

# Rota SSE para enviar progresso
@app.route('/progresso')
def progresso():
    def enviar_progresso():
        global progresso_atual
        while progresso_atual < 100:
            yield f"data: {progresso_atual}\n\n"
            time.sleep(0.5)
        yield "data: 100\n\n"  # Garante que chega a 100 no final

    return Response(enviar_progresso(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
