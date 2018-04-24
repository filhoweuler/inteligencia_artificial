
def solve(grid, pos, ultimo_limpo):
    print("Estou na posicao {} ...".format(pos))
    if grid[pos] == 1: #posicao suja
        print("Limpando a posicao!")
        grid[pos] = 0
        solve(grid, 1 if pos == 0 else 0, 1)
    else:
        print("A posicao esta limpa!")
        
        if ultimo_limpo == 1: #se a outra tambem esta limpa
            print("Terminamos!")
            return
        
        solve(grid, 1 if pos == 0 else 0 , 1)


solve([0,1], 1, 0)
