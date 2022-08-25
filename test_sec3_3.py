class TestExample():
  @classmethod
  def setup_class(cls):
    print("setup_function")

  @classmethod
  def teardown_class(cls):
    print("teardown_class")

  def test_example(self):
    print("hello world")

  def test_example2(self):
    print("pytest!")
