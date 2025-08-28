import React, { useEffect, useState } from "react";

function App() {
  const [quiz, setQuiz] = useState(null);
  const [answer, setAnswer] = useState("");
  const [result, setResult] = useState("");

  const fetchQuiz = () => {
    fetch("http://localhost:8000/quiz/random/")
      .then((res) => res.json())
      .then((data) => {
        setQuiz(data);
        setAnswer("");
        setResult("");
      });
  };

  const submitAnswer = () => {
    fetch("http://localhost:8000/quiz/answer/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ quiz_id: quiz.id, answer }),
    })
      .then((res) => res.json())
      .then((data) => setResult(data.result));
  };

  useEffect(() => {
    fetchQuiz();
  }, []);

  if (!quiz) return <div>クイズを読み込み中...</div>;

  return (
    <div style={{ padding: "20px" }}>
      <h1>クイズゲーム</h1>
      <p><strong>問題:</strong> {quiz.question}</p>

      <input
        placeholder="答えを入力"
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
      />
      <button onClick={submitAnswer}>回答</button>

      {result && (
        <div style={{ marginTop: "10px" }}>
          {result === "correct" ? "✅ 正解！" : "❌ 不正解"}
        </div>
      )}

      <button style={{ marginTop: "20px" }} onClick={fetchQuiz}>
        次の問題
      </button>
    </div>
  );
}

export default App;
