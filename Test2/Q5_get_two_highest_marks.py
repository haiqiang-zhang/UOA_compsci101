def get_two_highest_marks(names_marks_list):
    names_marks_list_score_sort = []
    for index in range(len(names_marks_list)):
        change_sort = (names_marks_list[index][1], names_marks_list[index][0])
        names_marks_list_score_sort.append(change_sort)
    names_marks_list_score_sort.sort()
    result = [names_marks_list_score_sort[-2][0], names_marks_list_score_sort[-1][0]]
    return result









names_marks = [("Ian", 78), ("Siggy", 88), ("Andy", 68), ("Irene", 90), ("Gio", 59)]
top_two = get_two_highest_marks(names_marks)
print(top_two)
names_marks = [("Isa", 88), ("Bro", 92), ("Bella", 88), ("Lee", 68), ("Teo", 60)]
top_two = get_two_highest_marks(names_marks)
print(top_two)
names_marks = [("David", 88), ("Lee", 68), ("Teo", 60), ("Jo", 91)]
top_two = get_two_highest_marks(names_marks)
print(top_two)