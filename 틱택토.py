# 2022041038 박정환 틱택톡 게임 프로그램램
import random  # -


# 보드 출력 함수
def print_board():
    for row in board:
        print(row)
    print()


def computer_turn():
    print("컴퓨터가 선택 중")
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if board[x][y] == 0:  # 빈 칸이면 선택
            board[x][y] = "O"  # 컴퓨터는 'O'
            break


def human_turn():
    print("사용자가 선택 중")
    while True:
        x = int(input("다음 수의 x좌표를 입력하시오: "))
        y = int(input("다음 수의 y좌표를 입력하시오: "))
        if board[x][y] == 0:  # 빈 칸이면 선택
            board[x][y] = "X"  # 사용자는 'X'
            break


def win(us):
    # 가로 승리 체크
    for row in range(3):
        if us[row][0] == us[row][1] == us[row][2] and us[row][0] != 0:
            return True

    # 세로 승리 체크
    for col in range(3):
        if us[0][col] == us[1][col] == us[2][col] and us[0][col] != 0:
            return True

    # 대각선 승리 체크
    if us[0][0] == us[1][1] == us[2][2] and us[0][0] != 0:
        return True
    if us[0][2] == us[1][1] == us[2][0] and us[0][2] != 0:
        return True

    return False


def draw(us):
    for row in us:
        for col in us:
            if 0 in row:
                return False

    return True


board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 게임 보드 초기화

print('게임을 시작할까요 말까요 할까요 말까요')
print_board()
while True:
    start = input("게임을 시작하시겠습니까? (y/n): ")
    if start.lower() == 'n':
        print("게임을 종료합니다.")
        exit()
    elif start.lower() == 'y':
        print("게임을 시작합니다.")
    else:
        print("잘못된 입력입니다. y 또는 n을 입력하세요.")
    while True:
        human_turn()
        print_board()

        if win(board):
            print("사용자가 승리 했습니당")
            break
        if draw(board):
            print("무승부")
            break

        computer_turn()
        print_board()
        if win(board):
            print("컴퓨터가 승리 했습니당")
            break
        if draw(board):
            print("무승부")

            break
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 컴퓨터의 턴을 실행한다.#-
# ... (previous code remains the same)#+





