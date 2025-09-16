from abc import ABC, abstractmethod
from models import User


class InterfaceUserRepository(ABC):
    @abstractmethod
    async def get_all(self, limit: int, offset: int):
        pass

    @abstractmethod
    async def get_user(self, id: str):
        pass

    @abstractmethod
    async def get_by_name(self, name: str):
        pass

    @abstractmethod
    async def create(self, user: User) -> User:
        pass

    @abstractmethod
    async def update(self, id: str, user: User) -> User:
        pass

    @abstractmethod
    async def delete(self, id: str) -> bool:
        pass
