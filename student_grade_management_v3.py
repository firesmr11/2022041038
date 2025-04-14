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
        self.number = number
        self.name = name
        self.eng = eng
        self.c_lang = c_lang
        self.python = python
        self.total = self.calculate_total()
        self.average = self.calculate_average()
        self.grade = self.assign_grade()
        self.rank = 0  # 등수는 나중에 계산

    def calculate_total(self):
        return self.eng + self.c_lang + self.python

    def calculate_average(self):
        return self.total / 3

    def assign_grade(self):
        if self.average >= 95:
            return 'A+'
        elif self.average >= 90:
            return 'A'
        elif self.average >= 85:
            return 'B+'
        elif self.average >= 80:
            return 'B'
        elif self.average >= 75:
            return 'C+'
        elif self.average >= 70:
            return 'C'
        elif self.average >= 65:
            return 'D+'
        elif self.average >= 60:
            return 'D'
        else:
            return 'F'

class GradeManagement:
    def __init__(self):
        self.students = []
        self.max_students = 5

    def add_student(self):
        if len(self.students) >= self.max_students:
            print("학생 수 초과")
            return

        number = input('학번: ')
        name = input('이름: ')
        eng = self.get_score('영어')
        c_lang = self.get_score('C-언어')
        python = self.get_score('파이썬')

        student = Student(number, name, eng, c_lang, python)
        self.students.append(student)

    def delete_student(self):
        num = input('삭제할 학번 입력: ')
        for student in self.students:
            if student.number == num:
                self.students.remove(student)
                print('삭제 성공')
                return
        print('삭제할 학생이 없습니다.')

    def get_score(self, subject):
        while True:
            score = input(f'{subject} : ')
            if not score.isdigit():
                print(" 숫자만 입력해 주세요.")
                continue

            score = int(score)

            if 0 <= score <= 100:
                return score
            else:
                print(" 점수는 0에서 100 사이여야 합니다.")

    def rank_students(self):
        self.students.sort(key=lambda x: x.average, reverse=True)
        for i, student in enumerate(self.students):
            student.rank = i + 1

    def count_students_above_80(self):
        return sum(1 for student in self.students if student.average >= 80)

    def display_results(self):
        print("성적관리프로그램".center(50))
        print('=' * 80)
        print('{:<15}{:<13}{:<5}{:<5}{:<5}{:<5}{:<5}{:<5}{:<5}'.format('학번', '이름', '영어', 'C-언어', '파이썬', '총점', '평균', '학점', '등수'))
        print('=' * 80)

        for student in self.students:
            print(f"{student.number:<15} {student.name:<15} {student.eng:<7} {student.c_lang:<7} {student.python:<7} "
                  f"{student.total:<7} {student.average:<7.2f} {student.grade:<7} {student.rank:<7}")

        print(f'80점 이상 학생 수: {self.count_students_above_80()}')
        print('성적 처리 결과 계산 완료')

    def menu(self):
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

def main():
    grade_management = GradeManagement()

    while True:
        choice = grade_management.menu()

        if choice == 1:
            grade_management.add_student()
        elif choice == 2:
            grade_management.delete_student()
        elif choice == 3:
            print('성적 처리 결과 계산')
            break

    grade_management.rank_students()  # 학생들의 등수 계산
    grade_management.display_results()  # 성적 출력

if __name__ == "__main__":
    main()
