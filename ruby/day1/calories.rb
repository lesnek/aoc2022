class Elf
    attr_accessor :calories

    def initialize
        @calories = 0
    end

    def increase_cal(cal)
        @calories += cal
    end
end

def day1(data)
    elves = get_elves_with_calories(data)
    calories = convert_to_calories(elves)
    return calories.max
end

def day1_2(data)
    elves = get_elves_with_calories(data)
    calories = convert_to_calories(elves)
    return get_sum_of_top_3(calories)
end

def get_sum_of_top_3(calories)
    calories = calories.sort
    calories = calories.reverse
    return calories.take(3).sum
end

def convert_to_calories(elves)
    calories = []
    elves.each do |elf|
        calories.append(elf.calories)
    end
    return calories
end

def get_elves_with_calories(data)
    elves = [Elf.new]
    data.each do |line|
        if line == "\n"
            elves.append(Elf.new)
        else
        elves[-1].increase_cal(line.to_i)
        end
    end
    return elves
end

def parse_input(path)
    file = File.open(File.join(File.dirname(__FILE__), path))
    return file.readlines
end

puts "Maximum calories for one elf is: %d" % day1(parse_input("../../inputs/day1.txt"))
puts "Sum of top three calories per elf is: %d" % day1_2(parse_input("../../inputs/day1.txt"))