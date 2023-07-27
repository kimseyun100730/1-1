import React, { useState } from 'react';
import './App.css';

function App() {
  const [studentId, setStudentId] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleLogin = () => {
    // 서버에 학생 정보와 비밀번호를 전달하여 로그인 처리를 수행
    // 예시로는 간단하게 학생 아이디와 비밀번호를 하드코딩으로 비교
    if (studentId === 'mj10101' && password === '0000') {
      // 로그인 성공 시 페이지 이동 또는 알림장 페이지를 보여주는 로직
      // 여기서는 예시로 콘솔에 로그인 성공 메시지를 출력
      console.log('로그인 성공');
    } else {
      // 로그인 실패 시 에러 메시지 출력
      setErrorMessage('아이디 또는 비밀번호가 올바르지 않습니다.');
    }
  };

  return (
    <div className="App">
      <div className="login-container">
        <h1>알림장 로그인</h1>
        <input
          type="text"
          placeholder="학생 아이디"
          value={studentId}
          onChange={(e) => setStudentId(e.target.value)}
        />
        <input
          type="password"
          placeholder="비밀번호"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button onClick={handleLogin}>로그인</button>
        {errorMessage && <div className="error-message">{errorMessage}</div>}
      </div>
    </div>
  );
}

export default App;
