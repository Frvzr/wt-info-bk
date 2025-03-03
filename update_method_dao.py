import asyncio
from uuid import uuid4
from pydantic import create_model
from sqlalchemy.ext.asyncio import AsyncSession
from src.dao.items import ItemDAO
from src.dao.session_maker import connection


@connection(commit=True)
async def update_item_description(session: AsyncSession, item_id: uuid4, new_description: str):
    value_model = create_model('ValueModel', description=(str, ...))
    await ItemDAO.update_one_by_id(session=session, data_id=item_id, values=value_model(description=new_description))


@connection(commit=True)
async def update_item(session: AsyncSession, item_id: uuid4, new_description: str, new_name: str):
    value_model = create_model('ValueModel', name=(str, ...), description=(str, ...))
    await ItemDAO.update_one_by_id(session=session, data_id=item_id, values=value_model(name=new_name, description=new_description))


@connection(commit=True)
async def update_item_category(session: AsyncSession, item_id: str, new_category: str):
    value_model = create_model('ValueModel', category_id=(str, ...))
    await ItemDAO.update_one_by_id(session=session, data_id=item_id, values=value_model(category_id=new_category))


# asyncio.run(update_item_description(item_id='92f20077-5373-4c70-8975-530def49dffe', new_description='O-ring'))
# asyncio.run(update_item(item_id='92f20077-5373-4c70-8975-530def49dffe', new_description='o-ring', new_name='T020'))
asyncio.run(update_item_category(item_id='56f5ac93-5f80-4f73-9c9c-1f7fe8fed887', new_category='42c21150-a0f5-4108-87df-4e58e46d2d5a'))

