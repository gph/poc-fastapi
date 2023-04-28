from pydantic import BaseModel, EmailStr, SecretStr


class User(BaseModel):
    """ User model. """
    id: int
    name: str
    email: EmailStr
    password: SecretStr
