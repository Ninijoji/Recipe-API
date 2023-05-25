import requests
import json
import sqlite3
from win10toast import ToastNotifier


def insert_recipe_json(label, ingredients, url):
    recipe_data = {
        'label': label,
        'ingredients': ingredients,
        'url': url
    }

    with open('recipes.json', 'a') as json_file:
        json.dump(recipe_data, json_file)
        json_file.write('\n')


def insert_recipe_db(label, ingredients, url):
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO recipes (label, ingredients, url)
        VALUES (?, ?, ?)
    ''', (label, json.dumps(ingredients), url))

    conn.commit()
    conn.close()


def search_recipes(keyword, app_id, app_key):
    url = "https://api.edamam.com/search"
    params = {
        "q": keyword,
        "app_id": app_id,
        "app_key": app_key
    }

    response = requests.get(url, params=params)

    if response.ok:
        data = response.json()
        hits = data.get('hits', [])

        if not hits:
            print(f"No recipes found for the keyword: {keyword}")
        else:
            toaster = ToastNotifier()
            recipe_count = 0
            for hit in hits:
                recipe = hit['recipe']

                label = recipe['label']
                ingredients = [ingredient['text'] for ingredient in recipe['ingredients']]
                url = recipe['url']

                print("Recipe:", label)
                print("Ingredients:")
                for ingredient in ingredients:
                    print(ingredient)
                print("Recipe URL:", url)
                print()

                insert_recipe_json(label, ingredients, url)
                insert_recipe_db(label, ingredients, url)

                recipe_count += 1

            if recipe_count > 0:
                toaster.show_toast("Success", f"{recipe_count} recipes have been added to the JSON file and database", duration=5)
            else:
                toaster.show_toast("No Recipes Found", f"No recipes found for the keyword: {keyword}", duration=5)

    else:
        print("Error occurred while fetching recipes.")
        print("Response Headers:", response.headers)

#Usage Example(გამოძახების ერთ-ერთ მაგალითი აქ "Chicken"-ის ნაცვლად ნებისმიერი ინგრედიენტი შეგვიძლია შევიყვანოთ")
app_id = "22f3a72e"
app_key = "212aeb1cc1f450d8066d5a63dce00b30"
search_recipes("potato", app_id, app_key)














