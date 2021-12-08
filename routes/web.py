"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    RouteGroup([
        Get("/", "DreamController@index").name("index"),
        Get("/@id", "DreamController@show").name("show"),
        Post("/", "DreamController@create").name("create"),
        Put("/@id", "DreamController@update").name("update"),
        Delete("/@id", "DreamController@destroy").name("destroy"),
    ], prefix="/dream", name="dream")
]
