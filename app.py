import json
from flask import Flask, render_template, request

with open('drink_data.json', 'r') as f:
    drink_data = json.load(f)

app = Flask(__name__)



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

@app.route('/')
def index():

    #ingredients = ['Gin', 'Vodka', 'Tequila', 'Triple Sec', 'Dry Vermouth', 'Campari', 'Sweet Vermouth', 'Lime Juice']
    liquors = ['Gin', 'White Rum', 'Spiced Rum', 'Vodka', 'Tequila', 'Whiskey', 'Brandy']
    #liqueurs = ['Absinthe', 'Amaretto', 'Amaro', 'Aperol', 'Benedictine', 'Cappelletti', 'Campari', 'Chambord', 'Chartreuse', 'Crème de Cacao (chocolate)', 'Crème de Cassis (black currant)', 'Crème de Menthe (mint)', 'Crème de Mûre (blackberry)', 'Crème de Noyaux (almond)', 'Coffee Liqueur (Kahlua, Tia Maria)', 'Drambuie', 'Jägermeister', 'Galliano', 'Hpnotiq', 'Irish Cream (Baileys)', 'Licor 43', 'Limoncello', 'Maraschino Liqueur', 'Midori', 'Triple Sec', 'Pastis', 'Pernod', "Pimm's", 'Peppermint Schnapps', 'Cinnamon Schnapps', 'Peach Schnapps', 'Sloe Gin', 'St Germain', 'Suze'] # Orange Liqueurs (triple sec) maybe more specified

    return render_template('index.html', ingredients=liquors)

@app.route('/find_drinks', methods=['POST'])
def find_drinks():
    selected_ingredients = request.form.getlist('ingredients')

    matched_drinks = get_matched_drinks(selected_ingredients)
    
    return render_template('results.html', matched_drinks=matched_drinks)

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

def get_matched_drinks(ingredients):
    matched_drinks = {}
    for drink, details in drink_data.items():
        
        if isinstance(details['ingredients'], list):
            if all(ingredient in details['ingredients'] for ingredient in ingredients):
                matched_drinks[drink] = details
        else:
            drink_ingredients = details['ingredients'].keys()
            if all(ingredient in drink_ingredients for ingredient in ingredients):
                matched_drinks[drink] = details
    return matched_drinks


if __name__ == "__main__":
    app.run(debug=True)