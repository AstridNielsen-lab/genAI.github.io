import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar-imagem', methods=['POST'])
def gerar_imagem():
    prompt = request.form['prompt']
    url = f'https://aiimage.hellonepdevs.workers.dev/?prompt={prompt}'

    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            image_url = data.get('image_url')
            return jsonify({'image_url': image_url})
        except ValueError:
            return jsonify({'error': 'Erro ao decodificar a resposta da API.'})
    else:
        return jsonify({'error': 'Erro ao chamar a API.'})

if __name__ == '__main__':
    app.run(debug=True)
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar-imagem', methods=['POST'])
def gerar_imagem():
    prompt = request.form['prompt']
    url = f'https://aiimage.hellonepdevs.workers.dev/?prompt={prompt}'

    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            image_url = data.get('image_url')
            return jsonify({'image_url': image_url})
        except ValueError:
            return jsonify({'error': 'Erro ao decodificar a resposta da API.'})
    else:
        return jsonify({'error': 'Erro ao chamar a API.'})

if __name__ == '__main__':
    app.run(debug=True)
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar-imagem', methods=['POST'])
def gerar_imagem():
    prompt = request.form['prompt']
    url = f'https://aiimage.hellonepdevs.workers.dev/?prompt={prompt}'

    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            image_url = data.get('image_url')
            return jsonify({'image_url': image_url})
        except ValueError:
            return jsonify({'error': 'Erro ao decodificar a resposta da API.'})
    else:
        return jsonify({'error': 'Erro ao chamar a API.'})

if __name__ == '__main__':
    app.run(debug=True)
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar-imagem', methods=['POST'])
def gerar_imagem():
    prompt = request.form['prompt']
    url = f'https://aiimage.hellonepdevs.workers.dev/?prompt={prompt}'

    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            image_url = data.get('image_url')
            return jsonify({'image_url': image_url})
        except ValueError:
            return jsonify({'error': 'Erro ao decodificar a resposta da API.'})
    else:
        return jsonify({'error': 'Erro ao chamar a API.'})

if __name__ == '__main__':
    app.run(debug=True)
