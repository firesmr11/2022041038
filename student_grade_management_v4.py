# Copyright (c) 2025, 박정환. All rights reserved.
################

# 프로그램명: 성적관리 프로그램 (데이터베이스 연동 버전)
# 작성자: 소프트웨어학부/박정환
# 작성일: 2025-06-07
# 프로그램 설명: 학생 성적을 DB로 관리하는 프로그램으로, 학생 정보를 입력/삭제하고 성적을 계산하여 출력합니다. (학생 수 제한 없음)

###################

import sqlite3


class GradeManagementDB:
    def __init__(self, db_name='grades.db'):
        """데이터베이스 연결 및 테이블 생성"""
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.setup_table()

    def setup_table(self):
        """students 테이블이 없으면 생성"""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_number TEXT PRIMARY KEY,
            student_name TEXT NOT NULL,
            eng_score INTEGER NOT NULL,
            c_lang_score INTEGER NOT NULL,
            python_score INTEGER NOT NULL
        )
        """)
        self.conn.commit()

    def add_student(self):
        """학생 정보를 입력받아 DB에 추가 (학생 수 제한 없음)"""

        while True:
            number = input('학번: ')
            self.cursor.execute("SELECT * FROM students WHERE student_number=?", (number,))
            if self.cursor.fetchone():
                print("이미 존재하는 학번입니다. 다른 학번을 입력하세요.")
            else:
                break

        name = input('이름: ')
        eng = self.get_score('영어')
        c_lang = self.get_score('C-언어')
        python = self.get_score('파이썬')

        # DB에 학생 정보 INSERT
        self.cursor.execute("""
            INSERT INTO students (student_number, student_name, eng_score, c_lang_score, python_score)
            VALUES (?, ?, ?, ?, ?)
        """, (number, name, eng, c_lang, python))
        self.conn.commit()
        print(f"'{name}' 학생의 정보가 성공적으로 입력되었습니다.")

    def delete_student(self):
        """학번을 입력받아 DB에서 학생 정보 삭제"""
        num = input('삭제할 학번 입력: ')
        self.cursor.execute("SELECT * FROM students WHERE student_number=?", (num,))
        if self.cursor.fetchone():
            self.cursor.execute("DELETE FROM students WHERE student_number=?", (num,))
            self.conn.commit()
            print('삭제 성공')
        else:
            print('삭제할 학생이 없습니다.')

    def get_score(self, subject):
        """0~100 사이의 유효한 점수를 입력받는 함수"""
        while True:
            score_str = input(f'{subject}: ')
            if score_str.isdigit():
                score = int(score_str)
                if 0 <= score <= 100:
                    return score
                else:
                    print("점수는 0에서 100 사이여야 합니다.")
            else:
                print("숫자만 입력해 주세요.")

    def display_results(self):
        """DB에서 모든 학생 정보를 조회하여 성적 결과 출력"""
        query = """
        SELECT
            student_number,
            student_name,
            eng_score,
            c_lang_score,
            python_score,
            (eng_score + c_lang_score + python_score) AS total,
            (eng_score + c_lang_score + python_score) / 3.0 AS average,
            CASE
                WHEN (eng_score + c_lang_score + python_score) / 3.0 >= 95 THEN 'A+'
                WHEN (eng_score + c_lang_score + python_score) / 3.0 >= 90 THEN 'A'
                WHEN (eng_score + c_lang_score + python_score) / 3.0 >= 85 THEN 'B+'
                WHEN (eng_score + c_lang_score + python_score) / 3.0 >= 80 THEN 'B'
                WHEN (eng_score + c_lang_score + python_score) / 3.0 >= 75 THEN 'C+'
                WHEN (eng_score + c_lang_score + python_score) / 3.0 >= 70 THEN 'C'
                WHEN (eng_score + c_lang_score + python_score) / 3.0 >= 65 THEN 'D+'
                WHEN (eng_score + c_lang_score + python_score) / 3.0 >= 60 THEN 'D'
                ELSE 'F'
            END AS grade,
            RANK() OVER (ORDER BY (eng_score + c_lang_score + python_score) DESC) AS rank
        FROM
            students
        ORDER BY
            rank;
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        print("\n" + "성적관리프로그램".center(80))
        print('=' * 80)
        print('{:<15}{:<13}{:<7}{:<10}{:<10}{:<7}{:<7}{:<7}{:<7}'.format('학번', '이름', '영어', 'C-언어', '파이썬', '총점', '평균',
                                                                         '학점', '등수'))
        print('=' * 80)

        if not results:
            print("입력된 학생 정보가 없습니다.")
        else:
            for row in results:
                print(f"{row[0]:<15} {row[1]:<15} {row[2]:<7} {row[3]:<10} {row[4]:<10} "
                      f"{row[5]:<7} {row[6]:<7.2f} {row[7]:<7} {row[8]:<7}")

        self.cursor.execute("SELECT COUNT(*) FROM students WHERE (eng_score + c_lang_score + python_score) / 3.0 >= 80")
        count_above_80 = self.cursor.fetchone()[0]

        print("-" * 80)
        print(f'80점 이상 학생 수: {count_above_80}')
        print('성적 처리 결과 계산 완료')

    def menu(self):
        print("\n--- 메뉴 ---")
        print('1. 학생 정보 입력')
        print('2. 학생 정보 삭제')
        print('3. 성적 처리 결과 계산 및 종료')
        print('-----------')

        while True:
            try:
                choice = int(input("메뉴를 선택하세요 (1-3): "))
                if choice in [1, 2, 3]:
                    return choice
                else:
                    print("1-3 사이의 숫자를 입력하세요.")
            except ValueError:
                print("숫자를 입력하세요.")

    def close(self):
        """데이터베이스 연결 종료"""
        self.conn.close()


def main():
    grade_system = GradeManagementDB()

    while True:
        choice = grade_system.menu()

        if choice == 1:
            grade_system.add_student()
        elif choice == 2:
            grade_system.delete_student()
        elif choice == 3:
            print('성적 처리 결과 계산을 시작합니다.')
            grade_system.display_results()
            break

    grade_system.close()
    print("프로그램을 종료합니다.")


if __name__ == "__main__":
    main()