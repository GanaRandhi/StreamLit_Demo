import streamlit as st
import requests

st.set_page_config(
    page_title="Wooo!!!",
    page_icon="🎨",
    layout="wide"
)

st.header("Pokémon Information App")  
#st.write("Press Enter to fetch the Pokémon's information!", key="fetch_pokemon_info")
#if st.button("Fetch Pokémon Info", key="fetch_pokemon_info"):

def fetch_pokemon_info():
    name = st.text_input("Enter a Pokémon name:")
    st.write("Fetching... " + name)
    if name:
        pokemon_info = get_pokemon_info(name)
        if pokemon_info:
            st.write(f"Name: {pokemon_info['name']}")
            st.write(f"Height: {pokemon_info['height']} decimeters")
            st.write(f"Weight: {pokemon_info['weight']} kilograms")
            st.write(f"Abilities: {', '.join(pokemon_info['abilities'])}")
            st.write(f"Types: {', '.join(pokemon_info['types'])}")
            st.image(f"Sprites:{', '.join([pokemon_info['sprites']['front_default']])}")
        else:
            st.write("No Pokémon found with that name.")
    
def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_info = {
            "name": pokemon_data["name"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
            "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]],
            "sprites": {
                "front_default": pokemon_data["sprites"]["front_default"]
            }
        }
        return pokemon_info
    else:
        return None
    


#name = st.text_input("Enter a Pokémon name:")
#st.write("Press Enter to fetch the Pokémon's information!", key="fetch_pokemon_info")
#if st.button("Fetch Pokémon Info"):
fetch_pokemon_info()