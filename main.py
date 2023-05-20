from fastapi import Response, status
from fastapi import FastAPI, UploadFile

from controller import predictMeat

app = FastAPI()


@app.post("/predict/", status_code=200)
async def predict(fileUpload: UploadFile, response: Response):
    res_predict = predictMeat(file=fileUpload)
    if (res_predict[0]):
        responseBody = res_predict[1]
        return responseBody
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {'message': 'ERROR'}


@app.get("/")
async def root():
    return {"message": "Hello I'm Beefy AI"}
