from src.repository.references_repo import (CategoryRepository, SourceRepository, GroupRepository, OperationRepository,
                                            DepartmentRepository)
from src.models import Category, Group, Source, Operation, Department


class CategoryService:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    async def get_all(self) -> list[Category]:
        return await self.repository.get_all()


class GroupService:
    def __init__(self, repository: GroupRepository):
        self.repository = repository

    async def get_all(self) -> list[Group]:
        return await self.repository.get_all()


class SourceService:
    def __init__(self, repository: SourceRepository):
        self.repository = repository

    async def get_all(self) -> list[Source]:
        return await self.repository.get_all()


class OperationServie:
    def __init__(self, repository: OperationRepository):
        self.repository = repository

    async def get_all(self) -> list[Operation]:
        return await self.repository.get_all()


class DepartmentService:
    def __init__(self, repository: DepartmentRepository):
        self.repository = repository

    async def get_all(self) -> list[Department]:
        return await self.repository.get_all()
