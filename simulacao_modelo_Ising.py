import numpy as np
import matplotlib.pyplot as plt
from numba import njit
import time



@njit
def criar_matriz(seed: int, tamanho: int) -> np.ndarray:
    """
    Cria uma matriz quadrada com spins aleatórios -1 ou 1.

    Args:
        seed (int): Semente para o gerador de números aleatórios, garantindo reprodutibilidade.
        tamanho (int): A dimensão da matriz (tamanho x tamanho).

    Returns:
        np.ndarray: Uma matriz de spins.
    """
    np.random.seed(seed)
    
    return np.random.choice(np.array([-1, 1]), size=(tamanho, tamanho))


@njit
def simular_monte_carlo(matriz: np.ndarray, passos: int, temperatura: float) -> np.ndarray:
    """
    Executa a simulação do Modelo de Ising usando o algoritmo de Metropolis.

    Args:
        matriz (np.ndarray): A matriz de spins inicial.
        passos (int): O número de inversões de spin a serem aceitas.
        temperatura (float): A temperatura do sistema em Celsius.

    Returns:
        np.ndarray: A matriz de spins após a simulação.
    """
    # Constante de Boltzmann em eV/K
    kb = 8.6173324e-5  
    kelvin = temperatura + 273.15
    tamanho = matriz.shape[0]
    aceitos = 0
    
    matriz_simulada = matriz.copy() # Cria uma cópia para não modificar a original

    while aceitos < passos:
        # 1. Escolhe um spin 
        i = np.random.randint(0, tamanho)
        j = np.random.randint(0, tamanho)

        # 2. Calcula a variação de energia se o spin for invertido
        spin = matriz_simulada[i, j]
        
        vizinhos = (
            matriz_simulada[(i - 1) % tamanho, j] +  # Vizinho acima
            matriz_simulada[(i + 1) % tamanho, j] +  # Vizinho abaixo
            matriz_simulada[i, (j - 1) % tamanho] +  # Vizinho à esquerda
            matriz_simulada[i, (j + 1) % tamanho]    # Vizinho à direita
        )
        delta_energia = 2 * spin * vizinhos

        # 3. Critério de Aceitação de Metropolis
        # Aceita a inversão se a energia diminuir (delta_energia <= 0)
        # ou, se a energia aumentar, aceita com uma probabilidade exponencial.
        if delta_energia <= 0 or np.random.rand() < np.exp(-delta_energia / (kb * kelvin)):
            matriz_simulada[i, j] *= -1  # Inverte o spin
            aceitos += 1

    return matriz_simulada


def mostrar_matriz(matriz: np.ndarray, titulo: str):
    """
    Mostra uma visualização gráfica da matriz de spins.
    
    Args:
        matriz (np.ndarray): A matriz a ser visualizada.
        titulo (str): O título do gráfico.
    """
    # Define mapa de cores: preto para -1, branco para 1
    cmap = plt.cm.colors.ListedColormap(['black', 'white'])
    
    plt.imshow(matriz, cmap=cmap, interpolation='nearest')
    plt.colorbar(ticks=[-1, 1], label="Spin")
    plt.title(titulo)
    plt.show()



if __name__ == "__main__":
    
    # Parâmetros da Simulação
    TAMANHO_MATRIZ = 100
    SEED_INICIAL = 93
    PASSOS_MC = 100000
    TEMPERATURA_C = 100
    
    # matriz inicial
    print("Criando a matriz inicial...")
    matriz_inicial = criar_matriz(seed=SEED_INICIAL, tamanho=TAMANHO_MATRIZ)
    print("Matriz inicial (primeiras 5x5 linhas/colunas):")
    print(matriz_inicial[:5, :5])
    mostrar_matriz(matriz_inicial, "Matriz de Spins Inicial (1 = Branco, -1 = Preto)")

    # Executa a simulação de Monte Carlo
    print(f"\nIniciando a simulação com {PASSOS_MC:,} passos... Isso pode levar um momento.")
    start_time = time.time()
    
    matriz_final = simular_monte_carlo(matriz_inicial, passos=PASSOS_MC, temperatura=TEMPERATURA_C)
    
    end_time = time.time()
    print(f"Simulação concluída em {end_time - start_time:.2f} segundos.")

    # Mostra a matriz final
    print("\nMatriz final após simulação (primeiras 5x5 linhas/colunas):")
    print(matriz_final[:5, :5])
    mostrar_matriz(matriz_final, f"Matriz Final após {PASSOS_MC:,} passos")