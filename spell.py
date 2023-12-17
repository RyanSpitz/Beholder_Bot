import requests
import discord

def fetch_spell_data(spellName):
    # The url to the website i am using
    api_url = "https://api.open5e.com/v1/spells/"
    api_url = api_url + spellName + "/?format=json"
    try:
        # Make the API request
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            spell_data = response.json()
            #print(spell_data)
            return spell_data
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        return None

def create_spell_Embed(spellJson):
    # Take the results from fetch_spell_data
    embed = discord.Embed(
        title=spellJson["name"],
        description=spellJson["desc"]
    )

    return embed

