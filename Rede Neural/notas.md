# Explicação das Bibliotecas Utilizadas no Projeto

## 1. Flask
   - **O que é**: Flask é um micro-framework para o desenvolvimento de aplicações web em Python. Ele permite a criação de servidores web, APIs RESTful, e manipulação de requisições HTTP.
   - **Por que usou**: No seu projeto, o Flask foi usado para criar o servidor que recebe a imagem do dígito manuscrito, faz a previsão usando o modelo de rede neural, e retorna o resultado para o usuário via API.

## 2. TensorFlow
   - **O que é**: TensorFlow é uma biblioteca de código aberto para computação numérica, especializada em criar e treinar modelos de aprendizado de máquina, incluindo redes neurais profundas (deep learning).
   - **Por que usou**: Você usou o TensorFlow para carregar o modelo de rede neural treinado (`modelo_mnist.h5`) e para fazer a previsão do dígito manuscrito a partir da imagem recebida.

## 3. Keras
   - **O que é**: Keras é uma API de alto nível para construção e treinamento de modelos de deep learning, que roda sobre bibliotecas como TensorFlow. Ela facilita o processo de criação e treinamento de redes neurais.
   - **Por que usou**: O Keras foi utilizado (via TensorFlow) para definir, compilar e treinar o modelo de rede neural que foi salvo em `modelo_mnist.h5`.

## 4. NumPy
   - **O que é**: NumPy é uma biblioteca fundamental para computação científica em Python. Ela oferece suporte para arrays multidimensionais e funções matemáticas eficientes para operações numéricas.
   - **Por que usou**: Você usou o NumPy para manipulação de dados numéricos, como normalizar a imagem de entrada e formatá-la para ser compatível com o modelo de rede neural.

## 5. Pillow (PIL)
   - **O que é**: Pillow é uma biblioteca de processamento de imagens em Python, que é uma versão mais moderna e mantida da antiga biblioteca Python Imaging Library (PIL).
   - **Por que usou**: Você usou o Pillow para abrir, redimensionar, e converter a imagem do dígito manuscrito para escala de cinza antes de processá-la no modelo de rede neural.
