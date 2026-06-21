from fastapi import Depends, APIRouter
from repository.user_repo import UserRepository
from service.user_service import UserService

router = APIRouter()

def get_repository():
    return UserRepository()

def get_service(repo: UserRepository = Depends(get_repository)):
    return UserService(repo)

@router.get("/users")
def get_users(service: UserService = Depends(get_service)):
    return service.get_users()