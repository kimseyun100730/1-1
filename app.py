from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 학생 정보를 저장할 임시 데이터 (예시로 딕셔너리를 사용)
students = {
    'teacher': '0000',
    'mj10101': '0000',
    'mj10102': '0000',
    'mj10103': '0000',
    'mj10104': '0000',
    'mj10105': '0000',
    'mj10106': '0000',
    'mj10107': '0000',
    'mj10108': '0000',
    'mj10109': '0000',
    'mj10110': '0000',
    'mj10112': '0000',
    'mj10113': '0000',
    'mj10121': '0000',
    'mj10122': '0000',
    'mj10123': '0000',
    'mj10124': '0000',
    'mj10125': '0000',
    'mj10126': '0000',
    'mj10127': '0000',
    'mj10128': '0000',
    'mj10129': '0000',
    'mj10130': '0000',
    'mj10131': '0000',
    'mj10132': '0000'
}

@app.route('/')
def index():
    return render_template('index.html', error=None)

@app.route('/index2', methods=['POST'])
def index2():
    student_id = request.form['student_id']
    password = request.form['password']

    if student_id in students and students[student_id]['password'] == password:
        student_info = students[student_id]
        return render_template('index2.html', student=student_info)
    else:
        error_message = "로그인 실패. 학번과 비밀번호를 확인하세요."
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
