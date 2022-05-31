use self::file_utils::read_file;

#[path = "./../file_utils.rs"]
mod file_utils;

pub fn run() {
	let lines = read_file("./inputs/day3.txt");

	let line_count = lines.len();
	let bit_count = lines[0].len();

	let mut gamma = String::new();
	let mut one_counts:Vec<u32> = vec![0; bit_count];

	for line in lines.iter() {
		for (i, char) in line.chars().enumerate() {
			if char.to_digit(10).unwrap() == 1 { 
				one_counts[i] += 1;
			}
		}
	}

	for (i, count) in one_counts.iter().enumerate() {
		if count * 2 >= line_count as u32 {
			gamma.replace_range(i..i, "1");
		} else {
			gamma.replace_range(i..i, "0");
		}
	}

	let gamma = i32::from_str_radix(gamma.as_str(), 2).unwrap();
	let epsilon = gamma ^ (2i32.pow(bit_count as u32) - 1);

	println!("Gamma: {0} ({0:b}), Epsilon: {1} ({1:b}), Answer: {2}", gamma, epsilon, gamma * epsilon);
}