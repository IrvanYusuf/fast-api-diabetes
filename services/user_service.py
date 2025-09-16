from interfaces.user_repository_interface import InterfaceUserRepository
from repositories.user_repository import UserRepository
from fastapi import HTTPException, status
from models import User


class UserService():

    def __init__(self, userRepositry: InterfaceUserRepository = UserRepository()):
        self.userRepository = userRepositry

    async def get_users(self, limit, offset):
        return await self.userRepository.get_all(limit, offset)

    async def create(self, user: User):
        return await self.userRepository.create(user)

    async def get_user(self, id: str):
        user = await self.userRepository.get_user(id)
        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
        return user

    async def get_user_by_name(self, name):
        user = await self.userRepository.get_by_name(name)
        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND,
                                f"User with name {name} not found")
        return user

    async def update(self, id: str, data: User):
        await self.get_user(id)
        return await self.userRepository.update(id, data)

    async def delete(self, id):
        await self.get_user(id)
        return await self.userRepository.delete(id)
