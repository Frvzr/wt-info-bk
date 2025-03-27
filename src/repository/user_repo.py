from sqlalchemy import select
from .base_repo import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import User


class UserRepository(BaseRepository[User]):
    def __init__(self, db: AsyncSession):
        super().__init__(User, db)

    async def get_by_email(self, email: str) -> User | None:
        result = await self.db.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def add_role(self, user_id: int, role_id: int) -> None:
        from ..models.user_role import UserRole
        user_role = UserRole(user_id=user_id, role_id=role_id)
        self.db.add(user_role)
        await self.db.commit()
