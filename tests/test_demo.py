from demo import add


def test_add_intentionally_fails() -> None:
    # Intentional failure to trigger CI failure signals.
    assert add(1, 1) == 3