import pytest
class Test_001:
    def setup_class(self):
        pass
    def test_001(self):
       assert 1
if __name__ == '__main__':
    pytest.main(["-s --alluredir report test_001.py"])