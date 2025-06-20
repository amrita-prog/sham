from fastapi import APIRouter
from pydantic import BaseModel
import uuid
from sh.firebase_setup import db  

router = APIRouter()

# Define input schema
class Teacher(BaseModel):
    name: str
    subject: str
    email: str
    phone: str

# POST /teacher
@router.post("/teacher")
def add_teacher(teacher: Teacher):
    doc_id = str(uuid.uuid4())
    db.collection("teachers").document(doc_id).set(teacher.dict())
    return {"message": f"✅ Teacher {teacher.name} added successfully."}

# GET /teachers
# @router.get("/teachers")
# def get_teachers():
#     teachers_ref = db.collection("teachers").stream()
#     return [
#         {
#             "id": doc.id,
#             **doc.to_dict()
#         }
#         for doc in teachers_ref
#     ]


