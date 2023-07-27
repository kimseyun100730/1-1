import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [studentId, setStudentId] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = () => {
    // 로그인 처리
    // 실제로는 서버와 통신하여 학생 정보를 확인해야 함
    // 여기서는 학생 정보를 하드코딩하고 비밀번호가 "0000"인 경우 로그인 성공으로 가정
    if (studentId.startsWith('mj101') && password === '0000') {
      setError('');
      // 로그인 성공 시, 원하는 화면으로 이동 (예시로 로그인 성공 메시지 출력)
      alert('로그인 성공!');
    } else {
      setError('로그인 실패. 학번과 비밀번호를 확인하세요.');
    }
  };

  return (
    <div className="App">
      <div className="login-box">
        <img src="school_logo.png" className="school-logo" alt="School Logo" />
        <h1>학교 알림장</h1>
        <div className="form">
          <label>학번:</label>
          <input type="text" value={studentId} onChange={(e) => setStudentId(e.target.value)} />

          <label>비밀번호:</label>
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />

          <button onClick={handleLogin}>로그인</button>
        </div>
        {error && <p className="error-message">{error}</p>}
      </div>
    </div>
  );
}

export default App;
