import os
import threading
from time import sleep
import sys

# Converte um .xml para um dicionário python e o armazena em um arquivo .data

# Nome do arquivo .data a ser criado
nome_data = "pmc.data"

def main():
    import subprocess
    import pkg_resources

    # https://stackoverflow.com/a/44210735
    # Checar se usuário tem o módulo xlrd instalado 
    required = {'xlrd'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        print("O módulo \"xlrd\" é necessário para a leitura de arquivos .xml e para o functionamento desse programa.")
        tmp = input("Você não possui o módulo \"xlrd\" instalado. Deseja instalá-lo? (S/n): ")
        if tmp.lower().strip() == 's':
            print("check")
            python = sys.executable
            subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
        else:
            sys.exit()

    import xlrd
    import pickle

    global nome_data
    global segundos

    # Thread que contará tempo levado
    t1 = threading.Thread(target=cronometro, daemon=True)
    t1.start()

    # Checar a existencia de um diretorio "data"
    data_exists = False
    for i in os.listdir():
        if i == "data":
            data_exists = True
    
    if not data_exists:
        os.mkdir("data")

    # Checar a existencia de um arquivo xls
    print("Procurando arquivo .xls...")
    xls_exists = False;
    for file in os.listdir():
        if (os.path.isfile(file) and file.endswith(".xls")):
            xls_exists = True
            nome_xls = file

    if not xls_exists:
        print("ERRO: Arquivo .xls nao encontrado.")
        sleep(4)
        return 1

    # Criar arquivo data, caso ele nao exista ainda
    if not os.path.exists(nome_data):
        print("Criando arquivo .data...")
        open(nome_data, "w")

    print("Lendo .xls...")
    # Carregar arquivo xls
    wb = xlrd.open_workbook(nome_xls)
    sh = wb.sheet_by_index(0)

    # Descobrir em que coluna os remedios comecam
    for fileira in range(sh.nrows):
        if (
            remover_text(sh.row(fileira)[0]) == 'SUBSTÂNCIA'   and
            remover_text(sh.row(fileira)[1]) == 'CNPJ'         and
            remover_text(sh.row(fileira)[2]) == 'LABORATÓRIO'  and
            remover_text(sh.row(fileira)[3]) == 'CÓDIGO GGREM' and
            remover_text(sh.row(fileira)[4]) == 'REGISTRO'
        ):
            remedios_fileira = fileira + 1
            print("Remedios começam na fileira", remedios_fileira + 1)
            break

    categorias = []
    remedios = {}

    # Popular categorias que todo remedio vai possuir
    # exemplo: nome, produto, pmc, etc
    for i in sh.row(remedios_fileira - 1):
        categorias.append(remover_text(i))

    print("Convertendo dados...")
    for fileira in range(remedios_fileira, sh.nrows):
        # Criar cada remedio como um value do dicionario "remedios" e atribuir
        # um dicionario vazio a ele, que possuira suas categorias
        remedios[fileira] = {}
        for categoria in range(len(categorias)):
            # Atribuir categorias a cada remedio
            remedios[fileira][categorias[categoria]] = remover_text(sh.row(fileira)[categoria])

    # Organizar remedios por ordem alfabetica do produto
    print("Organizando remedios...")
    remedios = dict(sorted(tuple(remedios.items()), key=lambda x: f"{x[1]['PRODUTO']} {x[1]['LABORATÓRIO']} {x[1]['APRESENTAÇÃO']}"))

    # Escrever dicionario remedios em arquivo .data
    print("Escrevendo dados...")
    with open(nome_data, "wb") as wf:
        pickle.dump(remedios, wf)

    # Mover arquivo xls para diretorio data
    os.rename(nome_xls, os.path.join("data", "pmc.xls"))
    print(f"Convertido com sucesso!\nTempo total: {segundos} segundos")
    sleep(3)

def cronometro():
    # Conta os segundos
    global segundos
    while True:
        sleep(1)
        segundos += 1

def remover_text(cell):
    # remove "text:" e "'" da célula
    return str(cell).replace("text:", "").replace("'", "")


segundos = 0
nome_data = os.path.join("data", nome_data)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcesso interrompido.\nSaindo...")
        sys.exit(0)