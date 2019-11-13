import random
#This code will be used as a healthy meal generator for breakfast, lunch, dinner, and snacks.
#Code will build a meal taking food choices from variables.
breakfast = {
'whole_grains':['wheat toast', 'quinoa', 'oatmeal', 'whole grain toast', 'whole grain cereal', 'whole grain bagel', 'whole grain english muffin'],
'fruits': ['apples', 'oranges', 'grapefruit', 'berries', 'grapes', 'melon', 'banana', 'peaches'],
'dairy': ['skim milk', 'plain yogurt', 'cheese'],
'lean_protein': ['eggs', 'turkey bacon', 'turkey sausage', 'nuts'],
'vegetables': ['broccoli', 'cauliflower', 'tomato', 'carrots', 'spinach', 'zucchini', 'mushrooms', 'lettuce', 'asparagus', 'celery', 'peppers']
}
lunch = {
'whole_grains': ['whole grain bread', 'brown rice', 'whole wheat pasta', 'quinoa'],
'fruits': ['oranges', 'apples', 'berries', 'grapes', 'melon', 'mango', 'peaches', 'banana', 'kiwi'],
'vegetables': ['broccoli', 'cauliflower', 'tomato', 'carrots', 'spinach', 'zucchini', 'mushrooms', 'lettuce', 'asparagus', 'celery', 'peppers'],
'lean_protein': ['fish', 'chicken', 'shellfish', 'nuts', 'turkey', 'tofu', 'beans', 'eggs', 'turkey bacon', 'turkey sausage'],
'dairy': ['plain yogurt', 'cheese', 'skim milk']
}
dinner = {
'lean_protein':['fish', 'chicken', 'shellfish', 'nuts', 'turkey', 'tofu', 'beans'],
'vegetables': ['broccoli', 'cauliflower', 'tomato', 'carrots', 'spinach', 'zucchini', 'mushrooms', 'lettuce', 'asparagus', 'celery', 'peppers'],
'dairy': ['cheese', 'plain yogurt', 'skim milk'],
'fruits': ['oranges', 'apples', 'berries', 'grapes', 'melon', 'mango', 'peaches', 'banana', 'kiwi'],
'whole_grains': ['whole grain bread', 'brown rice', 'whole wheat pasta', 'quinoa']
}
snack = {
'fruits':['oranges', 'apples', 'berries', 'grapes', 'melon', 'mango', 'peaches', 'banana', 'kiwi'],
'whole_grains':['bran muffin', 'popcorn', 'whole wheat crackers', 'whole wheat toast'],
'vegetables':['carrots', 'celery', 'peppers', 'tomatoes', 'broccoli', 'cauliflower'],
'dairy': ['cheese', 'plain yogurt', 'skim milk'],
'lean_protein':['fish', 'chicken', 'shellfish', 'nuts', 'turkey', 'tofu', 'beans']
}
#This function takes the string 'meal' as a variable and will return a single meal for either breakfast, lunch, dinner, and snacks.
def meal_plan(meal):
    breakfast = ''
    lunch = ''
    dinner = ''
    snack = ''
def meal_plan(ingredients):
    breakfast_dict = {'[]'}
    lunch_dict = {'[]'}
    dinner_dict = {'[]'}
    snack_dict = {'[]'}
    for breakfast_dict in random.sample(breakfast_dict.items(),k=5):
        print breakfast_dict
    for lunch_dict in random.sample(lunch_dict.items(),k=5):
        print lunch_dict
    for dinner_dict in random.sample(dinner_dict.items(),k=5):
        print dinner_dict
    for snack_dict in random.sample(snack_dict.items(),k=5):
        print snack_dict
