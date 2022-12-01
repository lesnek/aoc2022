pub mod day1;
pub mod read;

fn main() {
    println!("Day1");
    let data1 = read::file_to_str_vec("../inputs/day1.txt");
    println!(
        "Maximum calories for one elf is: {}",
        day1::solution::day1(data1.clone())
    );
    println!(
        "Sum of top three calories per elf is: {}",
        day1::solution::day1_2(data1.clone())
    );
}
