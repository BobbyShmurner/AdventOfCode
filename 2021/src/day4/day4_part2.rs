use self::file_utils::read_file;

#[path = "./../file_utils.rs"]
mod file_utils;

pub fn run() {
	let lines = read_file("./inputs/day4.txt");
}