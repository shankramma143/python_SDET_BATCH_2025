import pytest

@pytest.mark.smoke
def test_demo2_sample_one():
    print("Inside the sample one")

@pytest.mark.skip
@pytest.mark.smoke
def test_demo2_sample_two():
    print("Inside the sample two")
    assert 10==10

@pytest.mark.xfail
@pytest.mark.regression
@pytest.mark.smoke
def test_demo2_sample_three():
    print("Inside the sample three")