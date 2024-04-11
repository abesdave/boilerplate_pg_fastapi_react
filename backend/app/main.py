from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def main():
    return "Hello world."


def stub(n: int) -> int:
    return n + 1
