def studentEntity(item) -> dict:
    gpa = (item['maths'] + item['literature'] + item['english']) / 3
    return {
        "_id": str(item['_id']),
        "class_room": item['class_room'],
        "maths": item['maths'],
        "literature": item['literature'],
        "english": item['english'],
        "gpa": round(gpa, 2)

    }


def studentsEntity(items) -> list:
    return [studentEntity(item) for item in items]

