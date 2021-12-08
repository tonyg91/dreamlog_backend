"""DreamTableSeeder Seeder."""
from app.Dream import Dream
from masoniteorm.seeds import Seeder


class DreamTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Dream.create({"title": "Flying", "description": "flying", "image":"https://cdn.mos.cms.futurecdn.net/bxV5MWwY9mKUviwStDzUGT.jpg", "date": "July 7th, 2015"})
        Dream.create({"title": "Falling", "description": "Falling", "image":"https://cdn.mos.cms.futurecdn.net/bxV5MWwY9mKUviwStDzUGT.jpg", "date": "July 7th, 2015"})
        Dream.create({"title": "Running", "description": "running", "image":"https://cdn.mos.cms.futurecdn.net/bxV5MWwY9mKUviwStDzUGT.jpg", "date": "July 7th, 2015"})
