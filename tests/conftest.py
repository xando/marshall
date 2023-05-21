import pytest
import marshall.core as core


def pytest_addoption(parser):
    parser.addoption("--openai-key", action="store")
    parser.addoption("--openai-model", action="store")


@pytest.fixture(autouse=True, scope="session")
def openai_settings(pytestconfig):
    core.set_openai_key(pytestconfig.getoption("openai_key"))
    core.set_openai_model(pytestconfig.getoption("openai_model"))
