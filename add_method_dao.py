from database import connection
from asyncio import run
from sqlalchemy.ext.asyncio import AsyncSession

from src.dao.items import ItemDAO
from src.dao.categories import CategoryDAO

@connection
async def add_item(item_data: dict, session: AsyncSession):
    new_item = await ItemDAO.add_item(session=session, item_data=item_data)
    print(f"Added new item with ID: {new_item.id}")
    return new_item.id

@connection
async def add_category(category_data: dict, session: AsyncSession):
    new_category = await CategoryDAO.add_category(session=session, data=category_data)
    print(f"Added new item with ID: {new_category.id}")
    return new_category.id

item = {
    "name": "T008",
    "description": "o-ring",
    "category": "42c21150-a0f5-4108-87df-4e58e46d2d5a"
}

category = {
    "name": "SEAL",
    "description": "SEAL"
}

#run(add_category(category_data=category))
run(add_item(item_data=item))
