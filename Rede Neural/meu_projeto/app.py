from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

# Criar a instância da aplicação Flask
app = Flask(__name__)

# Carregar o modelo treinado (previamente salvo)
model = load_model("modelo_mnist.h5")

# Rota para servir a página inicial (index.html)
@app.route('/')
def home():
    return render_template('index.html')  # Carrega a página HTML principal

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Log para verificar se o arquivo foi enviado corretamente
        print("Arquivos recebidos:", request.files)  # Deve conter {'file': <FileStorage>}

        img_file = request.files['file']  # Tentar pegar o arquivo do formulário

        print(f"Nome do arquivo recebido: {img_file.filename}")  # Log do nome do arquivo recebido

        # Tentar abrir a imagem
        img = Image.open(img_file.stream)
        print("Imagem aberta com sucesso.")

        # Pré-processamento da imagem
        img = img.convert('L')  # Converte para escala de cinza
        print("Imagem convertida para escala de cinza.")

        img = img.resize((28, 28))  # Redimensiona para 28x28
        print("Imagem redimensionada para 28x28.")

        # Inverter cores, se necessário (fundo branco -> preto)
        img = np.array(img)
        if np.mean(img) > 127:  # Verifica se o fundo é claro
            img = 255 - img  # Inverte as cores
            print("Cores invertidas: fundo branco transformado em preto e vice-versa.")

        img = img / 255.0  # Normaliza os valores dos pixels
        print("Imagem normalizada.")

        img = img.reshape(1, 28, 28)  # Adiciona uma dimensão extra para o batch
        print(f"Forma da imagem pré-processada: {img.shape}")

        # Fazer a previsão
        prediction = model.predict(img)
        predicted_digit = np.argmax(prediction)
        print(f"Dígito previsto: {predicted_digit}")

        # Retornar o resultado como JSON
        return jsonify({'digit': int(predicted_digit)})

    except Exception as e:
        # Log detalhado do erro
        print(f"Erro durante o processamento: {e}")
        return jsonify({'error': str(e)}), 400

# Executar o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
