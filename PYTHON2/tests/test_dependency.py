import pytest
from pytest_dependency import depends
# optional ⇒ from pytest_dependency import depends #still it work without import

#Case 1 Make assert True for all methods
class TestClass:
   @pytest.mark.dependency()
   def test_openApp(self):
       assert True


   @pytest.mark.dependency(depends=["TestClass::test_openApp"])
   #class name::first class test method
   def test_login(self):
       assert True


   #this method depends on previous method execution
   @pytest.mark.dependency(depends=["TestClass::test_login"])
   def test_search(self):
       assert True
   @pytest.mark.dependency(depends=["TestClass::test_login","TestClass::test_search"])
   def test_advancedsearch(self):
       assert True
   @pytest.mark.dependency(depends=["TestClass::test_login"])
   def test_logout(self):
       assert True

# Case 2 make assert False for open app method



   class TestClass:
       @pytest.mark.dependency()
       def test_openApp(self):
           assert False

       @pytest.mark.dependency(depends=["TestClass::test_openApp"])
       # class name::first class test method
       def test_login(self):
           assert  True

       # this method depends on previous method execution
       @pytest.mark.dependency(depends=["TestClass::test_login"])
       def test_search(self):
           assert True

       @pytest.mark.dependency(depends=["TestClass::test_login", "TestClass::test_search"])
       def test_advancedsearch(self):
           assert True

       @pytest.mark.dependency(depends=["TestClass::test_login"])
       def test_logout(self):
           assert True






