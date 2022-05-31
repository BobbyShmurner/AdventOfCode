use self::file_utils::read_file;

#[path = "./../file_utils.rs"]
mod file_utils;

enum Instructions {
	HPos,
	Depth,
	Null
}

fn parse_instruction(line: &str) -> (Instructions, i32) {
	let mut split = line.split(' ');

	let opcode: &str = split.next().expect("Failed to parse opcode");
	let operand: i32 = split.next().expect("Failed to parse operand").parse().expect("Failed to parse operand");

	match opcode.to_lowercase().as_str() {
		"forward" => { (Instructions::HPos, operand) }
		"down" => { (Instructions::Depth, operand) }
		"up" => { (Instructions::Depth, -operand) }
		_ => { eprintln!("Failed to parse instruction"); (Instructions::Null, 0) }
	}
}

pub fn run() {
	let lines = read_file("./inputs/day2.txt");

	let mut h_pos = 0;
	let mut depth = 0;

	for line in lines.iter() {
		let (opcode, operand) = parse_instruction(line);

		match opcode {
			Instructions::HPos => { h_pos += operand; }
			Instructions::Depth => { depth += operand; }
			_ => { eprintln!("Failed to execute instruction!"); }
		}
	}

	println!("HPos: {}, Depth: {}, Answer: {}", h_pos, depth, h_pos * depth);
}