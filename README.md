# Projeto-Aplicacoes-Digitais

## Sumário
- [Descrição do problema](#descrição-do-problema)
- [pokemon.py](#pokemonpy)
- [frontend.py](#frontendpy)
- [database.py](#databasepy)
- [test_pokemon.py](#test_pokemonpy)

## Descrição do problema
Para o projeto, eu decidi criar uma Pokédex, onde o usuário digita o nome de um Pokémon e retorna vários dados sobre ele, como o número na Pokédex, o nome, o peso, a altura, a abilidade e os tipos, além de uma imagem dele e a sua cor. Para isso, as tecnologias listadas a baixo foram utilizadas, elas garantem o funcionamento adequado com uma GUI, testes unitários e um banco de dados para armazenar as consultas.

- Python
- Tkinter
- PokéAPI
- SQLite
- pytest
- Requests
- Pillow


O projeto foi dividido em 3 módulos, [pokemon.py](https://github.com/Rafael-aaf/Projeto-Aplicacoes-Digitais/blob/91c835f8ce8ca168286377dc91aca5f319f46826/pokemon.py), [frontend.py](https://github.com/Rafael-aaf/Projeto-Aplicacoes-Digitais/blob/91c835f8ce8ca168286377dc91aca5f319f46826/frontend.py), [database.py](https://github.com/Rafael-aaf/Projeto-Aplicacoes-Digitais/blob/91c835f8ce8ca168286377dc91aca5f319f46826/database.py), [test_pokemon.py](https://github.com/Rafael-aaf/Projeto-Aplicacoes-Digitais/blob/550234826fe2360a35aee07f6b89677e96d658c1/unit_tests/test_pokemon.py), que estão explicados a seguir.

## pokemon.py
Ocorre a chamada da API

## frontend.py


## database.py
Para o banco de dados, eu usei o SQLite. Como ele só armazena as consultas do usuário, apenas uma tabela com 6 atributos (além da chave primária) foi o suficiente, como pode-se ver na imagem a seguir de seu modelo conceitual.

![Modelo conceitual!](https://github.com/Rafael-aaf/Projeto-Aplicacoes-Digitais/blob/969704fbf0190e756f58d24a75197b68645869be/prints/tabela_pokedex.png)


Nesse módulo do código, foram utilizados 2 scripts SQL, um para a criação e outro para a inserção de dados. O fluxo de execução pode ser visto no diagrama de sequência a seguir: frontend.py -> import database -> database.py -> cursor.execute() -> mydatabase.db (se o arquivo do banco ainda não existir) -> database.inserir_pokemon() -> mydatabase.db

![Diagrama dos módulos!](https://github.com/Rafael-aaf/Projeto-Aplicacoes-Digitais/blob/59c78de3965290670cfb28966876d1947dfae75c/prints/Diagrama_seq_modulos_pokedex.drawio.png)

Os scripts SQL estão transcritos a seguir:
### Criação de tabela
```sql
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT NOT NULL,
    name TEXT NOT NULL,
    color TEXT NOT NULL,
    weight TEXT NOT NULL,
    height TEXT NOT NULL,
    ability TEXT NOT NULL
)
```

### Inserção na tabela
```sql
INSERT INTO usuarios (number, name, color, weight, height, ability)
        VALUES (?, ?, ?, ?, ?, ?)
```

## test_pokemon.py
Para os testes unitários, utilizei a biblioteca pytest e importei o módulo pokemon.py. Apenas 2 testes foram feitos, para testar se um Pokémon existe e se retorna os dados corretos, e para testar erro, quando um Pokémon não existe.

Os testes usam ```raw_data``` para armazenar um dicionário com todos os dados disponíveis do Pokémon na API (Python converte arquivos json em dicionário), e ```data``` para armazenar um dicionário com os dados que serão utilizados, como o número na Pokédex, o nome, o peso, a altura, a abilidade e a sua cor.

