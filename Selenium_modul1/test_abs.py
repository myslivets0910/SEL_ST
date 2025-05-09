# def test_abs1():
    # assert abs(-42) == 42, "Should be absolute value of a number"

# if __name__ == "__main__":
    # python test_abs_project.pytest_abs1()
    # print("All tests passed!")

    #https://stepik.org/lesson/36285/step/10?unit=162401

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")