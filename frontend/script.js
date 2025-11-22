document.getElementById("diagnoseBtn").addEventListener("click", async function () {
    const symptom = document.getElementById("symptomInput").value;
    const model = document.getElementById("modelSelect").value;
    if (!symptom) { alert("Please enter a symptom"); return; }
    document.getElementById("result").innerText = "Processing...";
    try {
        const resp = await fetch("http://127.0.0.1:8000/diagnose", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ symptom: symptom, model: model })
        });
        const data = await resp.json();
        let out = "🔍 Triage:\n";
        out += data.triage.map(t => `${t[0]} (confidence ${t[1]})`).join("\n");
        out += "\n\n🛠 Repair Steps:\n";
        data.repair_steps.forEach(s => { out += `- ${s.desc} (${s.expected_time_minutes} min)\n`; });
        document.getElementById("result").innerText = out;
    } catch (e) {
        document.getElementById("result").innerText = "Cannot reach backend. Make sure server is running.";
        console.error(e);
    }
});
