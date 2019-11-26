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
'dairy': ['Low Fat Cheese Cubes', 'Plain Yogurt', 'Skim Milk', 'Cottage Cheese'],
'lean_protein':['Hummus', 'Hard-Boiled Egg', 'Nuts', 'Turkey', 'Tofu', 'Peanut Butter']
}
#This function takes a string  as a variable and will return a single meal for either breakfast, lunch, dinner, or snacks.
def meal_plan(ingredients):
    food = ''
    for meal in ingredients:
        food += random.choice(ingredients[meal])+' & '
    return food

print ''.join(meal_plan(snack))
#Code will print random items from from each input category and return something different each time.
#For example if user chooses snack, code will return one ingredient from fruits, one from whole_grains, one from vegetables, one from lean_protein, and one from dairy.
