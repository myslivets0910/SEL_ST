import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.xfail(strict=True, reason = "тест как ожидаемо падающий")
# Декоратор, который помечает тест как ожидаемо падающий. Если тест проходит, это будет считаться ошибкой, если strict=True
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False