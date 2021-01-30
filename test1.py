
food_list = []
while True:
    food = input('ENTER A COMMEND ')
    if food != 'food':
        food_list.append(food)
    if food == 'food':
        print(food_list)
    