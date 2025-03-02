from src.dao.items import ItemDAO
from src.dao.session_maker import connection
from asyncio import run
from src.schemas.item import ItemNameIdSchema, ItemWithCategory, ItemSchema
from sqlalchemy.ext.asyncio import AsyncSession


@connection(isolation_level="READ COMMITTED")
async def select_all_items(session):
    return await ItemDAO.get_all_items(session)


@connection(isolation_level="READ COMMITTED")
async def select_items_id(session):
    return await ItemDAO.get_items_id(session)


@connection(isolation_level="READ COMMITTED")
async def select_item_by_name(session, item: str):
    rez = await ItemDAO.get_item_by_name(session=session, item=item)
    if rez:
        return ItemNameIdSchema.model_validate(rez)
    return {'message': f'Item not found'}


@connection(isolation_level="READ COMMITTED")
async def select_all_items_with_category(session):
    return await ItemDAO.get_item_with_category(session=session)


@connection(isolation_level="READ COMMITTED", commit=False)
async def select_all(session: AsyncSession, item: str):

    item = await ItemDAO.find_one_or_none(session=session, filters=ItemNameIdSchema(name=item))

    if item:
        # Преобразуем ORM-модель в Pydantic-модель и затем в словарь
        return ItemSchema.model_validate(item).model_dump()

    return {'message': f'Item не найден!'}

# all_items = run(select_all_items())
# for i in all_items:
#     print(i.to_dict())

# result = run(select_items_id())
# for i in result:
#     #data = {'id': i[0], 'item': i[1]}
#     data = ItemNameIdSchema.model_validate(i)
#     print(data)
#
# data = run(select_all_items_with_category())
# for i in data:
#     data = ItemWithCategory.model_validate(i)
#     print(data)

result = run(select_all(item='T006'))
print(result)
