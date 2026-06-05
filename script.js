function submitBug() {
    const bugText = document.getElementById("bugInput").value;

    fetch("http://127.0.0.1:5000/triage", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ bug: bugText })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText =
            JSON.stringify(data, null, 2);
    });
}