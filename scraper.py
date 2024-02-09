# import requests
# from bs4 import BeautifulSoup
# import json

# def get_drink_categories():
#     url = 'https://en.wikibooks.org/wiki/Bartending/Cocktails'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     categories = []
#     for category_link in soup.select('ul li a'):
#         if "Category:" in category_link['href']:
#             categories.append(category_link.text.strip())
#     return categories

# def get_drink_recipes(category_url):
#     response = requests.get(category_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     drink_recipes = []
#     for recipe_link in soup.select('.mw-category ul li a'):
#         if "/wiki/Bartending/Cocktails/" in recipe_link['href']:
#             drink_recipes.append(recipe_link['href'])
#     return drink_recipes

# def get_recipe(recipe_url):
#     response = requests.get(f"https://en.wikibooks.org{recipe_url}")
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     drink_name = soup.find('h1', class_='firstHeading').text.strip()
#     drink_name = drink_name.replace('Bartending/Cocktails/', '')
#     ingredients_title = soup.find('span', {'id': 'Ingredients'})
#     if ingredients_title:
#         ingredients = ingredients_title.find_next('ul')
#         ingredient_list = [ingredient.text.strip() for ingredient in ingredients.find_all('li')]
#     else:
#         ingredient_list = []
        
#     garnishes_title = soup.find('span', {'id': 'Garnishes'})
#     if garnishes_title:
#         garnishes = garnishes_title.find_next('ul')
#         garnish_list = [garnish.text.strip() for garnish in garnishes.find_all('li')]
#     else:
#         garnish_list = []

#     instructions_title = soup.find('span', {'id': 'Instructions'})
#     if instructions_title:
#         instructions = instructions_title.find_next('ol')
#         if instructions:
#            instruction_steps = [step.text.strip() for step in instructions.find_all('li')]
#         else:
#             instruction_steps = []
#     else:
#         instruction_steps = []

#     return {
#         'title': drink_name,
#         'ingredients': ingredient_list,
#         'instructions': instruction_steps,
#         'garnishes': garnish_list
#     }

# def main():
#     organized_data = {}
#     categories = get_drink_categories()
#     for category in categories:
#         category_url = f"https://en.wikibooks.org/wiki/Category:{category.replace(' ', '_')}"
#         drink_recipes = get_drink_recipes(category_url)
#         organized_data[category] = {}
#         for recipe_url in drink_recipes:
#             recipe_data = get_recipe(recipe_url)
#             organized_data[category][recipe_data['title']] = recipe_data
#     print(json.dumps(organized_data, indent=4))
#     with open('drink_recipes.json', 'w') as f:
#         json.dump(organized_data, f, indent=4)

# if __name__ == "__main__":
#     main()

import requests
import json
from bs4 import BeautifulSoup

def get_drink_categories():
    url = 'https://en.wikibooks.org/wiki/Bartending/Cocktails'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    categories = []
    
    for category_link in soup.select('ul li a'):
        if "Category:" in category_link['href']:
            categories.append(category_link.text.strip())
    
    return categories

def get_drink_recipes(category_url):
    response = requests.get(category_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    drink_recipes = []

    for recipe_link in soup.select('.mw-category ul li a'):
        if "/wiki/Bartending/Cocktails/" in recipe_link['href']:
            drink_recipes.append(recipe_link['href'])
    
    return drink_recipes

def get_recipe(recipe_url):
    response = requests.get(f"https://en.wikibooks.org{recipe_url}")
    soup = BeautifulSoup(response.text, 'html.parser')

    drink_name = soup.find('h1', class_='firstHeading').text.strip()
    drink_name = drink_name.replace('Bartending/Cocktails/', '')

    ingredients_title = soup.find('span', {'id': 'Ingredients'})

    if ingredients_title:
        ingredients = ingredients_title.find_next('ul')
        ingredient_list = [ingredient.text.strip() for ingredient in ingredients.find_all('li')]
    else:
        ingredient_list = []

    garnishes_title = soup.find('span', {'id': 'Garnishes'})

    if garnishes_title:
        garnishes = garnishes_title.find_next('ul')
        garnish_list = [garnish.text.strip() for garnish in garnishes.find_all('li')]
    else:
        garnish_list = []

    instructions_title = soup.find('span', {'id': 'Instructions'})

    if instructions_title:
        instructions = instructions_title.find_next('ol')
        if instructions:
            instruction_steps = [step.text.strip() for step in instructions.find_all('li')]
        else:
            instruction_steps = []
    else:
        instruction_steps = []
    
    return {
        'title': drink_name,
        'ingredients': ingredient_list,
        'instructions': instruction_steps,
        'garnishes': garnish_list
    }

def main():
    drink_data = {}
    categories = get_drink_categories()

    for category in categories:
        category_url = f"https://en.wikibooks.org/wiki/Category:{category}"
        drink_recipes = get_drink_recipes(category_url)

        for recipe in drink_recipes:
            recipe_data = get_recipe(recipe)
            recipe_data['category'] = category
            for ingredient in recipe_data['ingredients']:
                if ingredient not in drink_data:
                    drink_data[ingredient] = []
                drink_data[ingredient].append(recipe_data)

    print(json.dumps(drink_data, indent=4))
    with open('drink_recipes.json', 'w') as f:
        json.dump(drink_data, f, indent=4)

if __name__ == '__main__':
    main()
