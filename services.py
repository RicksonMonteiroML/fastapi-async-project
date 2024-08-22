from sqlalchemy import delete, and_
from sqlalchemy.future import select
from aiohttp import ClientSession
from datetime import date, timedelta

from database.models import User, Favorite
from database.connection import async_session
from schemas import UserFavoriteInput, DaySummaryOutput 


class UserService:
    async def create_user(name: str):
        async with async_session() as session:
            session.add(User(name=name))
            await session.commit()


    async def delete_user(user_id: int):
        async with async_session() as session:
            await session.execute(delete(User).where(User.id==user_id))
            await session.commit()


    async def list_users():
        async with async_session() as session:
            result = await session.execute(select(User))
            return result.scalars().all()


    async def get_user_by_id(user_id: int):
        async with async_session() as session:
            result = await session.execute(select(User).where(User.id == user_id))
            return result.scalar()
        
class FavoriteService:
    async def add_favorite(user_favorite_input: UserFavoriteInput):
        async with async_session() as session:
            session.add(Favorite(**user_favorite_input.model_dump()))
            await session.commit()


    async def remove_favorite(user_favorite_input: UserFavoriteInput):
        async with async_session() as session:
            await session.execute(delete(Favorite).where(and_(Favorite.user_id==user_favorite_input.user_id, Favorite.symbol==user_favorite_input.symbol)))
            await session.commit()

    
class AssetService:
    async def day_summary(symbol: str):
        async with ClientSession() as session:
            yesterday = date.today() - timedelta(days=1)
            url = f'https://www.mercadobitcoin.net/api/{symbol}/day-summary/{yesterday.year}/{yesterday.month}/{yesterday.day}/'
            
            response = await session.get(url)
            data = await response.json()

            return DaySummaryOutput(highest=data['highest'],
                                    lowest=data['lowest'],
                                    symbol=symbol)
