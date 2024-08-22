from fastapi import APIRouter, HTTPException

from schemas import UserCreateInput, StandardOutput, UserFavoriteInput, DaySummaryOutput, UserOutput
from services import UserService, AssetService, FavoriteService
from database.models import User, Favorite

from typing import List

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')


@user_router.post('/create', response_model=StandardOutput)
async def create_user(user_input: UserCreateInput):
    try:
        await UserService.create_user(user_input.name)
        return StandardOutput(message="User created with successful!")
    
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    

@user_router.delete('/delete/{user_id}', response_model=StandardOutput)
async def user_delete(user_id: int):
    try:
        await UserService.delete_user(user_id)
        return StandardOutput(message=f"User id {user_id} was deleted with successful!")
    
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    

@user_router.get('/list_users', response_model=List[UserOutput])
async def list_users():
    try:
        return await UserService.list_users()
    
    except Exception as error:
        HTTPException(400, detail=str(error))


@user_router.get('/get_user/{user_id}', response_model=UserOutput)
async def get_user_by_id(user_id: int):
    try:
        user = await UserService.get_user_by_id(user_id)
        return UserOutput(id=user.id, name=user.name ,favorites=user.favorites)
    except Exception as error:
        raise HTTPException(400, detail=str(error))    


@user_router.post('/favorite/add')
async def user_favorite_add(user_favorite_input: UserFavoriteInput):
    try:
        await FavoriteService.add_favorite(user_favorite_input)
        return StandardOutput(message="Asset added to favorites")
    except Exception as error:
        HTTPException(400, error=str(error))


@user_router.post('/favorite/remove', response_model=StandardOutput)
async def user_favorite_remove(user_favorite_input: UserFavoriteInput):
    try:
        await FavoriteService.remove_favorite(user_favorite_input)
        return StandardOutput(message="Favorite was removed with successfull!")
    except Exception as error:
        HTTPException(400, error=str(error))


@assets_router.post("/day_summary", response_model=DaySummaryOutput)
async def get_day_summary(symbol: str):
    try:
        return await AssetService.day_summary(symbol)
    except Exception as error:
        raise HTTPException(400, error=str(error))
