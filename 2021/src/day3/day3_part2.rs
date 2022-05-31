use self::file_utils::read_file;

#[path = "./../file_utils.rs"]
mod file_utils;

fn find_target_digit(lines: &Vec<String>, bit_pos: usize, most_common: bool) -> char {
	let mut one_count = 0;

	for line in lines.iter() {
		if line.get(bit_pos..bit_pos + 1).unwrap() == "1" { 
			one_count += 1;
		}
	}

	if most_common { 
		if one_count * 2 >= lines.len() { '1' } else { '0' }
	} else {
		if one_count * 2 >= lines.len() { '0' } else { '1' }
	}
}

fn find_target_num(lines: &mut Vec<String>, bit_pos: usize, finding_oxygen: bool) -> u32 {
	let bit_count = lines[0].len();
	let digit_to_keep = find_target_digit(lines, bit_pos, finding_oxygen);

	lines.retain(|x| x.chars().nth(bit_pos).unwrap() != digit_to_keep);

	if lines.len() == 1 || bit_pos > bit_count {
		u32::from_str_radix(lines[0].trim(), 2).unwrap()
	} else {
		find_target_num(lines, bit_pos + 1, finding_oxygen)
	}
}

pub fn run() {
	let lines = read_file("./inputs/day3.txt");

	let oxygen = find_target_num(&mut lines.clone(), 0, true);
	let co2 = find_target_num(&mut lines.clone(), 0, false);

	println!("Oxygen: {0} ({0:b}), CO2: {1} ({1:b}), Answer: {2}", oxygen, co2, oxygen * co2);
}