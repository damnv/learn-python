from fastapi import APIRouter
from configs.db import collection_student
from models.student import Student, Student_GPA
from schemas.serialize import serializeDict, serializeList
from schemas.student import studentsEntity
from bson import ObjectId
from fastapi import HTTPException

router = APIRouter(
    prefix="/student",
    tags=['Students']
)


@router.get('/')
async def get_student_list():
    data = serializeList(collection_student.find())
    if data:
        raise HTTPException(status_code=404, detail="Data not found")
    return {"status": True, "data": data}


@router.post('/gpa')
async def student_gpa(student: Student_GPA):
    print(student.class_room)
    data = studentsEntity(collection_student.find({"class_room": student.class_room.upper()}))
    if data:
        raise HTTPException(status_code=404, detail="Data not found")
    return {"status": True, "data": data}


@router.get('/{id}')
async def find_one_student(id):
    data = serializeDict(collection_student.find_one({"_id": ObjectId(id)}))
    return {"status": True, "data": data}


@router.post('/')
async def create_student(student: Student):
    _id = collection_student.insert_one(dict(student))
    data = serializeDict(collection_student.find_one({"_id": _id.inserted_id}))
    return {"status": True, "data": data}


@router.put('/{id}')
async def update_student(id, student: Student):
    collection_student.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(student)
    })
    data = serializeDict(collection_student.find_one({"_id": ObjectId(id)}))
    return {"status": True, "data": data}


@router.delete('/{id}')
async def delete_student(id):
    data = serializeDict(collection_student.find_one_and_delete({"_id": ObjectId(id)}))
    return {"status": True, "data": data}


