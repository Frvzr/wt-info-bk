from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models import Category, Group, Source, Operation, Department


class CategoryRepository:
    def __init__ (self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list:
        query = (select(Category.id, Category.name)
                 .select_from(Category))

        category = await self.session.execute(query)
        result = category.all()
        return list(result)


class GroupRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list:
        query = (select(Group.id, Group.name)
                 .select_from(Group))
        group = await self.session.execute(query)
        result = group.all()
        return list(result)


class SourceRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list:
        query = (select(Source.id, Source.name)
                 .select_from(Source))
        source = await self.session.execute(query)
        result = source.all()
        return list(result)


class OperationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list:
        query = (select(Operation.id, Operation.name)
                 .select_from(Operation))
        operation = await self.session.execute(query)
        result = operation.all()
        return list(result)


class DepartmentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list:
        query = (select(Department.id, Department.name)
                 .select_from(Department))
        department = await self.session.execute(query)
        result = department.all()
        return list(result)