import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data{response.status_code}")

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