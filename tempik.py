from collections import defaultdict
from enum import Enum
###################################################
# dicts merging
# uno = {'id': 69, 'name': 'olaf', 'nick': 'okap'}
# dos = {'rank': 1, 'age': 13}
# tres = {'s_animal': 'owl', 'id': 3}
#
# # id = 3
# al_final = {**uno, **dos, **tres}
#
# # id = 69
# # al_final = {**dos, **tres, **uno}
#
# print(al_final)

###################################################
# safer item access

# # Exception
# try:
#     print(dos['age'])
#     print(dos['id'])
# except Exception as x:
#     print("Oops! {}".format(x))
#
# # Safety None
# print(dos.get('age'))
# print(dos.get('year'))
#
# # Safety w value
# print(dos.get('age', 0))
# print(dos.get('year', '-'))
#
# # Default dict
# dos = defaultdict(lambda: "MISSING", dos)
# print(dos['age'])
# print(dos['year'])
###################################################
# switch

# def main():
#     text = input("Which direction I should make [u, d, l, r]? ")
#     mov = Move.pars(text)
#
#     print("Your choice was: {}".format(mov))
#
#     # Create char
#     # oliphant = Char("Kevin")
#
# class Move(Enum):
#     Up = 1
#     Down = 2
#     Left = 3
#     Right = 4
#
#     def pars(text: str):
#         if not text:
#             return None
#
#         text = text.strip().lower()
#         pars_dicti = {
#             'u': Move.Up, 'd': Move.Down, 'l': Move.Left, 'r': Move.Right}
#
#         return pars_dicti.get(text)
#
#         # if text == 'u':
#         #     return Move.Up
#         #
#         # if text == 'd':
#         #     return Move.Down
#         #
#         # if text == 'l':
#         #     return Move.Left
#         #
#         # if text == 'r':
#         #     return Move.Right
#         #
#         # return None
#
# class Char:
#     def __init__(self, name):
#         self.name = name
#
#     def move(self, direction: Move):
#         print("Character {} now moves {}".format(self.name, direction))
#
# if __name__ == '__main__':
#     main()
###################################################
############# Generators & Collections ############
###################################################
# Custom iterations
# class Kosik:
#     def __init__(self):
#         self.items = []
#
#     def __iter__(self):
#         # easy:     return self.items.__iter__()
#         sorted_items = sorted(self.items, key=lambda b: -b.price)
#         #           return sorted_items.__iter__()
#         for a in sorted_items:
#             yield a
#
#
#     def add_item(self, item):
#         self.items.append(item)
#
#
# class Zbozi:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# # Create Kosik se Zbozi(m)
# billa = Kosik()
# billa.add_item(Zbozi("kruti", 69))
# billa.add_item(Zbozi("trenky", 16.5))
# billa.add_item(Zbozi("susenky", 53.69))
#
# # Vyskladej zbozi na pult
# print("Zbozi v Kosiku jest: ")
# for it in billa:
#     print("--- {} za {} Kc".format(it.name, it.price))
###################################################
# Testing for containment

# el_list = [1, 1, 2, 3, 5, 8, 13, 21]
# el_set = {1, 1, 2, 3, 5, 8, 13}
# el_dict = {1: "one", 2: "two", 3: "three", 5: "five", 8: "eight"}
#
# los_numeros = int(input("Enteros numeros en fibonaccios: "))
#
# print("The {} is in list.".format(los_numeros) if los_numeros in el_list else "No es possible!")
# print("The {} is in set.".format(los_numeros) if los_numeros in el_set else "No es possible!")
# print("The {} is in dict.".format(los_numeros) if los_numeros in el_dict else "No es possible!")
#
# blabol = "Custom iteration and your types."
#
# word = input("Slovo: ")
#
# print("The {} rly xsist!".format(word) if word in blabol else "Nope / Nein / Nyet!")
###################################################
# yield and generators
# def classic_fibonacci(limit):
#     nums = []
#     current, nxt = 0, 1
#
#     while current < limit:
#         current, nxt = nxt, nxt + current
#         nums.append(current)
#
#     return nums
#
#
# def generator_fibonacci():
#     current, nxt = 0, 1
#
#     while True:
#         current, nxt = nxt, nxt + current
#         yield current
#
#
# if __name__ == '__main__':
#
#     print("Classic")
#     for m in classic_fibonacci(100):
#         print(m, end=', ')
#     print()
#
#     print("generator")
#     for m in generator_fibonacci():
#         print(m, end=', ')
#         if m > 100:
#             break
#     print()
###################################################
# inline generators via expression
# import collections
# import uuid
#
# Mereni = collections.namedtuple('Mereni', 'id x y hodnota')
#
# namereno = [
#     Mereni(str(uuid.uuid4()), 1, 1, 72),
#     Mereni(str(uuid.uuid4()), 2, 1, 40),
#     Mereni(str(uuid.uuid4()), 3, 1, 11),
#     Mereni(str(uuid.uuid4()), 2, 1, 90),
#     Mereni(str(uuid.uuid4()), 2, 2, 60),
#     Mereni(str(uuid.uuid4()), 2, 3, 73),
#     Mereni(str(uuid.uuid4()), 3, 1, 40),
#     Mereni(str(uuid.uuid4()), 3, 2, 90),
#     Mereni(str(uuid.uuid4()), 3, 3, 90)
# ]
#
# # generator - vypise IDcka mereni, ktere maj hodnotu vetsi jak 70
# nejv_mereni_gen = (
#     mer.id
#     for mer in namereno
#     if mer.hodnota > 70
# )
#
# print(nejv_mereni_gen)
#
# # list - vypise IDcka mereni, ktere maj hodnotu vetsi jak 70
# nejv_mereni_list = [
#     mer.id
#     for mer in namereno
#     if mer.hodnota > 70
# ]
#
# print(nejv_mereni_list)
#
# # dict - udela dict z idcka a hodnoty jak u listu
# nejv_mereni_dict = {
#     mer.id: mer.hodnota
#     for mer in namereno
#     if mer.hodnota > 70
# }
#
# print(nejv_mereni_dict)
#
# # distinct (set) - udela set itemu jak vyse... KAZDA VALUE JEN EJDNOU - set have distinct items
# nejv_mereni_distinct = {
#     mer.hodnota
#     for mer in namereno
#     if mer.hodnota > 70
# }
#
# print(nejv_mereni_distinct)

###################################################
# import collections
# import uuid
#
# Mereni = collections.namedtuple('Mereni', 'id x y hodnota')
#
# namereno = [
#     Mereni(str(uuid.uuid4()), 1, 1, 72),
#     Mereni(str(uuid.uuid4()), 2, 1, 40),
#     Mereni(str(uuid.uuid4()), 3, 1, 11),
#     Mereni(str(uuid.uuid4()), 2, 1, 90),
#     Mereni(str(uuid.uuid4()), 2, 2, 60),
#     Mereni(str(uuid.uuid4()), 2, 3, 73),
#     Mereni(str(uuid.uuid4()), 3, 1, 40),
#     Mereni(str(uuid.uuid4()), 3, 2, 90),
#     Mereni(str(uuid.uuid4()), 3, 3, 90)
# ]
#
# # generator - vypise IDcka mereni, ktere maj hodnotu vetsi jak 70
# nejv_mereni_gen = (
#     mer.hodnota
#     for mer in namereno
#     if mer.hodnota >= 70
# )
#
# # pocet hodnot nad 70 v generatoru
# davaj = sum(1 for _ in nejv_mereni_gen)
#
# print(davaj)
# ############ lambda expressions #############
# Create by Michael Kennedy (@mkennedy)


# def main():
#     print(type(check_for_odd), check_for_odd)
#     print("Find odd numbers via method:")
#     for n in find_special_numbers(check_for_odd, 25):
#         print(n, end=',')
#     print()
#
#     print("Find divisible by 6 via lambda:")
#     for n in find_special_numbers(lambda i: i % 6 == 0, 25):
#         print(n, end=',')
#     print()
#
#     print("Sorted list of words: ")
#     list_of_words = ['CPython', 'read', 'improvements,', 'issues.', 'on', 'comprehensive', 'porting', 'potential',
#                      'user-facing', 'of', 'other', 'for', 'smaller', 'deprecations,', 'a', 'optimizations,', 'changes,',
#                      'including', 'and', 'Please', 'many', 'list']
#
#     # list_of_words.sort()  # ? ;)
#     # list_of_words.sort(key=lambda w: w.lower())
#     list_of_words.sort(key=lambda wrd: wrd.upper())
#     print(list_of_words)
#
#     print("Done")
#
#
# def find_special_numbers(special_selector, limit=10):
#     found = []
#     n = 0
#     while len(found) < limit:
#         if special_selector(n):
#             found.append(n)
#         n += 1
#     return found
#
#
# def check_for_odd(n):
#     return n % 2 == 1
#
#
# if __name__ == '__main__':
#     main()
###################################################

# def order(food, price, num_people=99, **kwargs):
#     print("{} people are ordering {} and it will cost {}".format(num_people, food, price))
#     # print(type(kwargs))
#     if 'other' in kwargs:
#         print("* specials: {}".format(kwargs['other']))
#
#
# def main():
#     order('chicken', 690, num_people=6)
#     order('turkey', 230)
#     order('soup', 69, num_people=2, other='veggie')
#
#     dict_order = {
#         'food': 'salt',
#         'price': 70,
#         'other': 'bitchslap'
#     }
#
#     order(**dict_order)
#
#
# if __name__ == '__main__':
#     main()

###################################################

# def order(price: float, people: int):
#     ppl = people
#     prc = price
#
#     return ppl, prc
#
# def main():
#     aj1, aj2 = order(69.99, 2)
#     print("{} people came and paid {}".format(aj1, aj2))
#
#
# if __name__ == '__main__':
#     main()