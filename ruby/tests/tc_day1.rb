require_relative "../day1/solution1"
require "test/unit"

class TestSimpleNumber < Test::Unit::TestCase

  def test_day1
    assert_equal(solution1_1(["1", "2", "3"]), 6)
    assert_equal(solution1_1([]), 0)
    assert_equal(solution1_1(["1", "\n", "2"]), 2)
  end

  def test_day1_2
    assert_equal(solution1_2(["1", "2", "3"]), 6)
    assert_equal(solution1_2([]), 0)
    assert_equal(solution1_2(["1", "\n", "2"]), 3)
    assert_equal(solution1_2(["1", "\n", "2", "\n", "3", "\n", "4"]), 9)
  end

end
