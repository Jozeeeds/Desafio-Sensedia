# Desafio-Sensedia
Desafio Sensedia 2023


# Desafio 1

Desenvolvido na versão 3.8.10 do Python utilizando [Glob](https://docs.python.org/3/library/glob.html)

O Script foi desenvolvido utilizando um menu de navegação para o usuário poder escolher quais funções deseja utilizar e tambem uma funcao para definir onde os arquivos estao localizados no computador.

O módulo glob do python se mostra muito versátil e prático de ser utilizado para navegar entre pastas, ao inves de realizar diversas buscas entrando e saindo de pastas como normalmente é feito com o _path_ podemos navegar de forma recursiva dentro das pastas utilizando asteriscos duplos (* *) e também habilitando a forma recursiva de busca com _recursive=True_ conforme pode ser visto no código abaixo.

O módulo _os_ foi utilizado para poder deletar os arquivos na função de deletar e também para navegar até a pasta definida pelo usuário.

## Explicação do código
---

### Menu Principal

A parte do menu principal que o usuário pode interagir foi feita de forma simples, uma função menu que é colocada dentro de um loop _While_ que sera executado até o usuário decidir sair do programa.

Cada opção chama sua respectiva função passando a variável de localização dos arquivos que foi definida pelo usuario.

```python
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
    elif opcao == 1:  #Local dos arquivos
        localiza=(input("Path dos arquivos: "))
    elif opcao == 2:  #filtrar por nomes do cliente
        opcaoListar(localiza)      
    elif opcao == 3: #filtrar por tipo de arquivo
        opcaoTipo(localiza)
    elif opcao == 4: #filtrarpordata
        opcaoData(localiza)
    elif opcao == 5: #deleta tudo de um cliente
        opcaoDeleta(localiza)

```

---

### Função para listar os clientes

Nessa função temos a variavel SelecionarCliente (_SelCli_) que será um input do usuário, a mesma está realizando a conversão para letras minúsculas para melhorar a pesquisa, após o input do usuário teos um loop for que está sendo utilizado para listar todos os clientes selecionados, ou seja, o resultado final será todo impresso para o usuário.

_os.path.join_ está sendo utilizando para que a variavel _localiza_ possa orientar para o glob qual será o caminho que o mesmo deve realizar a busca. Os asteriscos duplos juntamente com _recursive=True_ indicam que essa busca deve ser recursiva dentro da pasta para encontrar todos os arquivos que o usuário está buscando, o _format(SelCli)_ está passando a variável digitada pelo usuário para a pesquisa.


```python
def opcaoListar(localiza): 
    SelCli = (input("Escolha um cliente: ")).lower()
    for clientes in (glob.glob(os.path.join(localiza,'/**/*_{}'.format(SelCli)), recursive=True)):
        print(clientes)
    return  
```

---

### Função para localizar os clientes

Esta função funciona de forma parecida com as outras, porém com algumas facilidades a mais para facilitar o uso, ao invés do usuário digitar se busca _metrics_ ou _calls_ foi disponibilizado os numeros 1 e 2 representando o que pode ser pesquisado.

Dentro da função existe um teste _if/elif_ que verifica qual número foi digitado, após isso a variável _seletor_ define o que será pesquisado.

```python
def opcaoTipo(localiza): #funcao selecionar o tipo de reuniao
    SelTipo = int(input("[1] - Metrics \n[2] - Calls \n[0] - Sair "))
    if SelTipo == 1:
        seletor = "metrics"
        for clientes in (glob.glob(os.path.join(localiza,'/**/{}_*'.format(seletor)), recursive=True)):
            print(clientes)
    elif SelTipo == 2:
        seletor = "calls"
        for clientes in (glob.glob(os.path.join(localiza,'/**/{}_*'.format(seletor)), recursive=True)):
            print(clientes)
    elif SelTipo == 0:
        return
```

---

### Função para localizar por data

Também funciona de forma parecida com as outras funções, tem um indicador para orientar qual formato de data deve ser colocado

```python
def opcaoData(localiza): #funcao para selecionar a data
    SelData = (input("Escolha uma data, formato (ANO_MES_DIA(): ")).lower()
    for clientes in (glob.glob(os.path.join(localiza,'/**/*{}*'.format(SelData)), recursive=True)):
        print(clientes)    
```
---

### Função para localizar para deletar

Essa função possui _os.remove_ para deletar os arquivos que foram encontrados.

```python
def opcaoDeleta(localiza): #funcao para deletar o cliente selecionado
    SelDel = (input("Escolha um cliente: ")).lower()
    for clientes in (glob.glob(os.path.join(localiza,'/**/*{}'.format(SelDel)), recursive=True)):
        print("Removendo {}".format(clientes))
        os.remove(clientes)
    return
```

---

## Como utilizar

Pode ser executado pelo VSCODE ou até mesmo pelo próprio editor do Python.

### Passo a passo

* 1 - Execute o programa da forma que preferir
* 2 - Utilize a opção numero **1** para definir o local dos arquivos, por exemplo, caso os arquivos estejam dentro da pasta desafio, colocar o seguinte caminho: D:\Desafio sensedia\desafio
* 3 - Escolha qual função utilizar! Enquanto permanecer no programa não é necessário adicionar o local dos arquivos novamente caso queira utilizar outra função.
