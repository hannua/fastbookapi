from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define Book model using Pydantic
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: float

def __init__(self, id: int, title: str, author: str, description: str, rating: float):
    self.id = id
    self.title = title
    self.author = author
    self.description = description
    self.rating = rating

class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: float

# Sample data
Books: List[Book] = [
    Book(id=1, title="1984", author="George Orwell", description="Dystopian novel", rating=4.5),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", description="Fiction", rating=4.8),
    Book(id=3, title="The Great Gatsby", author="F. Scott Fitzgerald", description="Fiction", rating=4.2),
    Book(id=4, title="Pride and Prejudice", author="Jane Austen", description="Romance", rating=4.6),
    Book(id=5, title="The Catcher in the Rye", author="J.D. Salinger", description="Fiction", rating=4.0),
    Book(id=6, title="The Hobbit", author="J.R.R. Tolkien", description="Fantasy", rating=4.7)
]

# GET endpoint to return all books
@app.get("/books")
async def read_all_books():
    return Books

# POST endpoint to add a new book
@app.post("/create-books")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    Books.append(new_book)
    return new_book
