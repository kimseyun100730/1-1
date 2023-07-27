from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 학생 정보를 저장할 임시 데이터 (예시로 딕셔너리를 사용)
students = {
    "mj10101": {"name": "홍길동", "password": "0000", "class": "1-1"},
    "mj10102": {"name": "김철수", "password": "0000", "class": "1-1"},
    # 학생 정보 추가...
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2', methods=['POST'])
def index2():
    student_id = request.form['student_id']
    password = request.form['password']

    if student_id in students and students[student_id]['password'] == password:
        # 학번과 비밀번호가 일치하면 해당 학생 정보를 index2.html에 전달
        student_info = students[student_id]
        return render_template('index2.html', student=student_info)
    else:
        error_message = "로그인 실패. 학번과 비밀번호를 확인하세요."
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
