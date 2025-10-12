from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

@app.get("/sum")
def sum_numbers():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Data file not found.")
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON format.")

    if "numbers" not in data:
        raise HTTPException(status_code=400, detail="Missing 'numbers' key in JSON.")

    numbers = data["numbers"]
    if not isinstance(numbers, list):
        raise HTTPException(status_code=400, detail="'numbers' should be a list.")

    try:
        return {"sum": sum(numbers)}
    except TypeError:
        raise HTTPException(status_code=400, detail="All items in 'numbers' must be numeric.")
