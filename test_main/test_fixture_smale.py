import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Посчитайте, сколько смайликов будет напечатано при выполнении этого тестового класса?

@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # какие-то проверки
    pass

    def test_second_smiling_faces(self, prepare_faces):
        # какие-то проверки
    pass

if __name__ == '__main__':
    TestPrintSmilingFaces.main()


# Фикстура prepare_faces используется в обоих методах тестирования.
# Фикстура very_important_fixture используется только в методе test_first_smiling_faces.
# Фикстура print_smiling_faces имеет параметр autouse=True, что означает, что она будет использоваться перед каждым тестом в классе.