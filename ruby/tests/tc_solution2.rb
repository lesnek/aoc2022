require_relative "../day2/solution"
require "test/unit"

class TestSimpleNumber < Test::Unit::TestCase

  def test_solution1
    assert_equal(solution1(["A X", "C Z", "A Y"]), 18)
  end

  def test_solution2
    assert_equal(solution2(["A X", "C Z", "A Y"]), 14)
  end

end