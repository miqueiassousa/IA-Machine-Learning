 # Regressão linear 

 A regressão linear é um dos métodos mais simples e fundamentais de inteligência artificial e aprendizado de máquina. Seu objetivo é encontrar a relação entre variáveis de forma a prever ou estimar um valor baseado em dados históricos.
 
 IA com aprendizado supervisionado usando um modelo de regressão linear para prever o valor de uma casa com base no número de cômodos. Esse exemplo será feito em português e no Jupyter Notebook, usando dados fictícios para simplificação.

```bash 
!pip install scikit-learn pandas matplotlib  # Bibliotecas necessárias.
```

### Conceitos das bibliotecas:

- *Scikit-Learn*: Constroe e avalia os modelos de aprendizado de máquina e realiza tarefas de pré-processamento.
- *Pandas*: Manipulação e análise de dados
- *matplotlib*: Visualização de dados

Essas três bibliotecas são frequentemente usadas juntas para construir um fluxo de trabalho completo de machine learning. Aqui está um exemplo típico de integração:

- Pandas para carregar e limpar os dados.
- Matplotlib para visualizar os dados e entender as relações entre as variáveis.
- Scikit-Learn para treinar e avaliar modelos de machine learning, utilizando os dados processados com pandas.

# Exemplo de Regressão Linear com Python

Este exemplo usa **regressão linear** para prever o salário de uma pessoa com base na sua experiência de trabalho (em anos). Vamos utilizar Python e a biblioteca **Scikit-Learn**.

Certifique-se de ter as bibliotecas necessárias instaladas:

```python

# Passo 1: Instalar as Bibliotecas
!pip install scikit-learn pandas matplotlib

# Passo 2: Importar as Bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Passo 3: Criar um Conjunto de Dados Fictício de experiência e salário
dados = {
    'experiencia': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'salario': [30000, 35000, 40000, 50000, 60000, 65000, 70000, 75000, 85000, 90000]
}
df = pd.DataFrame(dados)

# Exibir as primeiras linhas dos dados
df.head()

# Passo 4: Visualizar os Dados
plt.scatter(df['experiencia'], df['salario'], color='red')
plt.xlabel("Experiência (anos)")
plt.ylabel("Salário (R$)")
plt.title("Experiência vs. Salário")
plt.show

# Passo 5: Dividir os Dados
X = df[['experiencia']]  # Variável independente (experiência)
y = df['salario']        # Variável dependente (salário)

# Dividir em 80% para treino e 20% para teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Passo 6: Criar e Treinar o Modelo

# Criando o modelo de regressão linear
modelo = LinearRegression()

# Treinando o modelo com os dados de treino
modelo.fit(X_train, y_train)

# Passo 7: Prever e Avaliar o Modelo

# Fazer previsões com os dados de teste
y_pred = modelo.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Erro Quadrado Médio (MSE):", mse)
print("Coeficiente de Determinação (R^2):", r2)

# Passo 7: Visualizar o Ajuste da Regressão
# Plotar os dados e a linha de regressão
plt.scatter(df['experiencia'], df['salario'], color='blue', label="Dados Reais")
plt.plot(df['experiencia'], modelo.predict(df[['experiencia']]), color='red', label="Linha de Regressão")
plt.xlabel("Experiência (anos)")
plt.ylabel("Salário (R$)")
plt.title("Regressão Linear - Experiência vs. Salário")
plt.legend()
plt.show()


