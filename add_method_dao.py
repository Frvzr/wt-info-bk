from src.dao.items import ItemDAO
from database import connection
from asyncio import run
from sqlalchemy.ext.asyncio import AsyncSession


@connection
async def add_item(item_data: dict, session: AsyncSession):
    new_item = await ItemDAO.add_item(session=session, item_data=item_data)
    print(f"Added new item with ID: {new_item.id}")
    return new_item.id

item_data_t006 = {
    "name": "T006",
    "description": "o-ring"
}

run(add_item(item_data=item_data_t006))
