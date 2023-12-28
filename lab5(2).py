# вариант 9
import requests
base_url = "https://rickandmortyapi.com/api"

response = requests.get(f"{base_url}/character")


if response.status_code == 200:
    data = response.json()

    results = data["results"]

    num_fields = 5
    for character in results:
        if num_fields <= 0:
            break


        print("Имя: ", character["name"])
        print("Статус: ", character["status"])
        print("Вид: ", character["species"])
        print("Пол: ", character["gender"])
        print("Местоположение: ", character["location"]["name"])
        print("$$$$$$$$$$$$$$$$$$$")


        num_fields -= 1
else:
    print("error")