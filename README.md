#  🎮 Jogo da Velha - TicTacToe 🎮
Este é um projeto do Jogo da Velha (Tic-Tac-Toe) desenvolvido em Python utilizando a biblioteca
Tkinter para criar uma interface gráfica. O jogo permite que dois jogadores joguem alternadamente 
em um tabuleiro 3x3, onde o objetivo é alinhar três símbolos ("X" ou "O") horizontalmente, 
verticalmente ou diagonalmente.


## Funcionalidades ✨

- ### Tabuleiro 3x3: O jogo é jogado em um tabuleiro de 3x3 células. 🟦🟩🟥
- ### Jogadores: Dois jogadores podem jogar alternadamente. O jogador "X" é representado na cor vermelha 🔴 e o jogador "O" é representado na cor azul🔵.
- ### Vitória e Empate: O jogo verifica se há um vencedor  🏆  ou se ocorreu um empate 🤝.
- ### Reinício do Jogo: Após uma partida, é possível reiniciar o jogo e jogar novamente 🔄.
- ### Menu de opções: O menu possui a opção de reiniciar o jogo ou sair do aplicativo ❌.

## Tecnologias Utilizadas 💻

- Python 3.12.9
- Tkinter (para a interface gráfica) 🖥️
- Fontes do Tkinter para personalizar a aparência das letras. 🅾️
- 
 ##  Como Usar 🛠️
### Requisitos 📦

- Python 3.12.9 instalado em sua máquina.
- Biblioteca Tkinter instalada (normalmente vem junto com o Python). 

## Rodando o Jogo 🚀

1. Clone o repositório ou baixe o arquivo ``jogo_da_velha``.py 📂.
2. Abra o terminal ou prompt de comando 💻.
3. Navegue até o diretório onde o arquivo foi salvo 📍.
4. Execute o comando:
```` python jogo_da_velha.py ````

5. A interface gráfica do jogo será aberta 🖱️.

## Jogo 🎲
- Alternância entre jogadores: O jogo alterna entre os jogadores "X" e "O" após cada movimento 🔄.
- Clique nas células: Clique em uma célula vazia do tabuleiro para realizar o seu movimento 🖱️.
- Vitória ou empate: O jogo verifica se algum jogador ganhou 🏆 ou se o jogo terminou empatado 🤝.
- 
## Detalhes do Código 🧑‍💻
### Classes Principais 📚

1. Player: Define os jogadores, com a etiqueta (X ou O) e a cor do texto 🎨.
2. Move: Representa uma jogada feita por um jogador, contendo a linha, a coluna e o rótulo (X ou O) 🔢.
3. TicTacToeGame: Contém a lógica principal do jogo, como alternância de jogadores, validação de movimentos, verificação de vitória e empate  🧠..
4. TicTacToeTabuleiro: Gerencia a interface gráfica do jogo com Tkinter, atualiza o estado da tela, e interage com o jogador 🖥️.

## Funcionalidades Implementadas 🛠️: 

- Ciclos de Jogadores: A alternância entre jogadores "X" e "O" é realizada com o uso da função cycle() do módulo itertools  🔁.
- Verificação de Vitória: O código verifica se qualquer linha, coluna ou diagonal possui três símbolos iguais, indicando a vitória de um jogador 🎯.
- Interface Gráfica: A interface usa Tkinter para criar os botões interativos e exibir o status do jogo 🎮.