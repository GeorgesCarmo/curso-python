import moeda_ex107 as m

def main():
    p = float(input('Digite o preco: R$ '))
    print(f'A metade de {p} eh {m.metade(p)}')
    print(f'O dobro de {p} eh {m.dobro(p)}')
    print(f'Aumentando 10%, temos {m.aumentar(p, 10)}')
    print(f'Reduzindo 13%, temos {m.diminuir(p, 13)}')

main()