def solution6(data, marker_len)
    marker = []
    index = 0
    data = data[0]

    while marker.length() < marker_len
        letters = data[index, marker_len]
        if letters.chars.uniq.length()  == marker_len
            marker = letters.chars
        end
        index += 1
    end

    return index + marker_len - 1
end

def solution6_1(data)
    solution6(data, 4)
end

def solution6_2(data)
    solution6(data, 14)
end

def parse_input(path)
    file = File.open(File.join(File.dirname(__FILE__), path))
    return file.readlines
end

puts solution6_1(parse_input("../../inputs/day6.txt"))
puts solution6_2(parse_input("../../inputs/day6.txt"))