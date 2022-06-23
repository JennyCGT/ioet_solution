from ioet_solution import __version__
from ioet_solution.code import main, divide_in_range
from datetime import datetime
FORMAT = '%H:%M'

def test_version():
    assert __version__ == '0.1.0'

def test_week_range1():
    hour_init = datetime.strptime('02:00', FORMAT)
    hour_end = datetime.strptime('08:00', FORMAT)
    output = divide_in_range('week', hour_init, hour_end)
    assert output == 150

def test_week_range2():
    hour_init = datetime.strptime('10:00', FORMAT)
    hour_end = datetime.strptime('17:00', FORMAT)
    output = divide_in_range('week', hour_init, hour_end)
    assert output == 105

def test_week_range3():
    hour_init = datetime.strptime('19:00', FORMAT)
    hour_end = datetime.strptime('23:00', FORMAT)
    output = divide_in_range('week', hour_init, hour_end)
    assert output == 80

def test_week_range1_2():
    hour_init = datetime.strptime('06:00', FORMAT)
    hour_end = datetime.strptime('15:00', FORMAT)
    output = divide_in_range('week', hour_init, hour_end)
    assert output == 165

def test_week_range2_3():
    hour_init = datetime.strptime('12:00', FORMAT)
    hour_end = datetime.strptime('20:00', FORMAT)
    output = divide_in_range('week', hour_init, hour_end)
    assert output == 130

def test_week_range1_3():
    hour_init = datetime.strptime('05:00', FORMAT)
    hour_end = datetime.strptime('22:00', FORMAT)
    output = divide_in_range('week', hour_init, hour_end)
    assert output == 315


def test_weekend_range1():
    hour_init = datetime.strptime('02:00', FORMAT)
    hour_end = datetime.strptime('08:00', FORMAT)
    output = divide_in_range('weekend', hour_init, hour_end)
    assert output == 180

def test_weekend_range2():
    hour_init = datetime.strptime('10:00', FORMAT)
    hour_end = datetime.strptime('17:00', FORMAT)
    output = divide_in_range('weekend', hour_init, hour_end)
    assert output == 140

def test_weekend_range3():
    hour_init = datetime.strptime('19:00', FORMAT)
    hour_end = datetime.strptime('23:00', FORMAT)
    output = divide_in_range('weekend', hour_init, hour_end)
    assert output == 100

def test_weekend_range1_2():
    hour_init = datetime.strptime('06:00', FORMAT)
    hour_end = datetime.strptime('15:00', FORMAT)
    output = divide_in_range('weekend', hour_init, hour_end)
    assert output == 210

def test_weekend_range2_3():
    hour_init = datetime.strptime('12:00', FORMAT)
    hour_end = datetime.strptime('20:00', FORMAT)
    output = divide_in_range('weekend', hour_init, hour_end)
    assert output == 170

def test_weekend_range1_3():
    hour_init = datetime.strptime('05:00', FORMAT)
    hour_end = datetime.strptime('22:00', FORMAT)
    output = divide_in_range('weekend', hour_init, hour_end)
    assert output == 400

def test_case_especial1():
    hour_init = datetime.strptime('00:00', FORMAT)
    hour_end = datetime.strptime('08:00', FORMAT)
    output = divide_in_range('week', hour_init, hour_end)
    assert output == 200

def test_case_especial2():
    hour_init = datetime.strptime('18:00', FORMAT)
    hour_end = datetime.strptime('00:00', FORMAT)
    output = divide_in_range('week', hour_init, hour_end)
    assert output == 120





