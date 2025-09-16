from models import User
from schema.schema import User as UserSchema
from services.user_service import UserService


class UserController():
    def __init__(self, userService: UserService = UserService()):
        self.userService = userService

    # Get all users with pagination

    async def get_users(self, limit: int = 10, offset: int = 0):
        users, total = await self.userService.get_users(limit, offset)
        return {
            "message": "success",
            "pagination": {"total": total, "limit": limit, "offset": offset},
            "data": users,
        }

    # Create user

    async def create_user(self, item: UserSchema):
        await self.get_user_by_name(item.name)
        user = User(name=item.name, age=item.age)
        await self.userService.create(user)
        return {"message": "success", "data": user}

    # Get single user

    async def get_user(self, user_id: str):
        user = await self.userService.get_user(user_id)
        return {"message": "success", "data": user}

    # Get user by name

    async def get_user_by_name(self, name: str):
        user = await self.userService.get_user_by_name(name)
        return {"message": "success", "data": user}

    # Update user

    async def update_user(self, user_id: str, item: UserSchema):
        user = await self.userService.update(user_id, item)
        return {"message": "success update user", "data": user}

    # Delete user
    async def delete_user(self, user_id: str):
        await self.userService.delete(user_id)
        return {"message": "success delete user", "data": []}
