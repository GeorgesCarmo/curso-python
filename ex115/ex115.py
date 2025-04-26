import lib.interface as interface
import lib.arquivo as arquivo
from time import sleep

arq = 'pessoas1.txt'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

interface.cabecalho('SISTEMA DE ARQUIVO v1.0')
while True:
    resposta = interface.menu(['Ver pessoas cadastradas', 'Adicionar nova pessoa', 'Sair'])
    if resposta == 1:
        interface.cabecalho('PESSOAS CADASTRADAS')
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        interface.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = interface.leiaInt('Idade: ')
        arquivo.adicionarRegistro(arq, nome, idade)
    elif resposta == 3:
        interface.cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('Opção inválida! Tente novamente.')
    sleep(1)
