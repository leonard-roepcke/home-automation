from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

counter = 0


@app.get("/", response_class=HTMLResponse)
def home():
    return f"""
    <h1>{counter}</h1>
    <button onclick="count()">Count</button>

    <script>
        async function count() {{
            await fetch("/count");
            location.reload();
        }}
    </script>
    """


@app.get("/count")
def count():
    global counter
    counter += 1
