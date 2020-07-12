import random

def main():
    random.seed(30)
    print("Total of 3 dice:", get_dice_total(3))
    print("Total of 5 dice:", get_dice_total(5))
    print("Total of 4 dice:", get_dice_total(4))


def get_dice_total(how_many):
    count = 1
    grade = 0
    while count <= how_many:
        grade = grade + random.randrange(1, 7)
        count += 1
    return grade



main()