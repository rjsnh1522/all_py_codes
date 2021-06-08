# number_of_days = int(input())
ingredients_cat = {
    'fat': [],
    'fiber': [],
    'carb': []
}

# number_of_days = int(input())
arra = ["CARBBeetroot", "FIBERCarrot", "FATOlive", "CARBCorn",
        "CARBPotato", "FIBERBroccoli", "FATEgg", "FIBERBeans", "FATCheese",
        "CARBRice", "FIBERSpinach", "FATOil"]
# arra = input().split()
current_rank = 1
for ingredient in arra:
    a = ingredient.lower()
    if 'fat' in a:
        ingredients_cat['fat'].append(ingredient)
    elif 'fiber' in a:
        ingredients_cat['fiber'].append(ingredient)
    elif 'carb' in a:
        ingredients_cat['carb'].append(ingredient)
    else:
        pass

    current_ingredients_length = len(ingredients_cat['fat']) + len(ingredients_cat['fiber']) + len(ingredients_cat['carb'])
    print(ingredients_cat)
    if current_ingredients_length >= 3:
        fat = len(ingredients_cat['fat'])
        fiber = len(ingredients_cat['fiber'])
        carb = len(ingredients_cat['carb'])
        if fat >= 2:
            fat1 = ingredients_cat['fat'].pop(0)
            fat2 = ingredients_cat['fat'].pop(0)
            if fat == 3:
                fat3 = ingredients_cat['fat'].pop(0)
                print("1", end="")
            elif fiber >= 1:
                fiber1 = ingredients_cat['fiber'].pop(0)
                print("1", end="")
            else:
                carb1 = ingredients_cat['carb'].pop(0)
                print("1", end="")
        elif carb >= 2:
            carb1 = ingredients_cat['carb'].pop(0)
            carb2 = ingredients_cat['carb'].pop(0)
            if carb == 3:
                ingredients_cat['carb'].pop(0)
                print("1", end="")
            elif fat >= 1:
                ingredients_cat['fat'].pop(0)
                print("1", end="")
            else:
                fiber1 = ingredients_cat['fiber'].pop(0)
                print("1", end="")
        elif fiber >= 2:
            fiber1 = ingredients_cat['fiber'].pop(0)
            fiber2 = ingredients_cat['fiber'].pop(0)
            if fiber == 3:
                ingredients_cat['fiber'].pop(0)
            elif fat >= 1:
                ingredients_cat['fat'].pop(0)
                print("1", end="")
            else:
                ingredients_cat['carb'].pop(0)
                print("1", end="")
        else:
            print("0", end="")
    else:
        print("0", end="")






# print(ingredients_cat)
