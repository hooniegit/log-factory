from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.demo import *

router = APIRouter()

# update measurement
# confirmed
@router.get('/demo', response_class=PlainTextResponse)
async def demo(data_received):
    return create_error(data_received)
