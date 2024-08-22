from pydantic import BaseModel
from typing import List


class UserCreateInput(BaseModel):
    name: str


class UserFavoriteInput(BaseModel):
    user_id: int #alterar para UUID quando for utilizar 
    symbol: str

    class Config:
        from_attributes = True


class StandardOutput(BaseModel):
    message: str

    class Config:
        from_attributes = True


class Favorite(BaseModel):
    id: int
    symbol: str

    class Config:
        from_attributes = True


class UserOutput(BaseModel):
    id: int
    name: str
    favorites: List[Favorite]

    class Config:
        from_attributes = True


class DaySummaryOutput(BaseModel):
    highest: float
    lowest: float
    symbol: str
    
    class Config:
        from_attributes = True