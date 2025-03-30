# 5명의 학생에게 이름 영어점수,파이썬점수, c언어 점수 등을 입력 받아 총점, 평균, 학점, 등수 를 계산하여 출력하는 프로그램

def grade(a):     #변수를 입력받아 변수 값에 따라 학점을 리턴 해 주는 함수
    if a >= 95:
        return 'A+'
    elif a >= 90:
        return 'A'
    elif a >= 85:
        return 'B+'
    elif a >= 80:
        return 'B'
    elif a >= 75:
        return 'C+'
    elif a >= 70:
        return 'C'
    elif a >= 65:
        return 'D+'
    elif a >= 60:
        return 'D'
    else:
        return 'F'
def getscore(subject):
    #올바른 숫자를 입력받을 때까지 무한 반복하는 함수
    while True:
        score = input(f'{subject} : ')
        
        if not score.isdigit():  
            print(" 숫자만 입력해 주세요.")
            continue  # 숫자가 아니면 다시 입력받기
        
        score = int(score)  # 문자열을 정수로 변환

        if 0 <= score <= 100:
            return score  # 정상적인 범위면 반환
        else:
            print(" 점수는 0에서 100 사이여야 합니다.")  # 범위를 벗어나면 다시 입력받기def score_add(program):


def score_add(program):
    """ 총점과 평균을 계산하여 리스트로 반환하는 함수 """
    t_add_list = []
    t_aveg_list = []

    for i in range(5):
        t_add = sum(program[i][2:5])  # 총점 계산
        t_aveg = t_add / 3  # 평균 계산

        t_add_list.append(t_add)
        t_aveg_list.append(t_aveg)
    return t_add_list, t_aveg_list
def rank_md(aveg): #등수 계산 함수 
    sort_aveg = sorted(aveg, reverse=True)  # 내림차순 정렬
    rank = []
    for i in aveg:
        rank.append(sort_aveg.index(i) + 1)  # 등수 계산
    return rank

def pr(program,total,aveg,grad,rank,ecc):
    text = "성적관리프로그램"
    print(text.center(50))
    print('=' * 80)
    print('{:<15}{:<13}{:<5}{:<5}{:<5}{:<5}{:<5}{:<5}{:<5}'.format('학번', '이름', '영어', 'C-언어', '파이썬', '총점', '평균', '학점', '등수',))
    print('=' * 80)
    for i in range(5):
        print(f"{program[i][0]:<15} {program[i][1]:<15} {program[i][2]:<7} {program[i][3]:<7} {program[i][4]:<7} {total[i]:<7}{aveg[i]:<7.2f} {grad[i]:<7} {rank[i]:<7} ")

    print(f'80점 이상 학생 수: {ecc}')
    print('성적 처리 결과 계산 완료')
def menu():  # 메뉴 선택 함수
    print('1. 학생 정보 입력')
    print('2. 학생 정보 삭제')
    print('3. 성적 처리 결과 계산')

    while True:
        try:
            a = int(input("메뉴를 선택하세요 (1~3): "))
            if a in [1, 2, 3]:
                return a
            print("1~3 사이의 숫자를 입력하세요.")
        except ValueError:
            print("숫자를 입력하세요.")
def delete(program):
    num = input('삭제할 학번 입력: ')
    for student in program[:]:  # 리스트 복사본 사용
        if student[0] == num:
            program.remove(student)
            print('삭제 성공')
            return True  # 삭제 성공
    print('삭제할 학생이 없습니다.')
    return False  # 삭제 실패


def totalsort(program, total, aveg, grad, rank): #총점 정렬 함수
    for i in range(5):
        for j in range(i+1, 5):
            if total[i] < total[j]:
                total[i], total[j] = total[j], total[i]  # swap
                program[i], program[j] = program[j], program[i]  # swap
                aveg[i], aveg[j] = aveg[j], aveg[i]  # swap
                grad[i], grad[j] = grad[j], grad[i]  # swap
                rank[i], rank[j] = rank[j], rank[i]

    return program
def ec(aveg):
    count = 0
    for i in range(5):
        if float(aveg[i])>=80:
            count+=1

    return count



program = []
count =0

while True:
    temp = menu()

    if temp == 1:
        if count > 5:
            print('학생 수 초과')
            break

        number = input('학번: ') 
        name = input('이름: ')
        eng = getscore('영어')
        c_lang = getscore('C-언어')
        python = getscore('파이썬')

        program.append([number, name, eng, c_lang, python])
        print('=' * 80)

        count += 1  
    elif temp == 2:
        if count == 0:
            print('삭제할 학생이 없습니다.')
        else:
            if delete(program):  
                count -= 1
    elif temp == 3:
        print('성적 처리 결과 계산')
        break


    # 메뉴 함수 호출
# 학생 5명 입력

total = []       # 값을 저장할 리스트 선언
aveg = []
grad = []
rank = []

total,aveg =score_add(program)

for i in range(5):
    grad.append(grade(aveg[i]))  # 학점 리스트에 추가

rank=rank_md(aveg)     # 등수 계산 함수


program, total, aveg, grad, rank = totalsort(program, total, aveg, grad, rank)  # 총점 정렬 함수 호출

ecc=ec(aveg) #80점 이상 학생 수 계산 함수 호출
pr(program,total,aveg,grad,rank,ecc)  # 출력 함수 호출]



