import requests
import json

def download_artwork(game: list):
    with open("secrets.json", "r") as file:
        data = json.load(file)


    base_url = "https://api.igdb.com/v4"
    client_id = data.get("client_id")
    access_token = data.get("response").get("access_token")
    header = {
        "Client-ID":client_id,
        "Authorization":f"Bearer {access_token}"
    }


    response = requests.post("https://api.igdb.com/v4/artworks/",headers=header,data=f'fields url; where game = ({",".join(game)});')


    with open("result.json","w") as file:
        json.dump(response.json(),file,indent=4)


if __name__ == "__main__":
    with open("secrets.json", "r") as file:
        data = json.load(file)


    base_url = "https://api.igdb.com/v4"
    client_id = data.get("client_id")
    access_token = data.get("response").get("access_token")
    header = {
        "Client-ID":client_id,
        "Authorization":f"Bearer {access_token}"
    }

    game = ["119277", "17000", "119133"]

    response = requests.post("https://api.igdb.com/v4/artworks/",headers=header,data=f'fields url; where game = (119277,17000,119133); limit 1;') #{", ".join(game)}
    # Issue: Getting multiple cover img for a single game

    with open("result.json","w") as file:
        json.dump(response.json(),file,indent=4)