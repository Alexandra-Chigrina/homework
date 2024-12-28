import os

from src.decorators import log


def test_log(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(25, 14)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_error(capsys):
    @log()
    def my_function(x, y):
        return x / y

    my_function(12, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: ZeroDivisionError. Inputs: (12, 0), {}\n"


def test_log_into_filename():
    @log("mylog.txt")
    def my_function(x, y):
        return x / y

    my_function(4, 7)
    with open(os.path.join("logs", "mylog.txt"), "r", encoding="utf-8") as file:
        data = file.read().split("\n")
    assert data[-2] == "my_function ok"

    my_function(4, 0)
    with open(os.path.join("logs", "mylog.txt"), "r", encoding="utf-8") as file:
        data = file.read().split("\n")
    assert data[-2] == "my_function error: ZeroDivisionError. Inputs: (4, 0), {}"
