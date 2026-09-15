from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

counter = 0


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1 id="counter">0</h1>
    <button onclick="count()">Count</button>

    <script>
        async function count() {
            const response = await fetch("/count");
            const data = await response.json();

            document.getElementById("counter").innerText = data.counter;
        }
    </script>
    """


@app.get("/count")
def count():
    global counter
    counter += 1
    return {"counter": counter}
