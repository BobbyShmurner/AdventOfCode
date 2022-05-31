use std::fs::File;
use std::io::Read;

pub fn read_file(path: &str) -> Vec<String> {
	let mut file = File::open(path).expect(&format!("Failed to open file \"{}\"", path));
	let mut contents = String::new();

	file.read_to_string(&mut contents).expect(&format!("Failed to read file \"{}\"", path));

	contents.split("\r\n").map(String::from).collect()
}