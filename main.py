import os
import string

films_titles = {
    "results": [
        {
            "imdb_id": "tt1201607",
            "title": "Harry Potter and the Deathly Hallows: Part 2"
        },
        {
            "imdb_id": "tt0241527",
            "title": "Harry Potter and the Sorcerer's Stone"
        },
        {
            "imdb_id": "tt0926084",
            "title": "Harry Potter and the Deathly Hallows: Part 1"
        },
        {
            "imdb_id": "tt0304141",
            "title": "Harry Potter and the Prisoner of Azkaban"
        },
        {
            "imdb_id": "tt0417741",
            "title": "Harry Potter and the Half-Blood Prince"
        },
        {
            "imdb_id": "tt0295297",
            "title": "Harry Potter and the Chamber of Secrets"
        },
        {
            "imdb_id": "tt0330373",
            "title": "Harry Potter and the Goblet of Fire"
        },
        {
            "imdb_id": "tt0373889",
            "title": "Harry Potter and the Order of the Phoenix"
        }
    ]
}

# Створення тек від A до Z в кожній директорії фільму
def create_folders(path):
    for letter in string.ascii_uppercase:
        folder_path = os.path.join(path, letter)
        os.makedirs(folder_path, exist_ok=True)

# Створення тек та файлів для кожного фільму
for film in films_titles["results"]:
    film_title = film["title"]
    film_directory = os.path.join("Harry Potter", film_title)
    create_folders(film_directory)  # Створюємо теки від A до Z

    # Список нагород для кожного фільму (можна замінити на ваші дані)
    awards_list = [
        {'award_name': 'Oscar', 'award': 'Best Achievement in Makeup'},
        {'award_name': 'Golden Globe', 'award': 'Best Original Score'},
        {'award_name': 'BAFTA', 'award': 'Best Production Design'},
        {'award_name': 'Cannes Film Festival', 'award': 'Best Director'}
        # Додайте сюди інші нагороди, які ви бажаєте створити файли
    ]

    for award in awards_list:
        # Отримання першої літери назви нагороди
        first_letter = award['award_name'][0].upper()

        # Шлях до теки з відповідною літерою
        letter_directory = os.path.join(film_directory, first_letter)

        # Шлях до файлу з назвою нагороди
        filename = os.path.join(letter_directory, f"{award['award_name']}.txt")

        # Запис назви номінації в файл
        with open(filename, 'a') as file:
            file.write(f"{award['award']}\n")
