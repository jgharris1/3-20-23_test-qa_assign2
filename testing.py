from main import auto


def test_height_method_1():
    assert auto(1, 1, "1", 1) == 0.3302


def test_height_method_2():
    assert auto(1, 1, "2", 1) == 0.01


def test_height_method_3():
    assert auto(1, 1, "3", 1) == "unacceptable input '3' is not an accepted method"


def test_height_method_4():
    assert auto(1, 1, "aisdbfashfbd", 1) == "unacceptable input 'aisdbfashfbd' is not an accepted method"


def test_height_height_1_1():
    assert auto(1, 1, "1", 0) == 0.30479999999999996


def test_height_height_1_2():
    assert auto(1, 2, "1", 0) == 0.6095999999999999


def test_height_height_1_3():
    assert auto(1, 0, "1", 1) == 0.0254


def test_height_height_1_4():
    assert auto(1, 0, "1", 0) == "unacceptable inputs total height is zero inches"


def test_height_height_1_5():
    assert auto(1, -1, "1", 0) == "unacceptable input '-1' is negative"


def test_height_height_2_1():
    assert auto(1, 0, "1", 1) == 0.0254


def test_height_height_2_2():
    assert auto(1, 0, "1", 2) == 0.0508


def test_height_height_2_3():
    assert auto(1, 1, "1", 0) == 0.30479999999999996


def test_height_height_2_4():
    assert auto(1, 0, "1", 0) == "unacceptable inputs total height is zero inches"


def test_height_height_2_5():
    assert auto(1, 0, "1", -1) == "unacceptable input '-1' is negative"


def test_weight_method_1():
    assert auto(2, 1, "1") == 0.453592


def test_weight_method_2():
    assert auto(2, 1, "2") == 1


def test_weight_method_3():
    assert auto(2, 1, "3") == "unacceptable input '3' try again"


def test_weight_method_4():
    assert auto(2, 1, "afsdf") == "unacceptable input 'afsdf' try again"


def test_weight_weight_1():
    assert auto(2, 0, "1") == "unacceptable inputs total height is zero pounds"


def test_weight_weight_2():
    assert auto(2, 1, "1") == 0.453592


def test_weight_weight_3():
    assert auto(2, 2, "1") == 0.907184


def test_weight_weight_4():
    assert auto(2, -1, "2") == "unacceptable input '-1' is negative or zero"


def test_none_under_1():
    assert auto(3, -100, "2", 1, 1, "2") == "unacceptable input '-100' is negative or zero"


def test_none_under_2():
    assert auto(3, 0, "2", 1, 1, "2") == "unacceptable input '0' is negative or zero"


def test_none_under_3():
    assert auto(3, 100, "2", 1, 1, "2") == "bmi of 1.00 is considered underweight"


def test_under_norm_1():
    assert auto(3, 100, "2", 1, 18.4, "2") == "bmi of 18.40 is considered underweight"


def test_under_norm_2():
    assert auto(3, 100, "2", 1, 18.5, "2") == "bmi of 18.50 is considered normal weight"


def test_under_norm_3():
    assert auto(3, 100, "2", 1, 18.6, "2") == "bmi of 18.60 is considered normal weight"


def test_norm_over_1():
    assert auto(3, 100, "2", 1, 24.9, "2") == "bmi of 24.90 is considered normal weight"


def test_norm_over_2():
    assert auto(3, 100, "2", 1, 25, "2") == "bmi of 25.00 is considered overweight"


def test_norm_over_3():
    assert auto(3, 100, "2", 1, 25.1, "2") == "bmi of 25.10 is considered overweight"


def test_over_obe_1():
    assert auto(3, 100, "2", 1, 29.9, "2") == "bmi of 29.90 is considered overweight"


def test_over_obe_2():
    assert auto(3, 100, "2", 1, 30, "2") == "bmi of 30.00 is considered obese"


def test_over_obe_3():
    assert auto(3, 100, "2", 1, 30.1, "2") == "bmi of 30.10 is considered obese"


def test_obe_exre_1():
    assert auto(3, 100, "2", 1, 39.9, "2") == "bmi of 39.90 is considered obese"


def test_obe_exre_2():
    assert auto(3, 100, "2", 1, 40, "2") == "bmi of 40.00 is considered extremely obese"


def test_obe_exre_3():
    assert auto(3, 100, "2", 1, 40.1, "2") == "bmi of 40.10 is considered extremely obese"


def test_arbitrary():
    assert auto(3, 100, "2", 1, 12345, "2") == "bmi of 12345.00 is considered extremely obese"

