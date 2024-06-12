my_dict = {"Андрей": 27, "Максим": 18 , "Влад": 35}
print(my_dict["Максим"])
my_dict["Василий"] = 46
print(my_dict)
my_dict.update({"Антон": 15, "Женя": 33, "Стас": 24})
print(my_dict)
my_dict.pop("Андрей")
print(my_dict)
my_set = {"Вася", 14, 14, 2.5, False, (12,29)}
print(my_set)
print(my_set.discard("Вася"))
print(my_set)
print(my_set.add(7))
print(my_set.add((1,3,4)))
print(my_set)