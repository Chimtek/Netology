# ================== Открытие и чтение файла, запись в файл ===================================
# --------------------- Задание 1 ----------------------------------------------------

cook_book = {}
with open('recipes.txt', 'r', encoding='utf-8') as fl:
    data = fl.readlines()

step = 0
while step < len(data):
    line = data[step].strip('\n')
    if '|' not in line and line != '' and not line.isdigit():
        cook_book[line] = []
        count_ingr = int(data[step + 1].strip('\n'))
        for i in range(count_ingr):
            ingr_line = (data[step+2+i].strip('\n').split(' | '))
            cook_book[line].append({'ingredient_name': ingr_line[0], 'quantity': int(ingr_line[1]), 'measure': ingr_line[2]})
    step += 1

# ---------------------- Задача 2 ------------------------------------------
def get_shop_list_by_dishes(dishes, person_count):
    all_ingredients = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in all_ingredients:
                all_ingredients[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                  'quantity': int(ingredient['quantity']) * person_count}
            else:
                all_ingredients[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count

    for k, v in all_ingredients.items():
        print(k, v)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

