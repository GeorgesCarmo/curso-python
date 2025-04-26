import moeda_ex109 as m

def main():
    p = float(input('Digite o preco: R$ '))
    print(f'A metade de {m.moeda(p)} é {m.metade(p, True)}')
    print(f'O dobro de {m.moeda(p)} é {m.dobro(p, True)}')
    print(f'Aumentando 10%, temos {m.aumentar(p, 10, True)}')
    print(f'Reduzindo 13%, temos {m.diminuir(p, 13, True)}')

main()