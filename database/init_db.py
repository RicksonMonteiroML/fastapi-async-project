from asyncio import run
from models import Base
from connection import engine



async def create_database():
    async with engine.begin() as connection:
        
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)

if __name__ == '__main__':
    run(create_database())