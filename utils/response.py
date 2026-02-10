from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

#把成功的响应成果封装
def success_response(message:str="success",data=None):
    content={
        "code":200,
        "message":message,
        "data":data
    }
    
    return JSONResponse(content=jsonable_encoder(content)) 
