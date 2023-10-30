import random

def prettyPrint():
    for i, row in enumerate(bingo_card):
        for j, cell in enumerate(row):
            if cell == "Free Space":
                print(cell.center(12), end=' | ')
            else:
                if j < 2:
                    print(f'{str(cell).center(12)} |', end=' ')
                else:
                    print(f'{str(cell).center(12)}', end=' ')
        if i < 2:
            print("\n" + "-" * 14 * 3)
        else:
            print()

print("Bingo Card Generator")

bingo_card = [[None, None, None],
              [None, "Free Space", None],
              [None, None, None]]

generated_numbers = set()

for i in range(3):
    for j in range(3):
        if bingo_card[i][j] is None:
            while True:
                random_number = random.randint(1, 90)
                if random_number not in generated_numbers:
                    bingo_card[i][j] = random_number
                    generated_numbers.add(random_number)
                    break

print()
prettyPrint()