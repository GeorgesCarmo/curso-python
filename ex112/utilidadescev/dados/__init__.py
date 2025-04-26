def leiaDinheiro(msg):
    """
    Função para validar e formatar valores monetários.
    :param msg: Mensagem a ser exibida ao usuário.
    :return: Valor monetário formatado.
    """
    while True:
        valor = str(input(msg)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[0;31mERRO! "{valor}" é um preço inválido.\033[m')
        else:
            return float(valor)