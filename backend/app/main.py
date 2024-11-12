from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from .routes.movie_routes import router as movie_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Thay URL frontend của bạn
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Trang Review Phim</title>
        </head>
        <body>
            <h1>Chào mừng đến với trang web review phim!</h1>
        </body>
    </html>
    """

app.include_router(movie_router, prefix="/api")
