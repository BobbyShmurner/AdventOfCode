use self::file_utils::read_file;

#[path = "./../file_utils.rs"]
mod file_utils;

pub fn run() {
	let lines = read_file("./inputs/day1.txt");
	let mut depth_count = 0;

	let depths: Vec<u32> = lines.iter().flat_map(|line| line.parse()).collect();

	for i in 0..depths.len() {
		if i < 3 { continue; }

		if depths[i] + depths[i-1] + depths[i-2] > depths[i-1] + depths[i-2] + depths[i-3] {
			depth_count += 1;
		}
	}

	println!("Depth Increase Count: {}", depth_count);
}