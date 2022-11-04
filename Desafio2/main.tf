terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker" ##imagem do docker
      version = "2.23.0" ## versao
    }
  }
}

provider "docker" { ## Definindo o provider
  host = "unix:///var/run/docker.sock"
}

# Puxa o arquivo de configuração da imagem
resource "docker_image" "desafio_sensedia" {
  name = "desafio_sensedia_jose"
  build{
    path = "../../Desafio2" ## pasta onde está localizado o dockerfile
    dockerfile = "dockerfile"    ## Nome do dockerfile que está com a configuracao
  }
  
}

#definicao das portas que poderao ser acessadas para verificar o container
resource "docker_container" "desafio_sensedia_jose" {
  image = docker_image.desafio_sensedia.image_id
  name = "desafio_sensedia_jose"
  ports {
   internal = "80"
   external = "8080" #localhost 8080
  }
}
