"""
Tests for Day 1. Don't edit this file: it checks your work.
Run with:  python -m pytest day01
"""

from exercises import bytes_to_megabytes, traffic_report, session_duration


# Exercise 1
def test_bytes_exact_megabyte():
    assert bytes_to_megabytes(1048576) == 1.0


def test_bytes_five_megabytes():
    assert bytes_to_megabytes(5242880) == 5.0


def test_bytes_rounds_to_two_places():
    assert bytes_to_megabytes(1500000) == 1.43


def test_bytes_zero():
    assert bytes_to_megabytes(0) == 0.0


# Exercise 2
def test_traffic_basic():
    assert traffic_report("10.0.0.5", "1000", "500") == (
        1500,
        "Host 10.0.0.5 transferred 1500 bytes",
    )


def test_traffic_total_is_int_not_str():
    total, _ = traffic_report("8.8.8.8", "0", "64")
    assert isinstance(total, int), "The total should be an int, not text"
    assert total == 64


def test_traffic_message():
    _, message = traffic_report("192.168.1.20", "20", "22")
    assert message == "Host 192.168.1.20 transferred 42 bytes"


# Exercise 3
def test_duration_zero():
    assert session_duration(0) == "00:00:00"


def test_duration_padding():
    assert session_duration(65) == "00:01:05"


def test_duration_hours():
    assert session_duration(3661) == "01:01:01"


def test_duration_max_day():
    assert session_duration(86399) == "23:59:59"
