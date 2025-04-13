def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке

    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

    # Функция должна проверить вхождение строки substring в строку full_string с помощью оператора assert и, \
    # в случае несовпадения, предоставить исчерпывающее сообщение об ошибке. \
    # https://stepik.org/lesson/36285/step/9?unit=162401