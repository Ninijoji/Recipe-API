# Recipe-API
Recipe Search API
This repository contains a Python script that allows you to search for recipes using the Edamam API, store the recipe information in both  a SQLite database and a JSON file, and display notifications using the win10toast library.

Requirements
1. Python 3.x
2. requests library
3. win10toast library
4. SQLite3
5. JSON

Installation
1. Clone the repository.
2. Install the required libraries using pip.
3. Set up your Edamam API credentials.
4. Sign up for an account on [Edamam Developer](https://developer.edamam.com/) and obtain your API ID and API Key.
5. First run make_database.py to create database where recipes can be stored.
6. Run recipeAPI.py with API ID API key and keyword you are searching recipes for.

FEATURES
Recipe search: Enter a keyword to search for recipes.
Display recipe information: Print the recipe label, ingredients, and URL in the console.
Store in SQLite database: Store the recipe information in a SQLite database.
Store in JSON file: Store the recipe information in a structured JSON file (recipes.json).
Windows notifications: Show a Windows notification with the recipe details.
