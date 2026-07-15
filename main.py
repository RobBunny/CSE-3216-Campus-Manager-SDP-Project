from fastapi import FastAPI
from routes.auth import router
from database.mongodb import MongoDB
from factories.university_factory import UniversityFactory
from factories.college_factory import CollegeFactory
from factories.factory_provider import FactoryProvider
from routes.notice import router as notice_router

db = MongoDB().get_db()
app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Backend Working"
    }

@app.get("/db-test")
def db_test():

    db.test.insert_one({
        "status": "connected"
    })

    return {
        "message": "Database Connected"
    }


@app.get("/singleton-test")
def singleton_test():

    db1 = MongoDB()
    db2 = MongoDB()

    return {
        "id1": id(db1),
        "id2": id(db2),
        "same_instance": db1 is db2
    }


@app.get("/factory-test/{organization}/{role}")
def factory_test(
    organization: str,
    role: str
):

    try:

        factory = FactoryProvider.get_factory(
            organization
        )

        if role.lower() == "teacher":

            user = factory.create_teacher(
                "Test User",
                "test@gmail.com",
                "123",
                "CSE"
            )

        elif role.lower() == "student":

            user = factory.create_student(
                "Test User",
                "test@gmail.com",
                "123",
                "221-15-1234"
            )

        elif role.lower() == "staff":

            user = factory.create_staff(
                "Test User",
                "test@gmail.com",
                "123",
                "Lab Assistant"
            )

        else:

            return {
                "message": "Invalid role"
            }

        return {
            "class_created": type(user).__name__
        }

    except ValueError as e:

        return {
            "error": str(e)
        }


app.include_router(router)
app.include_router(notice_router)