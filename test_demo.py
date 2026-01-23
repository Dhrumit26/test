from demo import add


def test_add_intentionally_fails() -> None:
    assert add(1, 1) == 2