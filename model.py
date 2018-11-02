from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))

def connect_to_db(app, db_uri="postgresql:///hobbies"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    Game.query.delete()

    gf = Game(game_id=1, name='football', description='throw a ball and tackle')
    gv = Game(game_id=2, name='volleyball', description='hit a ball over a net')
    gt = Game(game_id=3, name='tennis', description='hit a ball with racket')
    # FIXME: above, write a function that creates a game and adds it to the database.
    db.session.add_all([gf, gv, gt])
    db.session.commit()



if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
