# Refaça o desafio que lê o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print("=" * 20)
print("10 TERMOS DE UMA PA")
print("=" * 20)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo_termo = primeiro + (10 - 1) * razao
c = primeiro
while c <= decimo_termo:
    print(c, end=" -> ")
    c += razao
print("ACABOU")
