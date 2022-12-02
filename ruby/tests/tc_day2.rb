require_relative "../day2/solution2"
require "test/unit"

class TestSimpleNumber < Test::Unit::TestCase

  def test_solution1
    assert_equal(solution2_1(["A X", "C Z", "A Y"]), 18)
  end

  def test_solution2
    assert_equal(solution2_2(["A X", "C Z", "A Y"]), 14)
  end

end