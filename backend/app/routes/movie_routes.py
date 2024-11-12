from fastapi import APIRouter
from ..controllers.movie_controller import get_all_movies, get_movie_by_id

router = APIRouter()

@router.get("/movies")
def fetch_movies():
    return get_all_movies()

@router.get("/movies/{movie_id}")
def fetch_movie(movie_id: int):
    movie = get_movie_by_id(movie_id)
    if not movie:
        return {"error": "Movie not found"}
    return movie
