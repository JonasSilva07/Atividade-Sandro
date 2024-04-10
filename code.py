def registrar_mensagem():
    mensagem = input("Digite sua mensagem (ou 'sair' para encerrar): ")
    if mensagem.lower() == 'sair':
        return False
    elif 'palavra_impropria' in mensagem.lower():
        registrar_arquivo('palavras_improprias.txt', mensagem)
    elif 'elogio' in mensagem.lower():
        registrar_arquivo('elogios.txt', mensagem)
    elif 'reclamacao' in mensagem.lower():
        registrar_arquivo('reclamacoes.txt', mensagem)
    else:
        print("Mensagem não reconhecida.")
    return True

def registrar_arquivo(nome_arquivo, mensagem):
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(mensagem + '\n')

def main():
    continuar = True
    while continuar:
        continuar = registrar_mensagem()

if _name_ == "_main_":
    main()
