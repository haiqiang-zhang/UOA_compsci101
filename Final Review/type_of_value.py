a_list = [1, '457', 4, 'True']
a_dict = {"strangely": 2, "happy": 4}
object1 = a_list[2] / 2
object2 = [a_list.pop(2) == a_dict["happy"]]
object3 = len(a_list[1] * 3) * a_dict["strangely"]
print(type(object1), type(object2), type(object3))