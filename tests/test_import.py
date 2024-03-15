"""Test My Awesome Package Name."""

import my_awesome_package_name


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(my_awesome_package_name.__name__, str)
