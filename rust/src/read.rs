use std::fs;

pub fn file_to_str_vec(path: &'static str) -> Vec<String> {
    fs::read_to_string(path)
        .unwrap()
        .lines()
        .map(|v| v.to_owned())
        .collect()
}
