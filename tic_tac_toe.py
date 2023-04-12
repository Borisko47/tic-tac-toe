winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
board = list(range(1, 10))

def greeting():
    print("-" * 19)
    print("Приветствуем в игре \n Крестики Нолики!")
    print("-" * 19)
    print("Чтобы сделать ход \n выбери цифру.")
    print("-" * 19)
    print()

greeting()

def creating_board():
    print("-" * 13)
    for i in range(3):
        print(f"| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |")
        print("-" * 13)

def game(players_move):
    while True:
        value = input(f"Ходит {players_move}: ")
        if value not in '123456789':
            print("Ээ.. Цифру же надо вводить от 1 до 9.")
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print("Куда? Это же занятая клетка. Ходи в другую!")
            continue
        board[value - 1] = players_move
        break

def check_wins():
    for i in winning_combinations:
        if (board[i[0] - 1]) == (board[i[1] - 1]) == (board[i[2] - 1]):
            return board[i[1] - 1]
    return False

def main():
    counter = 0
    while True:
        creating_board()
        if counter % 2 == 0:
            game('X')
        else:
            game('O')
        if counter > 3:
            winner = check_wins()
            if winner:
                creating_board()
                print(f"{winner} Ты победил!")
                break
        counter += 1
        if counter > 8:
            creating_board()
            print("Получается ничья :) Сыграйте ещё раз!")
            break

main()
