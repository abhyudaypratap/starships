import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object(os.environ.get("APP_SETTINGS"))

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Starship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    hyperdrive_rating = db.Column(db.Float())

@manager.command
def update_starships():
    import json
    f = open('fixtures/starships.json',)
    starships_data = json.load(f)
    f.close()
    ship_entries =[ ]
    for ship in starships_data:
        new_entry = Starship(name=ship['name'],
                             hyperdrive_rating=ship['hyperdriveRating'])
        ship_entries.append(new_entry)
    db.session.add_all(ship_entries)
    db.session.commit()

if __name__ == '__main__':
    manager.run()