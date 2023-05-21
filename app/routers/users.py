from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from auth.token import create_token
from crud.users import get_user_by_username, create_user
from db.session import get_sesssion
from schemas.user import User, UserCreate

users_router = APIRouter(tags=['/users'])


@users_router.post('/')
async def register_user(username: str, session: AsyncSession = Depends(get_sesssion)) -> dict:
    res = await get_user_by_username(username, session)
    user = res.scalar_one_or_none()
    if user:
        # alternative
        # raise HTTPException(
        #     status_code=starlette.status.HTTP_400_BAD_REQUEST,
        #     detail='User already created'
        # )
        user = User.from_orm(user)
        return {'uuid': user.uuid, 'access_token': user.access_token}

    new_user = UserCreate(username=username)
    access_token = create_token(str(new_user.uuid))
    new_user.access_token = access_token
    await create_user(new_user, session)

    return {'uuid': new_user.uuid, 'access_token': new_user.access_token}
