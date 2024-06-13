from fastapi import FastAPI

import routers


app = FastAPI()

app.include_router(routers.a16_1hogebat.router)