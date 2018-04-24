# programa dos2

import heapq
import copy

def manhattan(board):
    counter = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] != -1:
                v = board[i][j]
                line = (v-1)//3
                column = v - (line * 3 + 1)

                d_manhattan = abs(line - i) + abs(column - j)

                counter += d_manhattan
    
    return counter

def position(board):
    counter = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] != -1 and board[i][j] != (3*i + j + 1):
                counter+=1
    return counter


teste = [[5,4,8], [3,-1,7],[1,6,2]]
# teste = [[8, 3, 1], [5, 4, 2], [-1, 7, 6]]

# print(position(teste))
# print(manhattan(teste))

moves_x = [0, 0, -1, 1]
moves_y = [-1, 1, 0, 0]

# tree_visitado = {}

# def tree_solve(board, h):
#     if position(board) == 0: 
#         #position retorna o numero de pecas fora de lugar
#         print("Chegamos ao objetivo! Resolvido!")
#         print("Na DFS exploramos {} nos!".format(len(tree_visitado)))
#         return

#     tree_visitado[repr(board)] = 1

#     for i in range(0,3):
#         for j in range(0,3):
#             if board[i][j] == -1:
#                 #trazer pecas de : (i, j-1), (i, j+1), (i-1, j), (i+1, j)
#                 for k in range(4):
#                     x = i + moves_x[k]
#                     y = j + moves_y[k]

#                     if x in range(3) and y in range(3):
#                         board_move = copy.deepcopy(board)
#                         board_move[i][j] = board_move[x][y]
#                         board_move[x][y] = -1
#                         if not repr(board_move) in tree_visitado:
#                             tree_solve(board_move, h+1)

# tree_solve(teste, 0)

nos_explorados = 0

def a_estrela(inicial, h, path):
    global nos_explorados
    pq = []
    visitado = {}
    heapq.heappush(pq, (manhattan(inicial), inicial, 0, [inicial]))
    # heapq.heappush(pq, (manhattan(inicial), inicial, 0))

    while len(pq) != 0:
        tupla = heapq.heappop(pq)
        nos_explorados += 1
        board = tupla[1]
        altura = tupla[2]
        historico = tupla[3]

        visitado[repr(board)] = 1

        if position(board) == 0:
            print("TERMINAMOS NA ALTURA {} !".format(altura))
            print("Exploramos {} nos".format(len(visitado)))
            for bs in historico:
                print(bs)
            return
                
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] == -1:             
                    for k in range(4):
                        x = i + moves_x[k]
                        y = j + moves_y[k]

                        if x in range(3) and y in range(3):
                            board_move = copy.deepcopy(board)
                            board_move[i][j] = board_move[x][y]
                            board_move[x][y] = -1
                            
                            if not repr(board_move) in visitado:
                                historico.append(board_move)
                                heapq.heappush(pq, (manhattan(board_move) + altura + 1, board_move, altura + 1, copy.deepcopy(historico)))
                                #heapq.heappush(pq, (manhattan(board_move) + altura + 1, board_move, altura + 1))
                    break
    print("Exploramos {} nos".format(len(visitado)))
# a_estrela(teste, 0, [])