from fastapi import FastAPI
import uvicorn

BOOKS=[
    {
        "id":1,
        "title":"The Alchemist",
        "author":"Paulo Coelho",
        "price":200
    },
    {
        "id":2,
        "title":"The Subtle Art of Not Giving a F*ck",
        "author":"Mark Manson",
        "price":300
    },
    {
        "id":3,
        "title":"Atomic Habits",
        "author":"James Clear",
        "price":250
    },

]


app=FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get("/books")
async def get_books():
    return BOOKS



if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)