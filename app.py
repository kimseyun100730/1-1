from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2', methods=['POST'])
def index2():
    student_id = request.form['student_id']
    password = request.form['password']

    # 학생 정보를 확인하고 로그인 실패 시 오류 메시지를 error 변수에 저장
    if student_id in students and students[student_id]['password'] == password:
        student_info = students[student_id]
        return render_template('index2.html', student=student_info)
    else:
        error_message = "로그인 실패. 학번과 비밀번호를 확인하세요."
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
