import pandas as pd

import marshall


def test_square_root():
    square_root = marshall.python("Write a function that returns the square of a number")

    assert square_root(4) == 16
    assert square_root(2) == 4
    assert square_root(1) == 1
    assert square_root(0) == 0


def test_hash_function():
    hash_function = marshall.python("""
    Write a function that takes text as an argument and generates hash of that text using JUST ascii lower case letters.
        * Alphabet for has has 26 letters lowercase:
        * Hash should be 10 characters long
        * Hash should be unique for each text
        * Hash should be deterministic
    """)

    assert hash_function("hello world") == hash_function("hello world")
    assert not [a for a in hash_function("hello world") if a in list(range(0, 10))]
    assert len(hash_function("hello world")) == 10


def test_robot_language():
    robot_parser = marshall.python("""
    write a simple parser function in python that accepts code, and following code controls the robot.

    Robot can go straight and this will be represented as `s`
    Robot can turn left and this will be represented as `l`
    Robot can turn left and this will be represented as `r`

    with this code `sslssrss` would mean:
    - go straight
    - go straight
    - turn left
    - go straight
    - go straight
    - turn right
    - go straight
    - go straight

    Write lexer and parser in using rply library
    """)

    assert robot_parser("slsrs") == [
        "go straight",
        "turn left",
        "go straight",
        "turn right",
        "go straight",
    ]


def test_forecast_model():

    model = marshall.python("""
        Using pytorch library.

        Implement forecast model that takes two features 'load factor' and 'day of the week as input,
        and returns one feature as output 'load factor'.

        Use LSTM model with 2 layers and 64 hidden units.
    """)

    model_train = marshall.python("""

        Using pytorch library.

        Write the training loop function.

        * Model and dataset should be arguments to function
        * Use Mean Square Error as a loos function
        * Use Adam as the optimizer.
        * Use 1000 epochs.

    """)

    dataset_split = marshall.python("""
    For model training purposes, split panda dataframe in ration 80/20.

    Write a function.

    * The input dataframe contains multiple columns
    * The split should be applied on `day_of_week` field, in the way that training data will contain 80% of all Mondays, Tuesdays, Wednesdays, ...
    * Function should return two arguments, "training" and "test" data frames

    """)

    data = {
        'Name': ['John', 'Anna', 'Peter', 'Linda', 'John', 'Anna', 'Peter', 'Linda'],
        'day_of_week': [0, 0, 0, 0, 1, 1, 1, 1],
    }

    df = pd.DataFrame(data)

