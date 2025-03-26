from typing import Generic, TypeVar, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: type[ModelType], db: AsyncSession):
        self.model = model
        self.db = db

    async def get(self, id: Any) -> ModelType | None:
        result = await self.db.execute(
            select(self.model).where(self.model.id == id)
        )
        return result.scalar_one_or_none()

    async def create(self, **kwargs) -> ModelType:
        instance = self.model(**kwargs)
        self.db.add(instance)
        await self.db.commit()
        await self.db.refresh(instance)
        return instance

    async def update(self, id: Any, **kwargs) -> ModelType | None:
        result = await self.db.execute(
            update(self.model)
            .where(self.model.id == id)
            .values(**kwargs)
            .returning(self.model)
        )
        await self.db.commit()
        return result.scalar_one_or_none()