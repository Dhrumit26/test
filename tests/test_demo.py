from demo import add


def test_add_intentionally_fails() -> None:
    # Intentional failure to trigger CI failure signals.
    # This test will fail: add(1, 1) returns 2, but we assert it equals 3
    assert add(1, 1) == 2  # This will fail - triggering CI failure