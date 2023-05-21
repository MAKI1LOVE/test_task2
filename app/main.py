import uvicorn as uvicorn
from fastapi import FastAPI

from db.session import init_db, close_db_connection
from routers.record import record_router
from routers.users import users_router

app = FastAPI(title='task2', version='1.0.0')

app.include_router(record_router, prefix='/record')
app.include_router(users_router, prefix='/users')


@app.on_event('startup')
async def startup():
    await init_db()


@app.on_event('shutdown')
async def shutdown():
    await close_db_connection()


if __name__ == '__main__':
    uvicorn.run(app, port=8080)
