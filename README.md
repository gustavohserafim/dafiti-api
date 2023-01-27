## Teste Técnico
API para gerenciamento de Produtos - Dafiti
## Descrição
API RESTFul para gerenciamento de produtos que permite o upload de CSV para criação de produtos em lote e
download de csv personalizado de acordo com os parametros passados.
## Principais tecnologias
````Python 3````
````Flask````
````Pandas````
````MySQL````

## Pré requisitos
````Docker 20.10.21````
````docker-compose 2.13.0````

## Instalação
Com o docker e docker-compose devidamente instalados basta clonar o repositório e executar o comando
````
docker-compose up dafitiapi
````
Serão gerados dois containers, contendo backend e banco de dados;
## Rotas

| Rota             | Metodo | Descrição                                                                              |
|------------------|--------|----------------------------------------------------------------------------------------|
| /api/product/csv | POST   | Recebe um arquivo CSV para criação em lote de produtos                                 |
| /api/product/csv | GET    | Gera um arquivo CSV de produtos de acordo com parâmetros passados(documentação abaixo) |
| /api/product     | GET    | Pega todos os produtos                                                                 |
| /api/product     | POST   | Cria um novo produto                                                                   |
| /api/product/id  | GET    | Pega um produto pelo id                                                                |
| /api/product/id  | PUT    | Atualiza um produto pelo id                                                            |
| /api/product/id  | DELETE | Deleta um produto pelo id                                                              |

## Parametros para geração de CSV

Rota GET | /api/product/csv

| Parametro   | Tipo   | Descrição                                                      |                                                                
|-------------|--------|----------------------------------------------------------------|
| name        | string | Retorna produtos apenas com o nome começando com termo passado |
| min_price   | int    | Retorna produtos com preço acima do valor passado              |
| max_price   | int    | Retorna produtos com preço abaixo do valor passado             |

## Respostas

| Status code | Descrição                            |
|-------------|--------------------------------------|
| 200         | Ok                                   |
| 400         | Um ou mais parametros são invalidos. |


## Testes
| Nome                       | Descrição                                                      |
|----------------------------|----------------------------------------------------------------|
| create_products_csv        | Gera um CSV com produtos e faz requisição para criação em lote |
| get_products_csv           | Gera CSV para download com todos produtos                      |
| get_all_products           | CRUD, read all                                                 |
| get_one_product            | CRUD, read                                                     |
| update_product             | CRUD, update                                                   |
| delete_product             | CRUD, delete                                                   |
| create_and_get_csv_product | Cria um produto e faz o download do CSV passando o parametro   |
| get_csv_min_price          | Download do csv personalizado com o parametro de min_price     |
| get_csv_max_price          | Download do csv personalizado com o parametro de max_price     |
| get_csv_all_params         | Download do csv personalizado com todos os parametros          |

Rodar ```python tests/test_api.py``` se nenhuma exception for levantada os testes rodaram com sucesso.
Os CSVs serão gerados na pasta ```tests``` para conferência.