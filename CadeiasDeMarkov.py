#Cadeias de Markov

import numpy as np
from datetime import datetime, timedelta

dia_atual = datetime.today()
states = ["Ensolarado", "Nublado", "Nublado com Sol", "Chuvoso", "Chuva Forte", "Tempestade"]

# Matriz de transição de estados
transition_matrix = [
    [0.6, 0.15, 0.1, 0.1, 0.03, 0.02],  # De "Ensolarado"
    [0.2, 0.5, 0.15, 0.1, 0.03, 0.02],  # De "Nublado"
    [0.3, 0.2, 0.3, 0.1, 0.05, 0.05],   # De "Nublado com Sol"
    [0.2, 0.15, 0.1, 0.4, 0.1, 0.05],   # De "Chuvoso"
    [0.15, 0.1, 0.05, 0.2, 0.4, 0.1],   # De "Chuva Forte"
    [0.1, 0.05, 0.03, 0.15, 0.3, 0.37]  # De "Tempestade"
]

# Estado Inicial
initial_state = "Nublado com Sol"

# Número de dias a prever
num_days = 15

# Função para encontrar o índice de um estado
def get_state_index(state) :
    return states.index(state)

# Função para prever o clima para os próximos dias

def predict_weather(initial_state, num_days) :
    current_state = initial_state
    forecast = [current_state]

    for _ in range (num_days - 1) :
        current_index = get_state_index(current_state)
        next_state = np.random.choice(
            states,
            p=transition_matrix[current_index]
        )

        forecast.append(next_state)
        current_state = next_state

    return forecast

# Realizar a previsão 
forecast = predict_weather(initial_state, num_days)

# Exibir a previsão
print(f"Estado inicial: {initial_state}")
print("Previsão para os próximos dias:")

for day, state in enumerate(forecast, start=1) :
    data_formatada = dia_atual.strftime("%d/%m/%Y")
    print(f"Dia {data_formatada}: {state}")
    dia_atual += timedelta(days=1)

