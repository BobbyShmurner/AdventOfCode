use self::file_utils::read_file;

#[path = "./../file_utils.rs"]
mod file_utils;

pub fn run() {
	let lines = read_file("./inputs/day1.txt");
	let mut depth_count = 0;

	let depths: Vec<u32> = lines.iter().flat_map(|line| line.parse()).collect();

	for (i, depth) in depths.iter().enumerate() {
		if i == 0 { continue; }

		if depth > &depths[i-1] {
			depth_count += 1;
		}
	}

	println!("Depth Increase Count: {}", depth_count);
}