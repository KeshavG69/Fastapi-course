from fastapi import FastAPI, Body
import uvicorn
import ast
import json


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
    {
        "id":4,
        "title":"The Power of Now",
        "author":"Eckhart Tolle",
        "price":400
    },
    {
        "id":5,
        "title":"The 7 Habits of Highly Effective People",
        "author":"Stephen R. Covey",
        "price":350
    },
    {
        "id":2,
        "title":"Harry Potter and the Sorcerer's Stone",
        "author":"J.K. Rowling",
        "price":500
    },
    


]



@app.get("/books")
async def get_books(id:int):
    books_to_return=[]
    for book in BOOKS:
        if book['id']==id:
            books_to_return.append(book)
    return books_to_return
   


@app.post('/books/create_book')
async def create_new_book(book1=Body()):
    print(book1)
    print(type(book1))
    BOOKS.append(book1)
    return BOOKS

if __name__=='__main__':
    
    
    uvicorn.run(app, host='127.0.0.1', port=8000)
