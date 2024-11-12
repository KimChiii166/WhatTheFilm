from ..models.movie_model import Movie

# Cập nhật danh sách phim với thuộc tính imageUrl
movies = [
    Movie(1, "Inception", "Sci-fi thriller about dreams.", 8.8, "https://cdn.sforum.vn/sforum/wp-content/uploads/2023/02/phim-hai-hay-4.jpg"),
    Movie(2, "The Godfather", "Crime family saga.", 9.2, "https://letrongdai.vn/wp-content/uploads/2020/05/8_top-bo-phim-chieu-rap-viet-nam-moi-va-hot-nhat-hien-nay.jpg"),
]

def get_all_movies():
    return [movie.__dict__ for movie in movies]

def get_movie_by_id(movie_id):
    movie = next((m for m in movies if m.id == movie_id), None)
    return movie.__dict__ if movie else None
