from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from schemas.users import UserRequest

from config.db_conf import get_db
from crud import users
from utils.response import success_response
from schemas.users import UserAuthResponse,UserInfoResponse
from utils.auth import get_current_user
from schemas.users import UserUpdateRequest

router = APIRouter(prefix="/api/users", tags=["users"])

@router.post("/register")
async def register(user_data:UserRequest,db:AsyncSession=Depends(get_db)):
    existing_user=await users.get_user_by_username(db, user_data.username)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="用户已经存在")
    user=await users.create_user(db, user_data)
    token=await users.create_token(db, user.id)


    # return {
    #     "code":200,
    #     "message":"user registered",
    #     "data":{
    #     "token":token,
    #     "userInfo":{
    #         "id":user.id,
    #         "username":user.username,
    #         "bio":user.bio,
    #         "avatar":user.avatar
    #         }
    #     }
    # }
    response_data=UserAuthResponse(token=token,user_info=UserInfoResponse.model_validate(user))
    return success_response(message="注册成功",data=response_data)


@router.post("/login")
async def login(user_data:UserRequest,db:AsyncSession=Depends(get_db)):
    user=await users.authenticate_user(db,user_data.username,user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="用户名或密码错误")
    token=await users.create_token(db,user.id)
    response_data=UserAuthResponse(token=token,user_info=UserInfoResponse.model_validate(user))
    return success_response(message="成功登录",data=response_data)


#查token查用户-》封装crud-》功能整合成一个工具函数-》路由导入使用:依赖注入
@router.get("/info")
async def get_user_info(user=Depends(get_current_user)):
    return success_response(message="获取用户信息成功",data=UserInfoResponse.model_validate(user))


#修改用户信息：验证token -》更新（用户输入数据 put提交 -》请求体参数 -》定义pydantic模型类） -》响应结果
#参数：用户输入的+验证token的+db（调用更新的方法
@router.put("/update")
async def update_user_info(user_data:UserUpdateRequest,user=Depends(get_current_user),db:AsyncSession=Depends(get_db)):
    user=await users.update_user(db,user.username,user_data)
    return success_response(message="获取用户信息成功",data=UserInfoResponse.model_validate(user))