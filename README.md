# Python_Scraping_Gmail

## SOBRE

- Este projeto visa mostrar de uma maneira simples como fazer scraping do Gmail, podendo até mesmo salvar os pdf anexados.

## REQUISITOS

- python3.10^
- Conta no GCP (gratuito) com projeto criado e uma credencial para a conta (há diversos vídeos na internet de como fazer isso)
- pip installado

## PASSOS

- Depois de clonar o repositório em uma pasta, execute os seguintes comandos na pasta raiz.

```
python3 -m venv venv
```

```
source ./venv/bin/activate
```

```
pip install -r requirements.txt
```

- Utilize o setting.env para criar o arquivo .env na raiz do projeto e assim colocar as credenciais necessárias.

- Após isso só fazer as mudanças necessárias dentro do método "starting_scrap".

- A variável query pode ser alterada obedecendo o sistema de filtro do gmail que pode ser observado no site (https://support.google.com/mail/answer/7190?hl=pt-BR)
