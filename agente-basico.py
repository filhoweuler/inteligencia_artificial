import random

def acao(posicao, sujo, ultimo_limpo): 
    #para sujo, 1 eh limpo e 0 eh sujo

    if sujo:
        print("Limpando a posicao {}...".format(posicao))
        acao('A' if posicao == 'B' else 'B', random.randint(0, 1), 0)
    else:
        print("Não há sujeira por aqui ...")
        
        if ultimo_limpo:
            print("Tudo limpo por aqui! Até logo!")
        else:
            acao('A' if posicao == 'B' else 'B', random.randint(0, 1), 1)

acao('A', random.randint(0, 1), 0)





