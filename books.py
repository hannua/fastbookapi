from fastapi import Body , FastAPI 


app = FastAPI()

Books = [
    { "title": "1984", "author": "George Orwell","category": "Dystopian"},
    { "title": "To Kill a Mockingbird", "author": "Harper Lee","category": "Fiction"},
    { "title": "The Great Gatsby", "author": "F. Scott Fitzgerald","category": "Fiction"},
    { "title": "Pride and Prejudice", "author": "Jane Austen","category": "Romance"},
    { "title": "The Catcher in the Rye", "author": "J.D. Salinger","category": "Fiction"},
    { "title": "The Hobbit", "author": "Harper Lee","category": "Fantasy"}
]



@app.get("/books")
async def read_all_books():
    return Books

#----------------------------------------------------------------------
#api for get_books_by_author
@app.get("/books/byauthor/{book_author}")
async def read_books_by_author_path(book_author: str):
    result = []
    for book in Books:
        if book.get('author').casefold() == book_author.casefold():
            result.append(book)
    return result




#----------------------------------------------------------------------
#api for get_books_by_title
 
@app.get("/books/title/{book_title}")
async def get_books_by_title(book_title: str):
    for book in Books:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return {"error": "Book not found"}

#----------------------------------------------------------------------
#api for get_books_by_author
@app.get("/books/")
async def getbooks_by_query(category: str):
    result = []
    for book in Books:
        if book.get('category').casefold() == category.casefold():
            result.append(book)
    return result

#----------------------------------------------------------------------

#api for author and category
@app.get("/books/{book_author}")
async def get_author_category_by_query(book_author: str , category: str):
    result = []
    for book in Books:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            result.append(book)
    return result

#----------------------------------------------------------------------
#api for create book
@app.post("/books/create_book")
async def create_book(new_book = Body()):
    Books.append(new_book)
    return {"message": "Book added successfully", "book": new_book}

#----------------------------------------------------------------------
    
#api for update book

@app.put("/books/update_book")
async def update_books(updated_book = Body()):
    for book in range(len(Books)):
        if Books[book].get('title').casefold() == updated_book["title"].casefold():
            Books[book] = updated_book
            return {"message": "Book updated successfully", "book": updated_book}
   
#----------------------------------------------------------------------     
#api for delete book
        
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for book in range(len(Books)):
        if Books[book].get('title').casefold()  == book_title.casefold():
            Books.remove(Books[book])
            return {"message": "Book deleted successfully", "book": Books[book]}
    return {"error": "Book not found"}


