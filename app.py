from flask import Flask, render_template

app = Flask(__name__)

# Sample products and recommendations (replace with database or real data)
all_products = [' asparagus',
 'almonds',
 'antioxydant juice',
 'asparagus',
 'avocado',
 'babies food',
 'bacon',
 'barbecue sauce',
 'black tea',
 'blueberries',
 'body spray',
 'bramble',
 'brownies',
 'bug spray',
 'burger sauce',
 'burgers',
 'butter',
 'cake',
 'candy bars',
 'carrots',
 'cauliflower',
 'cereals',
 'champagne',
 'chicken',
 'chili',
 'chocolate',
 'chocolate bread',
 'chutney',
 'cider',
 'clothes accessories',
 'cookies',
 'cooking oil',
 'corn',
 'cottage cheese',
 'cream',
 'dessert wine',
 'eggplant',
 'eggs',
 'energy bar',
 'energy drink',
 'escalope',
 'extra dark chocolate',
 'flax seed',
 'french fries',
 'french wine',
 'fresh bread',
 'fresh tuna',
 'fromage blanc',
 'frozen smoothie',
 'frozen vegetables',
 'gluten free bar',
 'grated cheese',
 'green beans',
 'green grapes',
 'green tea',
 'ground beef',
 'gums',
 'ham',
 'hand protein bar',
 'herb & pepper',
 'honey',
 'hot dogs',
 'ketchup',
 'light cream',
 'light mayo',
 'low fat yogurt',
 'magazines',
 'mashed potato',
 'mayonnaise',
 'meatballs',
 'melons',
 'milk',
 'mineral water',
 'mint',
 'mint green tea',
 'muffins',
 'mushroom cream sauce',
 'napkins',
 'nonfat milk',
 'oatmeal',
 'oil',
 'olive oil',
 'pancakes',
 'parmesan cheese',
 'pasta',
 'pepper',
 'pet food',
 'pickles',
 'protein bar',
 'red wine',
 'rice',
 'salad',
 'salmon',
 'salt',
 'sandwich',
 'shallot',
 'shampoo',
 'shrimp',
 'soda',
 'soup',
 'spaghetti',
 'sparkling water',
 'spinach',
 'strawberries',
 'strong cheese',
 'tea',
 'tomato juice',
 'tomato sauce',
 'tomatoes',
 'toothpaste',
 'turkey',
 'vegetables mix',
 'water spray',
 'white wine',
 'whole weat flour',
 'whole wheat pasta',
 'whole wheat rice',
 'yams',
 'yogurt cake',
 'zucchini']
association_rules = {
    'milk': ['bread', 'butter'],
    'bread': ['butter', 'eggs'],
    'butter': ['bread', 'milk'],
    'eggs': ['cheese'],
    'cheese': ['milk']
}

@app.route('/')
def main_page():
    return render_template('index.html', products=all_products)

@app.route('/product/<product>')
def product_page(product):
    recommendations = association_rules.get(product, [])
    return render_template('product.html', product=product, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)