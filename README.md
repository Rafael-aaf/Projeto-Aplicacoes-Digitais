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


O projeto foi dividido em 4 módulos, [pokemon.py](https://github.com/Rafael-aaf/Projeto-Aplicacoes-Digitais/blob/91c835f8ce8ca168286377dc91aca5f319f46826/pokemon.py), [frontend.py](https://github.com/Rafael-aaf/Projeto-Aplicacoes-Digitais/blob/91c835f8ce8ca168286377dc91aca5f319f46826/frontend.py), [database.py](https://github.com/Rafael-aaf/Projeto-Aplicacoes-Digitais/blob/91c835f8ce8ca168286377dc91aca5f319f46826/database.py), [test_pokemon.py](https://github.com/Rafael-aaf/Projeto-Aplicacoes-Digitais/blob/550234826fe2360a35aee07f6b89677e96d658c1/unit_tests/test_pokemon.py), que estão explicados a seguir.

## pokemon.py
Neste primeiro módulo ocorre a chamada da API, com a biblioteca Requests, e é onde os dados são coletados e retornados como um dicionário. O módulo é dividido em 2 funções, a função ```get_pokemon_info``` e o ```main```.

Na primeira função, há o retorno de ```return pokemon_data```, caso o status code seja 200, ou uma mensagem de erro. O ```main``` recebe o retorno da função anterior e retorna os dados em um dicionário, como visto a seguir:

```python
def main(pokemon_info):
    if pokemon_info:
        
        name = pokemon_info['name']

        species_url = f"https://pokeapi.co/api/v2/pokemon-species/{name}"
        species_response = requests.get(species_url)
        species_data = species_response.json()

        return {
            "name": pokemon_info['name'].capitalize(),
            "id": pokemon_info['id'],
            "weight": pokemon_info['weight'],
            "height": pokemon_info['height'],
            "ability": pokemon_info['abilities'][0]['ability']['name'].capitalize(),
            "types": [t['type']['name'] for t in pokemon_info['types']],
            "sprite": pokemon_info["sprites"]["other"]["official-artwork"]["front_default"],
            "color": species_data["color"]["name"]
        }
```


## frontend.py
Nesse módulo, os dados são organizados em uma interface gráfica, o módulo pokemon.py é chamado e os dados são armazenados em um banco de dados (ver [database.py](#databasepy)). Para isso, as seguintes bibliotecas são usadas: Tkinter, Pillow e Requests.

O módulo contêm a função ```search()``` e a estrutura da interface gráfica. Nas 2 linhas mostradas abaixo, ocorre a chamada da função ```get_pokemon_info``` do módulo pokemon.py, passando como paramêtro o nome do Pokémon inserido pelo usuário, e a chamada de ```pokemon.main```. Em ```pokemon_info``` é armazenado os dados brutos, enquanto em  ```data``` há somente os dados que serão usados no decorrer do código. A principal diferença é que há centenas de dados em ```pokemon_info```, como dezenas de imagens e moves, então a variável ```data``` organiza-os para que sejam usados.

```python
pokemon_info = pokemon.get_pokemon_info(pokemon_name)
data = pokemon.main(pokemon_info)
``` 

Sobre a estrutura da interface gráfica, há uma tela inicial de 270x300, com o título POKEMON. Para a organização dos widgets foi utilizado um sistema de grid, que se expande desde a linha 0 até a 7, apenas o widget da imagem tem mais de uma linha, por isso foi usado o paramêtro ```rowspan=4```. 

Os widgets usados foram: Entry, Button e Label. Em ```Entry``` o usuário digita o nome de um Pokémon e em ```Button``` é executado a função ```search```, como visto na linha ```button = tk.Button(root, text="click!", command=search)```, a função preenche as Label com os dados de ```data```, substituindo os textos e o placeholder de uma imagem transparente.

Na imagem a seguir, pode-se ver um exemplo do código e da localização dos widgets.

INSERIR IMAGEM AQUI!!!!!

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
