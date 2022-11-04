import glob
import os


def opcaoListar(localiza): #funcao para listar os clientes
    SelCli = (input("Escolha um cliente: ")).lower()
    for clientes in (glob.glob(os.path.join(localiza,'/**/*{}'.format(SelCli)), recursive=True)):
        print(clientes)
    return       

def opcaoTipo(localiza): #funcao selecionar o tipo de reuniao
    SelTipo = int(input("[1] - Metrics \n[2] - Calls "))
    if SelTipo == 1:
        seletor = "metrics"
        for clientes in (glob.glob(os.path.join(localiza,'/**/*{}*'.format(seletor)), recursive=True)):
            print(clientes)
    elif SelTipo == 2:
        seletor = "calls"
        for clientes in (glob.glob(os.path.join(localiza,'/**/*{}*'.format(seletor)), recursive=True)):
            print(clientes)
    elif SelTipo == 0:
        return

def opcaoData(localiza): #funcao para selecionar a data
    SelData = (input("Escolha uma data, formato (ANO_MES_DIA(): ")).lower()
    for clientes in (glob.glob(os.path.join(localiza,'/**/*{}*'.format(SelData)), recursive=True)):
        print(clientes)    

def opcaoDeleta(localiza): #funcao para deletar o cliente selecionado
    SelDel = (input("Escolha um cliente: ")).lower()
    for clientes in (glob.glob(os.path.join(localiza,'/**/*{}'.format(SelDel)), recursive=True)):
        print("Removendo {}".format(clientes))
        os.remove(clientes)
    return

def menu():
    print ("POR FAVOR DEFINA O LOCAL DOS ARQUIVOS ANTES DE UTILIZAR O PROGRAMA!")
    print ("[1] Definir local dos arquivos")
    print ("[2] Filtrar por Nome")
    print ("[3] Filtrar por Tipo de Arquivo")
    print ("[4] Filtrar por Data")
    print ("[5] Remover cliente")
    print ("[0] Sair")

while True:

    menu()
    opcao = int(input("Escolha sua opcao: "))

    if opcao == 0: #sair do programa
        exit()
    elif opcao == 1:  #Local dos arquivoss
        localiza=(input("Path dos arquivos: "))
    elif opcao == 2:  #filtrar por nomes do cliente
        opcaoListar(localiza)      
    elif opcao == 3: #filtrar por tipo de arquivo
        opcaoTipo(localiza)
    elif opcao == 4: #filtrarpordata
        opcaoData(localiza)
    elif opcao == 5: #deleta tudo de um cliente
        opcaoDeleta(localiza)

