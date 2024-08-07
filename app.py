from fastapi import FastAPI
from main import main_function
from utils import timeit
import logging

app = FastAPI()

@timeit
@app.get("/test")
def test_api():
    logging.info(f"API Call Initiated")
    main_function()
    logging.info(f"API Returned Response")
    return {"message": "API call completed"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
