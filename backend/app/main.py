from fastapi import FastAPI

app = FastAPI(
    title="Boilerplate PG FastAPI React",
    description="Boilerplate codebase",
    version="0.0.1",
    contact={"name": "DaveAbes", "email": "abes.dave@outlook.com"},
    license_info={"name": "MIT"},
)


@app.get("/")
def main():
    return "Hello world."


def stub(n: int) -> int:
    return n + 1
