import os
import pytest

from openpilot.common.prefix import OpenpilotPrefix


@pytest.fixture(scope="function", autouse=True)
def openpilot_function_fixture():
  starting_env = dict(os.environ)

  # setup a clean environment for each test
  with OpenpilotPrefix():
    yield

  os.environ.clear()
  os.environ.update(starting_env)


# If you use setUpClass, the environment variables won't be cleared properly,
# so we need to hook both the function and class pytest fixtures
@pytest.fixture(scope="class", autouse=True)
def openpilot_class_fixture():
  starting_env = dict(os.environ)

  yield

  os.environ.clear()
  os.environ.update(starting_env)
