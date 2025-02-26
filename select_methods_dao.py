from src.dao.items import ItemDAO
from database import connection
from asyncio import run


@connection
async def select_all_items(session):
    return await ItemDAO.get_all_items(session)


all_items = run(select_all_items())
for i in all_items:
    print(i.to_dict())
