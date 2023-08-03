"""
функция рисования поля
функция установки х и о
функция проверки выигрыша
"""

def drawField(lst: list) -> None:
    for i in range(3):
        print(f"| {lst[0 + i*3]} | {lst[1 + i*3]} | {lst[2 + i*3]} |")

def setXO(lst: list, player: str) -> None:
    flag = False
    while not flag:
        answer = input(f"Введите номер клетки куда установить {player}: ")
        try:
            answer = int(answer)
        except:
            print("Не корректные данные. Введите число от 1 до 9")
            continue

        if 0 <= answer <= 9:
            if str(lst[answer-1]) not in "XO":
                lst[answer-1] = player
                flag = True
            else:
                print("Клетка уже занята")
        else:
            print("Введите корректное число от 1 до 9")

def winResult(lst: list) -> str | bool:
    win_lst = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for row in win_lst:
        if lst[row[0]] == lst[row[1]] == lst[row[2]]:
            return lst[row[0]]
    return False

if __name__ == "__main__":
    winFlag = False
    counter = 0
    field = list(range(1, 10))
    player_own = "X"
    player_two = "O"

    while not winFlag:
        drawField(field)
        if counter % 2 == 0:
            setXO(field, player_own)
        else:
            setXO(field, player_two)

        counter += 1

        if counter > 4:
            winFlag = winResult(field)
            if winFlag:
                print(f"Победил игрок {winFlag}")
                break

        if counter == 9:
            print("Ничья!")
            break