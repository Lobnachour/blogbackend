
def blogEntity(item) -> dict:
    return {
         "id":str(item["_id"]),
        "title":item["title"],
        "author":item["author"],
        "content":item["content"],
        "description":item["description"],
    }

def blogsEntity(entity) -> list:
    return [blogEntity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]