from typing import Union

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{'item_name': 'Foo'},
                 {'item_name': 'Bar'},
                 {'item_name': 'Baz'}]


@app.get('/items/')
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get('/items/{item_id}')
async def read_item(item_id: int, q: Union[str, None] = None):
    if q:
        return {'item_id': item_id, "q": q}
    return {'item_id': item_id}


@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(user_id: int, item_id: int, q: Union[str, None] = None):
    item = {'item_id': item_id, 'user_id': user_id}
    if q:
        item.update({"q": q})
    return item


"""
    the parameter is required when a default value is not set
    e.g.: "needy"
"""


@app.get('/required/{item_id}')
async def required_item(item_id: int, needy: str):
    item = {'item_id': item_id, "needy": needy}
    return item
