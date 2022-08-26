import random

spisok = ["соль", "162", "дружба", 'Петя']
empty_list = []
for item in spisok:
    rand_index = random.randint(0, len(empty_list))
    empty_list.insert(rand_index, item)
print(empty_list)


