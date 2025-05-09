from fastapi import FastAPI
import uvicorn

app=FastAPI()


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

@app.get('/books/{book_id}')
async def get_book(book_id:int):
    return {'book_id': book_id}



@app.get("/books/1")
async def get_books():
    return BOOKS[0]


#Static apis should be above path parameter apis


if __name__=='__main__':
    
    uvicorn.run(app, host='127.0.0.1', port=8000, reload=True)