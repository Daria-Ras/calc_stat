# Код печатает о каждом из друзей такое сообщение "<имя друга> живёт в городе <название города>".
friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']

friends = {}
for i in range(0, len(friends_names)):
    friends[friends_names[i]] = friends_cities[i]
print('Лена живет в городе ' + friends['Лена'])
