from os import system, name

def main():
    import pickle
    import os
    from sys import exit
    from converter import nome_data
    from time import sleep

    # Caractere usado para dividir resultados
    caractere_divisor = "#"
    # Numero de `caracter_divisor` usados para dividir os resultados
    divisor_num = 100

    # PMC mostrado nos resultados
    tipo_pmc = "PMC 17%"

    # Checar se arquivo .data existe
    if not os.path.exists(nome_data):
        print("Arquivo .data nao encontrado. Execute \"converter.py\" primeiro.")
        sleep(4)
        return 1;
    
    # Ler .data e criar dicionario com remedios
    with open(nome_data, "rb") as rf:
        remedios = pickle.load(rf)

    # Guardar remedio/laboratorio anterior para mostrar como "ultima pesquisa"
    remedio_anterior = ""
    laboratorio_anterior = ""

    system('cls' if name == 'nt' else 'clear')
    #print("-"*divisor_num)
    print("Pressione \"Ctrl + C\" para sair")

    while True:
        resultados = []
        print("-"*divisor_num)

        # Guardar nome e laboratorio do remedio do modo como foram
        # digitados pelo user, em uppercase
        nome_anterior = input("Remédio: ").upper()
        if not nome_anterior.isdigit():
            laboratorio_anterior = input("Laboratório (opcional): ").upper()
        else:
            laboratorio_anterior = ""

        # Remover todos os espacos em branco para facilitar a pesquisa
        nome = nome_anterior.replace(" ", "")
        laboratorio = laboratorio_anterior.replace(" ", "")

        system('cls' if name == 'nt' else 'clear')
        
        # Pesquisar por EXATAMENTE o que o user digitou
        if nome[-1] == '.':
            for remedio in remedios:
                if nome.replace(".", "") == remedios[remedio]['PRODUTO'].replace(" ", ""):
                    resultados.append(remedio)
	
	    # Pesquisar por código de barras
        elif nome.strip().isdigit():
            for remedio in remedios:
                if nome in remedios[remedio]['EAN 1']:
                    resultados.append(remedio)
                    break

	    # Pesquisar por resultados que contenham o que o user digitou
        else:
            for remedio in remedios:
                if nome in remedios[remedio]['PRODUTO'].replace(" ", ""):
                    resultados.append(remedio)

        # Filtrar resultados por laboratorio
        if not laboratorio == "":
            temp = resultados
            resultados = []
            for i in range(len(temp)):
                if laboratorio in remedios[temp[i]]['LABORATÓRIO'].replace(" ", ""):
                    resultados.append(temp[i])

        # Printar resultados, caso haja algum
        if len(resultados) > 0:
            print("\nResultados:")

            for r in resultados:
                mg = " ".join(remedios[r]['APRESENTAÇÃO'].split()[:2])
                print(caractere_divisor * divisor_num)
                print(
                    f"\nNome: {remedios[r]['PRODUTO']} {mg} ({remedios[r]['LABORATÓRIO']})\n"
                    f"Substância: {remedios[r]['SUBSTÂNCIA']}\n"
                    f"Apresentação: {remedios[r]['APRESENTAÇÃO']}\n"
                    f"Tipo de Produto: {remedios[r]['TIPO DE PRODUTO (STATUS DO PRODUTO)']}\n"
                    f"Tarja: {remedios[r]['TARJA']}\n"
                    f"PMC: {remedios[r][tipo_pmc]}\n"
                    )
        else:
            print("Nenhum resultado encontrado")

        # Mostrar a última pesquisa ao usuario para possibilitar a checagem de erros de escrita
        if nome_anterior != "" or laboratorio_anterior != "":
            print("-"*divisor_num)
            print("Você pesquisou:")
            print(f"Remédio: {nome_anterior}\nLaboratório: {laboratorio_anterior}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaindo...")
