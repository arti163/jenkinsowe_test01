from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_item(param: str):
	return {"Otrzymany Parametr:", param}
