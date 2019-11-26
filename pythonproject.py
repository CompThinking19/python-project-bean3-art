import random
#This code will be used as a healthy meal generator for breakfast, lunch, dinner, and snacks.
#Code will build a meal taking food choices from variables.
#Food choices come from the Harvard Healthy Eating Food Pyramid.
breakfast = {
'whole_grains':['Wheat Toast', 'Quinoa', 'Oatmeal', 'Whole Grain Toast', 'Whole Grain cereal', 'Whole Grain Bagel', 'Whole Grain English Muffin'],
'fruits': ['Apples', 'Oranges', 'Grapefruit', 'Berries', 'Grapes', 'Melon', 'Banana', 'Peaches'],
'dairy': ['Skim Milk', 'Plain Greek Yogurt', 'Low-fat Cream Cheese'],
'lean_protein': ['Eggs', 'Turkey Bacon', 'Turkey Sausage', 'Nuts'],
'vegetables': ['Broccoli', 'Tomato', 'Spinach', 'Zucchini', 'Mushrooms', 'Asparagus', 'Peppers']
}
lunch = {
'whole_grains': ['Whole Grain Bread', 'Brown Rice', 'Whole Wheat Pasta', 'Quinoa'],
'fruits': ['Oranges', 'Apples', 'Berries', 'Grapes', 'Melon', 'Mango', 'Peaches', 'Banana', 'Kiwi'],
'vegetables': ['Broccoli', 'Cauliflower', 'Tomato', 'Carrots', 'Spinach', 'Zucchini', 'Mushrooms', 'Lettuce', 'Asparagus', 'Celery', 'Peppers'],
'lean_protein': ['Fish', 'Chicken', 'Shellfish', 'Nuts', 'Turkey', 'Tofu', 'Beans', 'Hard Boiled Egg', 'Turkey Bacon'],
'dairy': ['Plain Greek Yogurt', 'Low-fat Cheese', 'Skim Milk']
}
dinner = {
'lean_protein':['Fish', 'Chicken', 'Shellfish', 'Nuts', 'Turkey', 'Tofu', 'Beans'],
'vegetables': ['Broccoli', 'Cauliflower', 'Tomato', 'Carrots', 'Spinach', 'Zucchini', 'Mushrooms', 'Lettuce', 'Asparagus', 'Celery', 'Peppers'],
'dairy': ['Low-fat Cheese', 'Plain Greek Yogurt', 'Skim Milk'],
'fruits': ['Oranges', 'Apples', 'Berries', 'Grapes', 'Melon', 'Mango', 'Peaches', 'Banana', 'Kiwi'],
'whole_grains': ['Whole Grain Bread', 'Brown Rice', 'Whole Wheat Pasta', 'Quinoa']
}
snack = {
'fruits':['Oranges', 'Apples', 'Berries', 'Grapes', 'Melon', 'Mango', 'Peaches', 'Banana', 'Kiwi'],
'whole_grains':['Bran Muffin', 'Popcorn', 'Whole Wheat Crackers', 'Whole Wheat Toast'],
'vegetables':['Carrots', 'Celery', 'Peppers', 'Tomatoes', 'Broccoli'],
'dairy': ['Low-fat Cheese Cubes', 'Plain Greek Yogurt', 'Skim Milk'],
'lean_protein':['Hummus', 'Chicken', 'Nuts', 'Turkey', 'Tofu']
}
#This function takes ingredients as a variable and will return a single meal for either breakfast, lunch, dinner, or snack.
def meal_plan(ingredients):
    food = ' '
    meal = ' & '.join(food)
    for meal in ingredients:
        food += random.choice(ingredients[meal])+' & '
    return food
print ''.join(meal_plan(dinner))
#When user inputs meal choice whether breakfast, lunch, dinner, or snack, code will return a random meal for them.
#Printed meal will consist of a fruit, a vegetable, a whole_grain, a dairy product, and a lean_protein.
