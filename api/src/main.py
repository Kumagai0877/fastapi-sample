from fastapi import FastAPI

app = FastAPI(
    title='FastAPI Sample',
    description='FastAPIのSample',
    version='0.0.1'
)


@app.get("/hello")
def hello():
    return {"Hello": "World!"}
