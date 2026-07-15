from fastapi import APIRouter, HTTPException
from schemas.user_schema import RegisterRequest
from services.user_service import UserService
from factories.factory_provider import FactoryProvider

router = APIRouter()

@router.post("/register")
def register(request: RegisterRequest):

    try:
        factory = FactoryProvider.get_factory(
            request.organization
        )

        user = factory.create_user(
            request.role,
            request.name,
            request.email,
            request.password,
            request.department,
            request.student_id,
            request.designation,
            request.classroom
        )

        return UserService.register(user)

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )