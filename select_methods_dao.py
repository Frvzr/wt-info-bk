from src.dao.items import ItemDAO
from database import connection
from asyncio import run
from src.schemas.item import ItemNameIdSchema


@connection
async def select_all_items(session):
    return await ItemDAO.get_all_items(session)


@connection
async def select_items_id(session):
    return await ItemDAO.get_items_id(session)


@connection
async def select_item_by_name(session, item: str):
    rez = await ItemDAO.get_item_by_name(session=session, item=item)
    if rez:
        return ItemNameIdSchema.model_validate(rez)
    return {'message': f'Item not found'}


# all_items = run(select_all_items())
# for i in all_items:
#     print(i.to_dict())

# result = run(select_items_id())
# for i in result:
#     #data = {'id': i[0], 'item': i[1]}
#     data = ItemNameIdSchema.model_validate(i)
#     print(data)

data = run(select_item_by_name(item='T006'))
print(data)