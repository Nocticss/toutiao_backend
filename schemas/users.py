from pydantic import BaseModel

class UserRequest(BaseModel):
    username: str
    password: str

#user_info对应的类
class UserInfoResponse(BaseModel)
    pass




#data数据类型
class UserAuthResponse(BaseModel)
    token:str
    user_info:UserInfoResponse=Filed(...,alias="userInfo")
    


