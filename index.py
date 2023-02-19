from fastapi import FastAPI
from routes.blog import blog
app = FastAPI()
app.include_router(blog)
