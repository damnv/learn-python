from fastapi import APIRouter
from configs.db import collection_user
from models.user import User
from schemas.serialize import serializeDict, serializeList
from bson import ObjectId

router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.get('/')
async def get_user_list():
    data = serializeList(collection_user.find())
    return {"status": True, "data": data}


@router.get('/{id}')
async def find_one_user(id):
    data = serializeDict(collection_user.find_one({"_id": ObjectId(id)}))
    return {"status": True, "data": data}


@router.post('/')
async def create_user(user: User):
    _id = collection_user.insert_one(dict(user))
    data = serializeDict(collection_user.find_one({"_id": _id.inserted_id}))
    return {"status": True, "data": data}


@router.put('/{id}')
async def update_user(id, user: User):
    collection_user.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })
    data = serializeDict(collection_user.find_one({"_id": ObjectId(id)}))
    return {"status": True, "data": data}


@router.delete('/{id}')
async def delete_user(id):
    data = serializeDict(collection_user.find_one_and_delete({"_id": ObjectId(id)}))
    return {"status": True, "data": data}
