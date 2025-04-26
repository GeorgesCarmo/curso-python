def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except Exception as e:
        print(f'Erro ao criar o arquivo: {e}')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except Exception as e:
        print(f'Erro ao ler o arquivo: {e}')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        a.close()
    finally:
        a.close()

def adicionarRegistro(nome, nomePessoa = 'desconhecido', idade = 0):
    try:
        a = open(nome, 'at')
    except Exception as e:
        print(f'Erro ao abrir o arquivo: {e}')
    else:
        try:
            a.write(f'{nomePessoa};{idade}\n')
        except Exception as e:
            print(f'Erro ao escrever no arquivo: {e}')
        else:
            print(f'\033[32mNovo registro de {nomePessoa} adicionado com sucesso!\033[m')
        finally:
            a.close()
    finally:
        a.close()         