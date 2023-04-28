from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from fastapi import Response
from sqlalchemy.orm import Session

from db import schemas, crud
from db.main import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post('/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """ Create a new user and retrieves it. """
    user_db = crud.get_user_by_email(db, user.email)

    if user_db:
        raise HTTPException(status_code=400, detail='Email already registered')

    return crud.create_user(db=db, user=user)


@router.get('/', response_model=list[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """ Retrieve a list of users. """
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get('/{user_id}', response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return db_user


@router.patch('/{user_id}', response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated_user = crud.update_user(db, user_id, user)
    if updated_user:
        return updated_user

    return Response(status_code=HTTPStatus.BAD_REQUEST)


@router.delete('/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    row_count = crud.delete_user(db, user_id=user_id)
    if not row_count:
        raise HTTPException(status_code=404, detail='User not found')
    return Response(status_code=HTTPStatus.NO_CONTENT)
