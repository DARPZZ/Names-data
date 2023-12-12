import json
import requests
from users import send_post_request
def post_data_from_csv():
    login_url = "http://localhost:5000/login"
    names_url = "http://localhost:5000/names"
    login_json_body = {"Email": "", "Password": ""}
    jsonl_file_path = "meme.json"

    with requests.Session() as session:
        login_response = session.post(login_url, json=login_json_body)

        if login_response.status_code == 200:
            print("Login successful.")

            with open(jsonl_file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    json_data = json.loads(line)
                    name = json_data["name"]
                    gender = json_data["gender"]
                    is_international = json_data["isInternational"]
                    popularity = json_data["popularity"]
                    occurrences = json_data["occurrences"]
                    names_json_body = {
                        "name": name,
                        "gender": gender,
                        "isInternational": is_international,
                        "popularity": popularity,
                        "occurrence": occurrences
                    }

                    names_response = session.post(names_url, json=names_json_body)

                    if names_response.status_code == 201:
                        print(f"API call for {name} successful. Response:{names_response.status_code}")
                    
                    else:
                        print(f"API call for {name} failed. Status code: {names_response.status_code}")

if __name__ == "__main__":
    send_post_request()
    post_data_from_csv()