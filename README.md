# Modelo-de-Ising-

Este projeto implementa uma simulação 2D do Modelo de Ising usando o algoritmo de Monte Carlo de Metropolis. O objetivo é visualizar o comportamento emergente de um sistema de spins em uma rede quadrada, observando a formação de domínios magnéticos em uma determinada temperatura.
A performance da simulação é significativamente acelerada usando a biblioteca Numba, que compila funções Python críticas em código de máquina de alta velocidade.
(Exemplo de uma possível matriz final, mostrando a formação de domínios.)
Sobre o Projeto
O Modelo de Ising é um modelo matemático em mecânica estatística usado para descrever o ferromagnetismo. Ele consiste em uma rede de "spins" discretos que podem estar em um de dois estados (+1 ou -1). A energia do sistema depende da interação entre spins vizinhos.
Este script utiliza o algoritmo de Metropolis-Hastings, um método de Monte Carlo, para simular a evolução do sistema. A cada passo, um spin aleatório é escolhido e a possibilidade de invertê-lo é avaliada com base na mudança de energia e na temperatura do sistema. Isso permite que o sistema explore diferentes configurações e eventualmente atinja o equilíbrio térmico.
Tecnologias utilizadas:
Python 3: Linguagem principal do projeto.
NumPy: Para manipulação eficiente de matrizes.
Matplotlib: Para visualização dos dados.
Numba: Para compilação Just-In-Time (JIT) e aceleração massiva do loop de simulação.

Siga estes passos para configurar o ambiente do projeto.
Clone o repositório (ou baixe os arquivos)
Generated bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Use code with caution.
Bash
Crie e ative um ambiente virtual (recomendado)
Isso cria um ambiente isolado para as dependências do projeto, evitando conflitos com outros projetos Python.
No macOS/Linux:
Generated bash
python3 -m venv venv
source venv/bin/activate
```    *   No Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
Use code with caution.
Bash
Instale as dependências
Instale todas as bibliotecas necessárias com um único comando:
Generated bash
pip install numpy matplotlib numba
Use code with caution.
Bash
Como Usar
Com o ambiente configurado e as dependências instaladas, execute o script principal a partir do seu terminal:
Generated bash
python modelo_ising.py
Use code with caution.
Bash
O script irá:
Imprimir no console o status da criação e da simulação.
Exibir uma janela de gráfico com a matriz de spins inicial (aleatória).
Após a conclusão da simulação, exibir uma segunda janela com a matriz final, mostrando os domínios formados.
Personalização



Você pode facilmente alterar os parâmetros da simulação modificando as variáveis no bloco if __name__ == "__main__": do arquivo modelo_ising.py.
Generated python
if __name__ == "__main__":
    
    # Parâmetros da Simulação
    TAMANHO_MATRIZ = 100       # Dimensão da grade (100x100)
    SEED_INICIAL = 93          # Semente para reprodutibilidade
    PASSOS_MC = 100000         # Número de inversões de spin aceitas
    TEMPERATURA_C = 100        # Temperatura do sistema em Celsius
Use code with caution.
Python
TAMANHO_MATRIZ: Altere para redes maiores ou menores.
PASSOS_MC: Um número maior de passos levará o sistema para mais perto do equilíbrio, mas aumentará o tempo de simulação.
TEMPERATURA_C: A temperatura é um parâmetro crítico. Temperaturas altas resultam em desordem (matriz aleatória), enquanto temperaturas baixas (próximas ou abaixo da temperatura crítica de Curie) favorecem a formação de grandes domínios.
Estrutura do Código
O código está organizado nas seguintes funções:
criar_matriz(): Cria a grade inicial de spins aleatórios.
simular_monte_carlo(): Contém o loop principal da simulação. Esta é a função otimizada com @njit.
mostrar_matriz(): Função utilitária para exibir a matriz usando Matplotlib.
