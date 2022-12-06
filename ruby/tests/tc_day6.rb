require_relative "../day6/solution6"
require "test/unit"

class TestSimpleNumber < Test::Unit::TestCase

    def test_sol1
        assert_equal(solution6_1(["bvwbjplbgvbhsrlpgdmjqwftvncz"]), 5)
        assert_equal(solution6_1(["nppdvjthqldpwncqszvftbrmjlhg"]), 6)
        assert_equal(solution6_1(["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"]), 10)
        assert_equal(solution6_1(["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]), 11)
    end

    def test_sol2
        assert_equal(solution6_2(["bvwbjplbgvbhsrlpgdmjqwftvncz"]), 23)
        assert_equal(solution6_2(["nppdvjthqldpwncqszvftbrmjlhg"]), 23)
        assert_equal(solution6_2(["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"]), 29)
        assert_equal(solution6_2(["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]), 26)
    end
end