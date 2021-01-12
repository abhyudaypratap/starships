from starships.manage import Starship


def test_new_starship():
    """
    GIVEN a Starship model
    WHEN a new ship is created
    THEN check the name, and rating fields are defined correctly
    """

    ship = Starship(name='Galaxy 1', hyperdrive_rating=2.0)
    assert ship.name == 'Galaxy 1'
    assert ship.hyperdrive_rating == 2.0
