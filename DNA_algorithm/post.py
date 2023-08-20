from fastapi import FastAPI
from pydantic import BaseModel
from encrypt import encrypt
from decrypt import decrypt
from typing import Optional
from fastapi.staticfiles import StaticFiles
from evaluate import *
import os

app = FastAPI()
path = 'D:\\PyCharm\\bishe_algorithm\\data\\'
app.mount("/static", StaticFiles(directory="data"), name="data")

class Item(BaseModel):
    id: str = None
    imageUrl: str = None
    key: Optional[list] = None


@app.post('/encrypt')
async def Encrypt(item: Item):
    savePath = path + item.id
    encrypt(savePath, item.imageUrl),
    image1 = cv2.imread(savePath+'\\origin.png')
    image2 = cv2.imread(savePath+'\\encrypt.png')
    with open(savePath+'\\key.json', 'r', encoding='utf8')as fp:
        key = json.load(fp)
    Histogram(savePath, image1, image2)
    Correlation(savePath, 'correlation1', '原始图像', image1)
    Correlation(savePath, 'correlation2', '密文图像', image2)
    Information_Entropy(savePath, image1, image2)
    Key_Sensitive(savePath, key)
    NPCR(savePath, image2)
    UACI(savePath, image2)
    return {
        "url": "http://localhost:3000/static/"+item.id+"/encrypt.png",
        "key": "http://localhost:3000/static/"+item.id+"/key.json"
    }

@app.post('/decrypt')
async def Decrypt(item: Item):
    # item.imageUrl = './data/pic/lena_e.png'
    savePath = path + item.id
    decrypt(savePath, item.imageUrl, item.key)
    return {
        "url": "http://localhost:3000/static/"+item.id+"/decrypt.jpg"
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app,
                host="localhost",
                port=3000,
                workers=1)




