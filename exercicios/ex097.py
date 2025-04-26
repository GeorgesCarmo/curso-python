# Faça um programa que tenha a função escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

    
# Programa principal
escreva('Olá, Mundo!')
escreva('Curso em Vídeo')
escreva('Aprendendo Python')
escreva('Desenvolvimento de Software')
