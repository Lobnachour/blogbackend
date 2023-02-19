from fastapi import APIRouter
from models.blog import Blog 
from config.db import conn 
from schemas.blog import serializeDict, serializeList
from bson import ObjectId
blog = APIRouter() 

@blog.get('/')
async def find_all_blogs():
    return serializeList(conn.local.blog.find())

@blog.get('/{id}')
async def find_one_blog(id):
    return serializeDict(conn.local.blog.find_one({"_id":ObjectId(id)}))

@blog.post('/')
async def create_blog(blog:Blog):
    conn.local.blog.insert_one(dict(blog))
    return serializeList(conn.local.blog.find())
