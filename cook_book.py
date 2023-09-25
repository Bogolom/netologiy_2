
import os


with open('book_cook.txt', 'r', encoding='utf-8') as cook_file:
    cook_book = {}
    for string in cook_file:
        dish = string.strip()
        ingredients_count = int(cook_file.readline().strip())
        dish_dict = []
        for item in range(ingredients_count):
            ingredient_name, quantity, measure = cook_file.readline().strip().split('|')
            dish_dict.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish] = dish_dict
        cook_file.readline()
# print(cook_book[dish])


def get_shop_list_by_dishes(dishes, person_count):
    grocery_dict = {}
    for _dish in dishes:
        for ingredient in cook_book[_dish]:

            ingredient_list = dict([(ingredient['ingredient_name'],
                                     {'quantity': int(ingredient['quantity']) * person_count,
                                      'measure': ingredient['measure']})])

            if grocery_dict.get(ingredient['ingredient_name']) == 'None':
                _merger = (int(grocery_dict[ingredient['ingredient_name']]['quantity']) +
                           int(ingredient_list[ingredient['ingredient_name']]['quantity']))
                grocery_dict[ingredient['ingredient_name']]['quantity'] = _merger
            else:
                grocery_dict.update(ingredient_list)
    return grocery_dict

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос', 'Омлет', 'Запеченный картофель'], 5))

def get_info_and_writing_to_list(file_names):
    my_data = []
    for file in file_names:
        with open(file, encoding='utf-8') as f:
            lines = f.read().splitlines()
            my_data.append([file, len(lines)])
            my_data[len(my_data)-1] += lines
    my_data.sort(key=len)
    return my_data

def writing_info_to_file(my_data, my_file):
    with open('result.txt', 'w', encoding='utf-8') as f:
        for file in my_data:
            for elem in file:
                f.write(f'{elem}\n')
    file_path = os.path.join(os.getcwd(), my_file)
    return file_path

print(writing_info_to_file(get_info_and_writing_to_list(['1.txt', '2.txt', '3.txt']), 'result.txt'))