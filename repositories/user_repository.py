from interfaces.user_repository_interface import InterfaceUserRepository
from models import User


class UserRepository(InterfaceUserRepository):

    async def get_all(self, limit, offset):
        users = await User.find_all().skip(offset).limit(limit).to_list()
        total = await User.find_all().count()
        return users, total

    async def get_by_name(self, name):
        user = await User.find_one(User.name == name)
        return user

    async def get_user(self, id):
        user = await User.get(id)
        return user

    async def create(self, user):
        return await User.create(user)

    async def update(self, id, data):
        user = await User.get(id)
        user.name = data.name
        user.age = data.age
        await user.save()
        return user

    async def delete(self, id):
        user = await User.get(id)
        return await user.delete()
