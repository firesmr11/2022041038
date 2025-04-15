#Copyright (c) 2025, 박정환. All rights reserved.
################

#프로그램명: 성적관리 프로그램 


#작성자: 소프트웨어학부/박정환

#작성일: 2025-04-14

#프로그램 설명: 학생 성적을 관리하는 프로그램으로, 학생 정보를 입력하고 삭제하며 성적을 계산하여 출력합니다.
#학생 수는 최대 5명으로 제한되어 있으며, 각 학생의 성적은 영어, C-언어, 파이썬 과목으로 구성됩니다.
#성적은 총점, 평균, 학점으로 계산되며, 평균이 80점 이상인 학생 수를 출력합니다.
#프로그램 사용법: 프로그램을 실행하면 메뉴가 나타납니다. 메뉴에서 학생 정보 입력, 삭제, 성적 처리 결과 계산 중 하나를 선택할 수 있습니다.   
#학생 정보를 입력하면 성적이 자동으로 계산되고, 삭제하면 해당 학생의 정보가 삭제됩니다. 성적 처리 결과 계산을 선택하면 모든 학생의 성적이 출력됩니다.
#프로그램 종료: 프로그램을 종료하려면 Ctrl+C를 누르거나, 프로그램이 완료되면 자동으로 종료됩니다.

###################

class Student:
    def __init__(self, number, name, eng, c_lang, python):
        # 학생 정보를 초기화하는 생성자
        self.number = number  # 학번
        self.name = name  # 이름
        self.eng = eng  # 영어 성적
        self.c_lang = c_lang  # C-언어 성적
        self.python = python  # 파이썬 성적
        self.total = self.calculate_total()  # 총점 계산
        self.average = self.calculate_average()  # 평균 계산
        self.grade = self.assign_grade()  # 학점 계산
        self.rank = 0  # 등수 (초기값은 0)

    def calculate_total(self):
        # 총점 계산 함수
        return self.eng + self.c_lang + self.python  # 세 과목의 점수를 더함

    def calculate_average(self):
        # 평균 계산 함수
        return self.total / 3  # 총점을 3으로 나누어 평균을 계산

    def assign_grade(self):
        # 평균에 따라 학점 부여 함수
        if self.average >= 95:
            return 'A+'  # 평균이 95 이상이면 A+
        elif self.average >= 90:
            return 'A'  # 평균이 90 이상이면 A
        elif self.average >= 85:
            return 'B+'  # 평균이 85 이상이면 B+
        elif self.average >= 80:
            return 'B'  # 평균이 80 이상이면 B
        elif self.average >= 75:
            return 'C+'  # 평균이 75 이상이면 C+
        elif self.average >= 70:
            return 'C'  # 평균이 70 이상이면 C
        elif self.average >= 65:
            return 'D+'  # 평균이 65 이상이면 D+
        elif self.average >= 60:
            return 'D'  # 평균이 60 이상이면 D
        else:
            return 'F'  # 그 외에는 F

class GradeManagement:
    def __init__(self):
        # 학생들을 관리하는 클래스의 생성자
        self.students = []  # 학생들을 저장할 리스트
        self.max_students = 5  # 최대 학생 수는 5명으로 제한

    def add_student(self):
        # 학생 정보를 입력하는 함수
        if len(self.students) >= self.max_students:
            print("학생 수 초과")  # 학생 수가 초과되면 오류 메시지 출력
            return

        # 사용자로부터 학생 정보 입력
        number = input('학번: ')
        name = input('이름: ')
        eng = self.get_score('영어')  # 영어 점수 입력
        c_lang = self.get_score('C-언어')  # C-언어 점수 입력
        python = self.get_score('파이썬')  # 파이썬 점수 입력

        # 새로운 학생 객체 생성 후 리스트에 추가
        student = Student(number, name, eng, c_lang, python)
        self.students.append(student)

    def delete_student(self):
        # 학생 정보를 삭제하는 함수
        num = input('삭제할 학번 입력: ')  # 삭제할 학생의 학번 입력
        for student in self.students:
            if student.number == num:
                self.students.remove(student)  # 해당 학번의 학생을 리스트에서 제거
                print('삭제 성공')
                return
        print('삭제할 학생이 없습니다.')  # 해당 학번이 리스트에 없으면 오류 메시지 출력

    def get_score(self, subject):
        # 각 과목의 성적을 입력 받는 함수
        while True:
            score = input(f'{subject} : ')  # 성적 입력
            if not score.isdigit():
                print(" 숫자만 입력해 주세요.")  # 숫자가 아닌 값이 입력되면 오류 메시지 출력
                continue

            score = int(score)

            if 0 <= score <= 100:
                return score  # 0~100 사이의 성적만 유효
            else:
                print(" 점수는 0에서 100 사이여야 합니다.")  # 성적이 0~100이 아니면 오류 메시지 출력

    def rank_students(self):
        # 학생들의 성적을 기준으로 등수를 계산하는 함수
        self.students.sort(key=lambda x: x.average, reverse=True)  # 평균을 기준으로 내림차순 정렬
        for i, student in enumerate(self.students):
            student.rank = i + 1  # 정렬 후 학생의 등수 부여

    def count_students_above_80(self):
        # 80점 이상인 학생 수를 계산하는 함수
        return sum(1 for student in self.students if student.average >= 80)  # 평균이 80 이상인 학생을 세어 반환

    def display_results(self):
        # 성적 처리 결과를 출력하는 함수
        print("성적관리프로그램".center(50))  # 제목 출력
        print('=' * 80)  # 구분선 출력
        print('{:<15}{:<13}{:<5}{:<5}{:<5}{:<5}{:<5}{:<5}{:<5}'.format('학번', '이름', '영어', 'C-언어', '파이썬', '총점', '평균', '학점', '등수'))  # 헤더 출력
        print('=' * 80)  # 구분선 출력

        # 각 학생의 성적 출력
        for student in self.students:
            print(f"{student.number:<15} {student.name:<15} {student.eng:<7} {student.c_lang:<7} {student.python:<7} "
                  f"{student.total:<7} {student.average:<7.2f} {student.grade:<7} {student.rank:<7}")

        # 80점 이상 학생 수 출력
        print(f'80점 이상 학생 수: {self.count_students_above_80()}')
        print('성적 처리 결과 계산 완료')

    def menu(self):
        # 메뉴 출력 함수
        print('1. 학생 정보 입력')
        print('2. 학생 정보 삭제')
        print('3. 성적 처리 결과 계산')

        while True:
            try:
                a = int(input("메뉴를 선택하세요 (1~3): "))  # 메뉴 선택
                if a in [1, 2, 3]:
                    return a  # 1~3 사이의 숫자일 경우 선택된 메뉴 반환
                print("1~3 사이의 숫자를 입력하세요.")  # 유효하지 않은 숫자 입력 시 오류 메시지 출력
            except ValueError:
                print("숫자를 입력하세요.")  # 숫자가 아닌 값을 입력 시 오류 메시지 출력

def main():
    # 메인 함수
    grade_management = GradeManagement()  # 성적 관리 객체 생성

    while True:
        choice = grade_management.menu()  # 메뉴 선택

        if choice == 1:
            grade_management.add_student()  # 학생 정보 입력
        elif choice == 2:
            grade_management.delete_student()  # 학생 정보 삭제
        elif choice == 3:
            print('성적 처리 결과 계산')
            break

    grade_management.rank_students()  # 학생들의 등수 계산
    grade_management.display_results()  # 성적 출력

if __name__ == "__main__":
    main()  # 프로그램 실행
