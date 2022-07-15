from typing import List, Union,Dict

from beanie import PydanticObjectId
from models.category import Category

from models.user import User
from models.question import Question
from models.student import Student
from models.group import Group
from models.category import Category

user_collection = User
student_collection = Student
question_collection = Question
group_collection = Group
category_collection = Category


async def add_user(new_user: User) -> User:
    user = await new_user.create()
    return user


async def add_group(new_group: Group) -> Group:
    group = await new_group.create()
    return group

async def add_category(new_category: Category) -> Category:
    category = await new_category.create()
    return category

async def add_question(new_question: Question) -> Question:
    question = await new_question.create()
    return question

async def update_user_data(id: PydanticObjectId, data: dict) -> Union[bool, User]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in des_body.items()
    }}
    user = await user_collection.get(id)
    if user:
        await user.update(update_query)
        return user
    return False

async def retrieve_students() -> List[Student]:
    students = await student_collection.all().to_list()
    return students


async def add_student(new_student: Student) -> Student:
    student = await new_student.create()
    return student


async def retrieve_student(id: PydanticObjectId) -> Student:
    student = await student_collection.get(id)
    if student:
        return student


async def delete_student(id: PydanticObjectId) -> bool:
    student = await student_collection.get(id)
    if student:
        await student.delete()
        return True


async def update_student_data(id: PydanticObjectId, data: dict) -> Union[bool, Student]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in des_body.items()
    }}
    student = await student_collection.get(id)
    if student:
        await student.update(update_query)
        return student
    return False
