pub mod day1;
pub mod day2;
pub mod read;

fn main() {
    println!("Day1");
    let data1 = read::file_to_str_vec("../inputs/day1.txt");
    println!(
        "Maximum calories for one elf is: {}",
        day1::solution::solution1(data1.clone())
    );
    println!(
        "Sum of top three calories per elf is: {}",
        day1::solution::solution2(data1.clone())
    );
    println!("Day2");
    let data2 = read::file_to_str_vec("../inputs/day2.txt");
    println!(
        "Score exploited is: {}",
        day2::solution::solution1(data2.clone())
    );
    println!(
        "Planned score is: {}",
        day2::solution::solution2(data2.clone())
    );
}
