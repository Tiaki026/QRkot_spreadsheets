from typing import Any, List, Optional, Type

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User


class CRUDBase:
    """Класс для работы с CRUD операциями."""

    def __init__(self, model) -> None:
        self.model = model

    async def get(
        self,
        obj_id: int,
        session: AsyncSession,
    ) -> Optional[Type[User]]:
        """Получение объекта."""
        db_obj = await session.execute(
            select(self.model).where(self.model.id == obj_id)
        )
        return db_obj.scalars().first()

    async def get_multi(
        self,
        session: AsyncSession,
    ) -> List[Type[User]]:
        """Получение всех объектов."""
        db_objs = await session.execute(select(self.model))
        return db_objs.scalars().all()

    async def create(
        self, obj_in, session: AsyncSession, user: Optional[User] = None
    ) -> Type[User]:
        """Создание нового объекта."""
        obj_in_data = obj_in.dict()
        if user is not None:
            obj_in_data["user_id"] = user.id
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update(
        self,
        db_obj,
        obj_in,
        session: AsyncSession,
    ) -> Type[User]:
        """Обновление объекта."""
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def remove(
        self,
        db_obj,
        session: AsyncSession,
    ) -> Type[User]:
        """Удаление объекта."""
        await session.delete(db_obj)
        await session.commit()
        return db_obj

    async def get_by_field(
        self, field, value, session: AsyncSession
    ) -> Optional[Any]:
        """Абстракция для получения объектов."""
        query = await session.execute(select(self.model).where(field == value))
        return query.scalars().first()
