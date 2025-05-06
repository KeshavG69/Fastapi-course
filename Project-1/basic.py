from fastapi import FastAPI
import uvicorn

app=FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/greet')
async def greet():
    return {'message': 'Hello Keshav'}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)