import pytest
class TestClass:
   @pytest.mark.third
   def test_methodC(self):
       print("Running Method C")


   @pytest.mark.fourth
   def test_methodD(self):
       print("Running Method D")


   @pytest.mark.fifth
   def test_methodE(self):
       print("Running Method E")


   @pytest.mark.first
   def test_methodA(self):
       print("Running Method A")


   @pytest.mark.second
   def test_methodB(self):
       print("Running Method B")
