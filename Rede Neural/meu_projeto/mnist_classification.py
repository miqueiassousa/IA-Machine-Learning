# Importar as bibliotecas necessárias
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Carregar o conjunto de dados MNIST (dígitos manuscritos)
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar os dados (transformar de 0-255 para 0-1)
x_train, x_test = x_train / 255.0, x_test / 255.0

# Converter os rótulos para uma representação de one-hot encoding
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Definir o modelo da rede neural
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Achatar a imagem 28x28 para um vetor de 784 elementos
    layers.Dense(128, activation='relu'),  # Primeira camada oculta
    layers.Dense(10, activation='softmax')  # Camada de saída com 10 neurônios (um para cada dígito)
])

# Compilar o modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Treinar o modelo
model.fit(x_train, y_train, epochs=10, batch_size=128)

# Avaliar o modelo no conjunto de testes
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"Acurácia no conjunto de teste: {test_accuracy:.2f}")

# Salvar o modelo treinado em um arquivo .h5
model.save("modelo_mnist.h5")
print("Modelo salvo com sucesso!")
