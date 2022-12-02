class GamePower
    attr_accessor :score, :oponent_label, :player_label, :win, :lose

    def initialize(score, oponent_label, player_label, win, lose)
        @score = score
        @oponent_label = oponent_label
        @player_label = player_label
        @win = win
        @lose = lose
    end
end

class Weapons

    SCISSORS = GamePower.new(3, "C", "Z", Array["B", "Y"], ["A", "X"])
    PAPER = GamePower.new(2, "B", "Y", ["A", "X"], ["C", "Z"])
    ROCK = GamePower.new(1, "A", "X", ["C", "Z"], ["B", "X"])

    WEAPONS = Hash["A" => ROCK, "B" => PAPER, "C" => SCISSORS, "X" => ROCK, "Y" => PAPER, "Z" => SCISSORS]
end

def solution1(data)
    total_score = 0
    data.each do |line|
        oponent, me = line.strip().split(" ")
        me = Weapons::WEAPONS[me]
        if me.win.include?(oponent)
            total_score += 6 + me.score
        elsif oponent == me.oponent_label
            total_score += 3 + me.score
        else
            total_score += me.score
        end
    end

    return total_score
end

def solution2(data)
    total_score = 0
    data.each do |line|
        oponent, outcome = line.strip().split(" ")
        oponent = Weapons::WEAPONS[oponent]
        if outcome == "Z"
            total_score += Weapons::WEAPONS[oponent.lose[0]].score + 6
        elsif outcome == "X"
            total_score += Weapons::WEAPONS[oponent.win[0]].score
        else
            total_score += oponent.score + 3
        end
    end

    return total_score
end

def parse_input(path)
    file = File.open(File.join(File.dirname(__FILE__), path))
    return file.readlines
end

puts "Score exploited is: %d" % solution1(parse_input("../../inputs/day2.txt"))
puts "Planned score is: %d" % solution2(parse_input("../../inputs/day2.txt"))