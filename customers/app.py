from fastapi import FastAPI

app = FastAPI()


@app.get('/get')
def get():
    return "Got it"

@app.get('/')
def run():
    return "Running"
