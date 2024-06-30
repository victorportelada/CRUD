# CRUD em Python com MySQL

Este repositório contém um exemplo básico de como implementar operações CRUD (Create, Read, Update, Delete) usando Python e MySQL. O código foi modularizado em funções para facilitar a manutenção e a reutilização.

## Requisitos

- Python 3.x
- MySQL Server
- Biblioteca `mysql-connector-python`

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/victorportelada/CRUD.git
   cd CRUD
   ```

2. Instale a biblioteca `mysql-connector-python`:

   ```bash
   pip install mysql-connector-python
   ```

3. Configure o MySQL com as seguintes credenciais e crie o banco de dados e tabela necessários:

   ```sql
   CREATE DATABASE bdcrud;
   USE bdcrud;
   CREATE TABLE vendas (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nome_produto VARCHAR(255),
       valor DECIMAL(10, 2)
   );
   ```

## Uso

1. No arquivo `crud.py`, você encontrará as funções para cada operação do CRUD: `create`, `read`, `update` e `delete`.

2. As funções são definidas como segue:

   ```python
   def connect_to_db():
       # Função para conectar ao banco de dados
       pass

   def create(nome_produto, valor):
       # Função para criar um novo registro
       pass

   def read():
       # Função para ler os registros
       pass

   def update(nome_produto, valor):
       # Função para atualizar um registro existente
       pass

   def delete(nome_produto):
       # Função para deletar um registro
       pass
   ```

3. Para testar as funções, você pode usar o seguinte código:

   ```python
   create('chocolate', 15)
   print(read())
   update('chocolate', 20)
   print(read())
   delete('chocolate')
   print(read())
   ```

## Exemplos de Uso

### Criar um Novo Registro

```python
create('chocolate', 15)
```

### Ler Todos os Registros

```python
print(read())
```

### Atualizar um Registro Existente

```python
update('chocolate', 20)
```

### Deletar um Registro

```python
delete('chocolate')
```

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.