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
    }


]



@app.get("/books")
async def get_books(id:int):
    books_to_return=[]
    for book in BOOKS:
        if book['id']==id:
            books_to_return.append(book)
    return books_to_return
   


@app.get('/books/{id}')
async def return_autor_id_books(id:int,author_name:str):
    books_to_return=[]
    for book in BOOKS:
        if book.get('id')==id and book.get('author').casefold()==author_name.casefold():
            books_to_return.append(book)
    return books_to_return


if __name__=='__main__':
    
    
    uvicorn.run(app, host='127.0.0.1', port=8000)