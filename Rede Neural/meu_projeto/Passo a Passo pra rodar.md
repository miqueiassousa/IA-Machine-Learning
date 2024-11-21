### Passo a Passo para Rodar o Projeto

#### 1. Configuração do Ambiente Virtual:

- Crie um ambiente virtual:
```bash
    python -m venv venv
```

- Ative o ambiente virtual:
    - No PowerShell (Windows):
        ```bash
        .\venv\Scripts\Activate.ps1
        ```

#### 2. Instalar Dependências:

- Instale as bibliotecas necessárias dentro do ambiente virtual:
```bash
    pip install flask tensorflow numpy pillow
```

#### 3. Gerar o Modelo Treinado:

- Execute o script `mnist_classification.py` para treinar a rede neural e gerar o arquivo `modelo_mnist.h5`.
```bash
    python mnist_classification.py
````

#### 4. Rodar o Servidor Flask:

- Execute o script `app.py` para iniciar o servidor Flask que irá processar as imagens enviadas.
```bash
    python app.py
```

#### 5. Testar a Aplicação:

- Acesse a aplicação no navegador:
```
http://127.0.0.1:5000
```

- Faça o upload de uma imagem de dígito manuscrito e veja o resultado da previsão.
