async function fetchQuiz() {
    const res = await fetch("http://localhost:8000/quiz");
    const data = await res.json();
    document.getElementById("quiz").innerText = JSON.stringify(data);
}
