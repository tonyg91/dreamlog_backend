""" A DreamController Module """
from masonite.request import Request
from app.Dream import Dream
from masonite.controllers import Controller


class DreamController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request:Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", DreamController)
        """
        id = self.request.param("id")
        return Dream.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", DreamController)
        """
        return Dream.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", DreamController)
        """
        title = self.request.input("title")
        description = self.request.input("description")
        image = self.request.input("image")
        date = self.request.input("date")
        dream = Dream.create({"title": title, "description": description, "image": image, "date": date})
        return dream

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", DreamController)
        """
        id = self.request.param("id")
        title = self.request.input("title")
        description = self.request.input("description")
        image = self.request.input("image")
        date = self.request.input("date")
        Dream.where("id", id).update({"title": title, "description": description, "image": image, "date": date})
        return Dream.where("id", id).get()

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", DreamController)
        """
        id = self.request.param("id")
        dream = Dream.where("id", id).get()
        Dream.where("id", id).delete()
        return dream