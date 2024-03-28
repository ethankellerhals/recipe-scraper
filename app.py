import csv
import json
from flask import Flask, render_template, request

with open('drink_data.json', 'r') as f: 
    drink_data = json.load(f)
# drinks = []
# with open('all_drinks.csv', newline='', encoding='utf-8-sig') as f:
#     csvReader = csv.reader(f)
#     for row in csvReader:
#         drinks.append(row)

#print(drinks)
#print(drinks[1][1]) # drink name
# for i in range(1, len(drinks)):
#     print(drinks[i][1])

app = Flask(__name__)

@app.route('/')
def index():
    # different types of rums (spiced, white)
    liquors = ['Beer', 'Bourbon', 'Brandy', 'Gin', 'Rum', 'Sake', 'Tequila', 'Vodka', 'Whiskey', 'Wine']
    liqueurs = ['Absinthe', 'Amaretto', 'Amaro', 'Aperol', 'Benedictine', 'Cappelletti', 'Campari', 'Chambord', 'Chartreuse', 'Crème de Cacao (chocolate)', 'Crème de Cassis (black currant)', 'Crème de Menthe (mint)', 'Crème de Mûre (blackberry)', 'Crème de Noyaux (almond)', 'Coffee Liqueur (Kahlua, Tia Maria)', 'Drambuie', 'Jägermeister', 'Galliano', 'Hpnotiq', 'Irish Cream (Baileys)', 'Licor 43', 'Limoncello', 'Maraschino Liqueur', 'Midori', 'Triple Sec', 'Pastis', 'Pernod', "Pimm's", 'Peppermint Schnapps', 'Cinnamon Schnapps', 'Peach Schnapps', 'Sloe Gin', 'St Germain', 'Suze']
    mixers = ['Bloody Mary Mix', 'Club Soda', 'Coconut Milk', 'Coke', 'Cranberry Juice', 'Cream', 'Ginger Ale', 'Ginger Beer', 'Grapefruit Juice', 'Grenadine',  'Lemon Juice', 'Lemon-Lime Soda', 'Lime Juice', 'Milk', 'Orange Juice', 'Pineapple Juice', 'Simple Syrup', 'Sour Mix', 'Tomato Juice', 'Tonic Water']
    sodas = ['Club Soda', 'Coke', 'Ginger Ale', 'Ginger Beer', '7-Up', 'Sprite', 'Tonic Water']
    juices = ['Apple Juice', 'Cranberry Juice', 'Grapefruit Juice', 'Lemon Juice', 'Lime Juice', 'Orange Juice', 'Pineapple Juice', 'Tomato Juice']
    others = ['Celery Salt', 'Tabasco', 'Horseradish', 'Worcestershire Sauce', 'Soy Sauce', 'Sriracha', 'Bitters', 'Simple Syrup', 'Grenadine', 'Mint', 'Sugar', 'Salt', 'Pepper', 'Egg White', 'Cream', 'Coconut Milk', 'Milk', 'Coffee', 'Tea', 'Hot Chocolate', 'Honey', 'Maple Syrup', 'Agave Nectar', 'Lemonade', 'Sour Mix']
    garnishes = ['Celery', 'Cherry', 'Lemon Wedge', 'Lime Wedge', 'Mint', 'Nutmeg', 'Olives', 'Orange Wedge']

    return render_template('index.html', liquors=liquors, mixers=mixers, garnishes=garnishes)

@app.route('/find_drinks', methods=['POST'])
def find_drinks():
    selected_liquors = request.form.getlist('liquors')
    selected_mixers = request.form.getlist('mixers')
    selected_garnishes = request.form.getlist('garnishes')
    
    matched_drinks = get_matched_drinks(selected_liquors, selected_mixers, selected_garnishes)
    
    return render_template('results.html', matched_drinks=matched_drinks)

def get_matched_drinks(selected_liquors, selected_mixers, selected_garnishes):
    matched_drinks = {}
    i = j = k = 0


    # for liquor in selected_liquors:
    #     for drink_list in drink_data.values():
    #         for drink in drink_list:
                
    #             if all(liquor.lower() in ingredient.lower() for ingredient in drink['ingredients']):
    #                 matched_drinks[drink['title']] = drink
    #             elif any(liquor.lower() in ingredient.lower() for ingredient in drink['ingredients']):
    #                 matched_drinks[drink['title']] = drink
    liquor_amount = len(selected_liquors)
    mixer_amount = len(selected_mixers)
    garnish_amount = len(selected_garnishes)
    for category, drinks in drink_data.items():
        # if category == selected_liquors[i]:
        #     for drink in drinks:
        #         matched_drinks[drink['title']] = drink
                
        #     if i < len(selected_liquors) - 1:
        #         i += 1
        if mixer_amount == 0 and garnish_amount == 0:
            if liquor_amount == 1:
                if category == selected_liquors[0]:
                    for drink in drinks:
                        matched_drinks[drink['title']] = drink
        else:
            for drink in drinks:
                if any(ingredient.lower() in [liquor.lower() for liquor in selected_liquors] for ingredient in drink['ingredients']) or any(ingredient.lower() in [mixer.lower() for mixer in selected_mixers] for ingredient in drink['ingredients']) or any(ingredient.lower() in [garnish.lower() for garnish in selected_garnishes] for ingredient in drink['ingredients']):
                    matched_drinks[drink['title']] = drink


        # else:
        #     for drink in drinks:
        #         if selected_mixers[j] in drink['ingredients']:
        #             matched_drinks[drink['title']] = drink
        #             if j < len(selected_mixers) - 1:
        #                 j += 1
        #         elif selected_garnishes[k] in drink['ingredients']:
        #             matched_drinks[drink['title']] = drink
        #             if k < len(selected_garnishes) - 1:
        #                 k += 1


    print(matched_drinks)
    return matched_drinks

if __name__ == "__main__":
    app.run(debug=True)

        # for drink in drinks:
        #     drink_title = drink['title']
        #     drink_ingredients = drink['ingredients']
        #     if "gin" in drink_ingredients or "Gin" in drink_title:
        #         print(drink_title)
        #     if selected_liquors in drink_ingredients:
        #         matched_drinks[drink_title] = drink

    #print(drink_data.items())
    

    # for category, drinks in drink_data.items():
    #     for drink in drinks:
    #         drink_title = drink['title']
    #         drink_ingredients = drink['ingredients']
    #         if all(ingredient in drink_ingredients for ingredient in selected_liquors) \
    #                 and all(ingredient in drink_ingredients for ingredient in selected_mixers) \
    #                 and all(ingredient in drink_ingredients for ingredient in selected_garnishes):
    #             matched_drinks[drink_title] = drink

# def get_matched_drinks(selected_liquors, selected_mixers, selected_garnishes):

#     matched_drinks = {}

#     for drink, details in drink_data.items():
#         drink_ingredients = details['ingredients']
#         if all(ingredient in drink_ingredients for ingredient in selected_liquors) \
#             and all(ingredient in drink_ingredients for ingredient in selected_mixers) \
#             and all(ingredient in drink_ingredients for ingredient in selected_garnishes):
#             matched_drinks[drink] = details

#     return matched_drinks



 # Orange Liqueurs (triple sec) maybe more specified
    #ingredients = ['Gin', 'Vodka', 'Tequila', 'Triple Sec', 'Dry Vermouth', 'Campari', 'Sweet Vermouth', 'Lime Juice']

    # for drink, details in drink_data.items():
        
    #     if isinstance(details['ingredients'], list):
    #         if all(ingredient in details['ingredients'] for ingredient in ingredients):
    #             matched_drinks[drink] = details
    #     else:
    #         drink_ingredients = details['ingredients'].keys()
    #         if all(ingredient in drink_ingredients for ingredient in ingredients):
    #             matched_drinks[drink] = details
    # return matched_drinks

# def get_matched_drinks(ingredients):
#     #matched_drinks = [drink for drink, ingredients_list in drink_data.items() if set(ingredients).issubset(ingredients_list)]

#     matched_drinks = {}
#     for drink, details in drink_data.items():
#         drink_ingredients = details['ingredients'].keys()
#         if all(ingredient in drink_ingredients for ingredient in ingredients):
#             matched_drinks[drink] = details
#         # if set(ingredients).issubset(details['ingredients']):
#         #     matched_drinks[drink] = details
#     # matched_drinks = {drink: details for drink, details in drink_data.items() if set(ingredients).issubset(details['ingredients'])}
#     return matched_drinks

# doesn't work


# negroni garnish with orange peel
# martini, 1 dash orange bitters (optional)
# gin and tonic, garnish lime wedge
# moscow mule, garnish lime wedge

# drink_data = {
#     'Negroni': {
#         'ingredients': {'Gin': '1 oz', 'Campari': '1 oz', 'Sweet Vermouth': '1 oz'},
#         'instructions': '1. Add the gin, Campari, and sweet vermouth to a mixing glass filled with ice, and stir until well-chilled. \n 2. Strain into a rocks glass over a large ice cube. \n 3. Garnish with an orange peel.'
#     },
#     'Margarita': {
#         'ingredients': {'Tequila': '2 oz', 'Triple Sec': '1 oz', 'Lime Juice': '1 oz'},
#         'instructions': '1111'
#     },
#     'Martini': {
#         'ingredients': {'Gin': '2 oz', 'Dry Vermouth': '1 oz'},
#         'instructions': 'aas'
#     },
#     'Mojito': {
#         'ingredients': {'White Rum': '1 1/2 oz', 'Lime Juice': '1 oz', 'Sugar': '2 tsp', 'Mint': '6 leaves', 'Club Soda': '1/2 cup, or as needed'},
#         'instructions': 'asas'
#     },
#     'Screwdriver': {
#         'ingredients': {'Vodka': '1 3/4 oz', 'Orange Juice': '3 1/2 oz'},
#         'instructions': 'asasdsa'
#     },
#     'Gin & Tonic': {
#         'ingredients': {'Gin': '3 oz', 'Lime Juice': '1/2 oz', 'Tonic Water': '4 oz'},
#         'instructions': 'asd'
#     },
#     'Moscow Mule': {
#         'ingredients': {'Vodka': '1 1/2 oz', 'Lime Juice': '1/2 oz', 'Ginger Beer': '1/2 cup'},
#         'instructions': 'asdasd'
#     }
# }