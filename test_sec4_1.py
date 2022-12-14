import pytest

# 前処理
@pytest.fixture()
def setup_processing(request):
  print("setup_processing")
  def teardown_processing():
    print("teardown_processing")
  request.addfinalizer(teardown_processing)

# 後処理
def test_hello(setup_processing):
  print("hello")

def test_goodmorning():
  print("goodmorning")

def test_goodafternoon(setup_processing):
  print("goodafternoon")
