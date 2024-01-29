import pytest

@pytest.fixture
def login(py):
    # TODO: Get these parameters from another file than pylenium.json

    py.visit(py.config.custom["environment"]["url"])
    py.get("[id='username']").type(py.config.custom["environment"]["username"])
    py.get("[id='password']").type(py.config.custom["environment"]["password"])
    py.get("[id='submit']").click()
    yield
    py.get("[id='avatar-item']").click()
    py.get("a[href='/logout/index']").click()
