import streamlit as st
import requests

st.set_page_config(
    page_title="WooHoo!!!",
    page_icon="🎨",
    layout="centered"
)

st.header("Pokémon Information App")

def fetch_pokemon_info(name):
    #name = st.text_input("Enter a Pokémon name:")
    st.write("Fetching... " + name)
    if name:
        pokemon_info = get_pokemon_info(name)
        if pokemon_info:
            st.write(f"Name: {pokemon_info['name']}")
            st.write(f"Height: {pokemon_info['height']} decimeters")
            st.write(f"Weight: {pokemon_info['weight']} kilograms")
            st.write(f"Abilities: {', '.join(pokemon_info['abilities'])}")
            st.write(f"Types: {', '.join(pokemon_info['types'])}")
            st.image(f"Sprites:{', '.join([pokemon_info['sprites']['front_shiny']])}")
        else:
            st.write("No Pokémon found with that name.")
    else:
        st.write("Please enter a Pokémon name.")
    st.info("This app uses the Pokémon API to fetch and display information about Pokémon.")
    
def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url, verify=False)
    st.write(response.status_code, response.text)    
    
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_info = {
            "name": pokemon_data["name"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
            "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]],
            "sprites": {
                "front_shiny": pokemon_data["sprites"]["front_shiny"]
            }
        }
        return pokemon_info
    elif response.status_code == 443:
        st.write("Unable to connect to the Pokémon API server.")
        return None
    else:
        return None
    


name = st.text_input("Enter a Pokémon name:")
if name:
    fetch_pokemon_info(name)