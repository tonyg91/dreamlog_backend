"""CreateDreamsTable Migration."""

from masoniteorm.migrations import Migration


class CreateDreamsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("dreams") as table:
            table.increments("id")
            table.string("title")
            table.string("description")
            table.string("image")
            table.string("date")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("dreams")
