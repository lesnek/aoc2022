struct Elf {
    calories: u32,
}

pub fn day1(data: Vec<String>) -> u32 {
    let elves = get_elves_with_calories(data);
    elves.into_iter().map(|elf| elf.calories).max().unwrap()
}

pub fn day1_2(data: Vec<String>) -> u32 {
    let elves = get_elves_with_calories(data);
    let mut cals = elves
        .into_iter()
        .map(|elf| elf.calories)
        .collect::<Vec<u32>>();
    cals.sort_unstable();
    cals.reverse();
    cals.into_iter().take(3).sum()
}

fn get_elves_with_calories(data: Vec<String>) -> Vec<Elf> {
    let mut elves = vec![Elf { calories: 0 }];
    let mut counter: u32 = 0;
    for line in data {
        if line == "".to_string() {
            elves.push(Elf { calories: 0 });
            counter += 1
        } else {
            elves[counter as usize].calories += line.parse::<u32>().unwrap();
        }
    }
    elves
}

#[test]
fn test_solution1() {
    assert_eq!(
        day1(vec!["1".to_string(), "".to_string(), "2".to_string()]),
        2
    );
}

#[test]
fn test_solution2() {
    assert_eq!(
        day1_2(vec![
            "1".to_string(),
            "".to_string(),
            "2".to_string(),
            "".to_string(),
            "3".to_string()
        ]),
        6
    );
}
