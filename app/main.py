import csv
import logging
import uvicorn

from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    with open('data/resort_data.csv', 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        resort_csv = list(csv_reader) 
        print(f"resort_csv: {resort_csv}")

    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
