import logging
import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from routes.instagram_routers import instagram_routers
from routes.users_routers import users_routes
from pathlib import Path

app = FastAPI()

app.include_router(instagram_routers, prefix="/instagram")
app.include_router(users_routes, prefix="/user")

if __name__ == "__main__":
    load_dotenv()
    file_name = os.getenv('SYSTEM_NAME')
    log_format = '%(asctime)s %(process)d-%(levelname)s-%(message)s'
    logging.basicConfig(filename=file_name + '.log',
                        level=logging.DEBUG,
                        format=log_format)
    uvicorn.run(f"{Path(__file__).stem}:app", host="0.0.0.0", port=8000)
