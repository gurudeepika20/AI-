
board = [" "] * 9
wins = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

def show():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6:
            print("-----")

for turn in range(9):
    show()
    player = "X" if turn % 2 == 0 else "O"

    while True:
        try:
            pos = int(input(player + " (1-9): ")) - 1
            if 0 <= pos < 9 and board[pos] == " ":
                break
            print("Invalid position. Try again.")
        except ValueError:
            print("Enter a number from 1 to 9.")

    board[pos] = player

    if any(all(board[i] == player for i in line)
           for line in wins):
        show()
        print(player, "wins!")
        break
else:
    show()
    print("Draw!")




