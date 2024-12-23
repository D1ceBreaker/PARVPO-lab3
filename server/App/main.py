import uvicorn
from fastapi import FastAPI

from  import router
app = FastAPI()
app.include_router(router=router, prefix="")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host='7000')