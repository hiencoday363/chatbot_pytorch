from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from chat import chatbot
import time

class Item(BaseModel):
	text:str

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World"}

@app.post("/chat", tags=['chatbot'])
async def chat(item:Item):
	time.sleep(2)
	res = chatbot(item.text)
	return res


# c1
if __name__ == '__main__':
	uvicorn.run('server:app', port=8080, reload=True)

# c2 in cmd
'''
uvicorn server:app --reload
'''	