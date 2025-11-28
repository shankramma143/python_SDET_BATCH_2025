import pytest

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.sanity
def test_demo3_sample_one():
    print("Inside the sample one")
    a = "Basava"
    b = "QACircle"
    assert a.__eq__(b), "'Basava' is not Equal to 'QACircle'"

@pytest.mark.regression
def test_demo3_sample_two():
    print("Inside the sample two")
    a=2
    b=5
    assert a>b


@pytest.mark.regression
def test_demo3_sample_three():
    print("Inside the sample three")
    a=20
    b=30
    assert a.__eq__(b)