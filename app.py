from fastapi import FastAPI
import pandas as pd
import uvicorn
from pydantic import BaseModel
import json
from fastapi.responses import FileResponse

class JsonCsv(BaseModel):
    json:list
    nome:str
app = FastAPI()



@app.post("/json_to_csv/")
def json_to_csv(json_str:JsonCsv):
    read_json = pd.read_json(json.dumps(json_str.json))

    read_json.to_csv(f"{json_str.nome}.csv")
    # read_csv = pd.read_csv(f"{json_str.nome}.csv")
    # read_csv.to_excel(f'{json_str.nome}.xlsx', index = None)

    return FileResponse(path=f"{json_str.nome}.csv", filename = f"{json_str.nome}.csv", media_type="csv")


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=9090, reload=True)