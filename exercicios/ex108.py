import moeda_ex108 as m

def main():
    p = float(input('Digite o preco: R$ '))
    print(f'A metade de {m.moeda(p)} é {m.moeda(m.metade(p))}')
    print(f'O dobro de {m.moeda(p)} é {m.moeda(m.dobro(p))}')
    print(f'Aumentando 10%, temos {m.moeda(m.aumentar(p, 10))}')
    print(f'Reduzindo 13%, temos {m.moeda(m.diminuir(p, 13))}')

main()