# DESAFIO 2

O desafio 2 consiste em subir o NGINX em um container e alterar o arquivo index.html no body para apresentar as informações requisitadas, foi realizado utilizando [Terraform](https://developer.hashicorp.com/terraform/docs).

Decidi utilizar terraform nesse desafio pois facilita o compartilhamento do container e criação do mesmo.

**Necessário ter instalado terraform e docker para o funcionamento do tutorial abaixo**

---

## Configuração do terraform - Parte 1

**Para fins de facilitar o entendimento do funcionamento irei dividir o arquivo em 3 partes, mas no ambiente final ele é somente um arquivo**

Nessa primeira parte do código do terraform estou definindo quais serão os providers necessários para realizar a criação do container, o primeiro provider sendo  [_kreuzwerker/docker_](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs) que é um provider obtido diretamente do site do terraform. 

O provider _docker_ que está definido para rodar diretamente no linux/localhost com _unix:///var/run/docker.sock_

```terraform
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker" 
      version = "2.23.0" 
    }
  }
}

provider "docker" { 
  host = "unix:///var/run/docker.sock"
}
```

---

## Configuração do terraform - Parte 2

Essa parte aqui que é um pouco diferente de configurações mais comuns, pois o terraform está se baseando em uma dockerfile para criar o container, essa dockerfile possui as seguintes configurações:

Na primeira linha  estou buscando a ultima versão disponível do nginx.<br>
Na segunda linha estou copiando o index.html customizado e adicionando ele dentro do container.<br>
```dockerfile
FROM nginx:latest 
COPY ./html/index.html /usr/share/nginx/html/index.html 
```

O terraform le as configurações definidas no arquivo dockerfile acima e realiza a criação do container

```terraform
# Puxa o arquivo de configuração da imagem
resource "docker_image" "desafio_sensedia" {
  name = "desafio_sensedia_jose"
  build{
    path = "../../Docker"       
    dockerfile = "dockerfile"    
  }
  
}
```

---

## Configuração do terraform - Parte 3

Aqui está sendo definido quais portas internas e externas poderão ser acessadas no container, esta sendo liberado a 8080 para acessar ela no localhost:8080, sempre referenciando a imagem do docker que foi definida na parte 2.


```terraform
#definicao das portas que poderao ser acessadas para verificar o container
resource "docker_container" "desafio_sensedia_jose" {
  image = docker_image.desafio_sensedia.image_id
  name = "desafio_sensedia_jose"
  ports {
   internal = "80"
   external = "8080" 
  }
}
```

## Como executar

* 1 - Primeiro é necessário utilizar o comando _terraform init_ no arquivo main.tf, irá aparecer a mensagem "Terraform has been successfully initialized!"
* 2 - Executar o comando _terraform apply_ que irá pedir para confirmar, basta digitar um **yes** e aguardar o aviso que está completo a criação.
* 3 - Acesse o localhost na porta 8080 http://localhost:8080 para visualizar a página principal do nginx que está com uma mensagem de boas vindas!
