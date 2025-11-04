import pytest
import pokemon


def test_names():
    raw_data = pokemon.get_pokemon_info("Pikachu")
    data = pokemon.main(raw_data)

    assert data["name"].lower() == "pikachu"
    assert data["id"] == 25
    assert data["weight"] == 60
    assert data["height"] == 4
    assert data["color"].lower() == "yellow"
    assert data["ability"].lower() == "static"


def test_error():
    raw_data = pokemon.get_pokemon_info("Pikachuuu")
    data = pokemon.main(raw_data)

    with pytest.raises(TypeError):
        data["name"]