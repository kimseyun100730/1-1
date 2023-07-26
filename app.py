from flask import Flask, render_template, request

app = Flask(__name__)

# 학생 아이디와 비밀번호를 딕셔너리로 정의
student_passwords = {
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
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    class_name = request.form['class']
    student_name = request.form['student']
    password = request.form['password']
    # 학생 아이디를 형식에 맞게 생성
    student_id = f"mj{class_name}{student_name}"
    
    # 학생 아이디와 비밀번호를 확인하여 로그인 여부 판단
    if student_id in student_passwords and password == student_passwords[student_id]:
        return render_template('index2.html', class_name=class_name, student_name=student_name)
    else:
        return "로그인 실패: 학생 아이디 또는 비밀번호가 잘못되었습니다."

@app.route('/write', methods=['POST'])
def write_alimjang():
    class_name = request.form['class']
    student_name = request.form['student']
    message = request.form['message']
    
    # 학생 아이디를 형식에 맞게 생성
    student_id = f"mj{class_name}{student_name}"
    
    # 학생 아이디와 비밀번호를 확인하여 작성 권한 판단
    if student_id in student_passwords and request.form['password'] == student_passwords[student_id]:
        # 여기서 알림장 작성 로직을 추가하여 파일 또는 데이터베이스에 선생님의 글을 저장할 수 있습니다.
        return f"알림장 작성 완료: 반 {class_name}, 학생 {student_name}, 글: {message}"
    else:
        return "학생 아이디 또는 비밀번호가 잘못되었습니다."

if __name__ == '__main__':
    app.run()
