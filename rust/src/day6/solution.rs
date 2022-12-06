use std::collections::HashSet;

fn solution(data: String, marker_len: u32) -> u32 {
    let mut marker: Vec<char> = vec![];
    let mut index = 0;

    while marker.len() < marker_len as usize {
        let letters: &str = &data[index as usize..marker_len as usize + index as usize];
        let hash_marker: HashSet<char> = letters.chars().collect();
        if hash_marker.len() == marker_len as usize {
            marker = letters.chars().collect()
        }
        index += 1
    }

    index + marker_len - 1
}

pub fn solution1(data: Vec<String>) -> u32 {
    solution(data[0].clone(), 4)
}

pub fn solution2(data: Vec<String>) -> u32 {
    solution(data[0].clone(), 14)
}

#[test]
fn test_solution1() {
    assert_eq!(solution1(vec!["bvwbjplbgvbhsrlpgdmjqwftvncz".to_string()]), 5);
    assert_eq!(solution1(vec!["nppdvjthqldpwncqszvftbrmjlhg".to_string()]), 6);
    assert_eq!(solution1(vec!["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg".to_string()]), 10);
    assert_eq!(solution1(vec!["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw".to_string()]), 11);
}
#[test]
fn test_solution2() {
    assert_eq!(solution2(vec!["bvwbjplbgvbhsrlpgdmjqwftvncz".to_string()]), 23);
    assert_eq!(solution2(vec!["nppdvjthqldpwncqszvftbrmjlhg".to_string()]), 23);
    assert_eq!(solution2(vec!["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg".to_string()]), 29);
    assert_eq!(solution2(vec!["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw".to_string()]), 26);
}
