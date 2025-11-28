import pytest
class TestLogin:
  def test_LoginByEmail(self):
      print("This is Login By Email")
      assert True==True


  def test_LoginByFacebook(self):
      print("This is Login By Facebook")
      assert True==True


  def test_LoginByTwitter(self):
      print("This is Login By Twitter")
      assert True==True


  @pytest.mark.skip
  def test_SignupByEmail(self):
      print("This is Signup By Email")
      assert True == True


  @pytest.mark.skip
  def test_SignupByFacebook(self):
      print("This is Signup By Facebook")
      assert True == True


  @pytest.mark.skip
  def test_SignupByTwitter(self):
      print("This is Signup By Twitter")
      assert True == True

