import io
import os.path
import uuid
from uuid import UUID

from fastapi import APIRouter, UploadFile, HTTPException, Depends
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import FileResponse

from auth.token import verify_token
from crud.records import create_record, get_record_by_uuid
from db.session import get_sesssion

record_router = APIRouter(tags=['/record'])

SAVE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/data/'


@record_router.post('/')
async def transform_track(user_uuid: str, access_token: str, file: UploadFile,
                          session: AsyncSession = Depends(get_sesssion)):
    if not verify_token(access_token, user_uuid):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='bad token'
        )

    if not file.filename.endswith('.wav'):
        # we can also check first bytes and/or content type header, but we won't
        raise (
            HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='wrong file format'
            )
        )

    wav_bytes = await file.read()
    record_uuid = uuid.uuid4()
    name = str(record_uuid) + file.filename[:-3] + 'mp3'
    transform_wav_to_mp3(wav_bytes, name)
    await create_record(str(SAVE_PATH + name), record_uuid, UUID(user_uuid), session)

    return f'http://localhost:8080/record?id={record_uuid}&user={user_uuid}'


@record_router.get('/')
async def get_record(id: str, user: str, session: AsyncSession = Depends(get_sesssion)):
    try:
        record_uuid = UUID(id)
        user_uuid = UUID(user)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='bad uuid'
        )

    res = await get_record_by_uuid(record_uuid, user_uuid, session)
    record = res.scalar_one_or_none()
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='not found'
        )

    return FileResponse(record.filepath)


def transform_wav_to_mp3(src: bytes, name: str):
    bio = io.BytesIO(src)
    try:
        sound = AudioSegment.from_wav(bio)
    except CouldntDecodeError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='bad file'
        )

    with open(SAVE_PATH + name, 'wb') as file:
        sound.export(file, format='mp3')
