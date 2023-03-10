from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    tatooine = 'tatooine'
    naboo = 'naboo'
    coruscant = 'coruscant'


app = FastAPI()


@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.tatooine:
        return {'model_name': model_name, 'message': 'Welcome to Tatooine'}
    if model_name.value == 'coruscant':
        return {'model_name': model_name, 'message': 'Welcome to Coruscant'}
    return {'model_name': model_name, 'message': 'Welcome to Naboo'}
