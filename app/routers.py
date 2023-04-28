from fastapi import APIRouter
from starlette.responses import RedirectResponse

from users.routers import router as user_router

router = APIRouter()


@router.get('/')
def index() -> RedirectResponse:
    """ Redirect to redoc page. """
    return RedirectResponse(url='/redoc')


router.prefix = "/api/v1"
router.include_router(user_router)
