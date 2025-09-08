import json
import requests


def main():


    url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"


    data = {
        "UCID": "ejg37",
        "first_name": "Eric",
        "last_name": "Gomez",
        "github_username": "EJ8127",
        "discord_username": "oofberic",
        "favorite_cartoon": "Avatar: The Last Airbender",
        "favorite_language": "Python",
        "movie_or_game_or_book": "Interstellar",
        "section": "101",
    }


    headers = {"Content-Type": "application/json"}


    try:
        response = requests.post(url, headers=headers, json=data)
        print("Status:", response.status_code)
        print("Response:", response.text)
    except requests.exceptions.RequestException as error:
        print("Error", error)


if __name__ == "__main__":
    main()