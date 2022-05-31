#[path = "./day1/day1_part1.rs"] mod day1_part1;
#[path = "./day1/day1_part2.rs"] mod day1_part2;
#[path = "./day2/day2_part1.rs"] mod day2_part1;
#[path = "./day2/day2_part2.rs"] mod day2_part2;
#[path = "./day3/day3_part1.rs"] mod day3_part1;
#[path = "./day3/day3_part2.rs"] mod day3_part2;
#[path = "./day4/day4_part1.rs"] mod day4_part1;
#[path = "./day4/day4_part2.rs"] mod day4_part2;

fn main() {
    println!("Please select what challenge to run in the format \"day.part\" (e.g. 3.2):");
    let mut choice = String::new();

    match std::io::stdin().read_line(&mut choice) {
        Ok(_) => { 
            match choice.trim() {
                "1.1" => { day1_part1::run(); }
                "1.2" => { day1_part2::run(); }
                "2.1" => { day2_part1::run(); }
                "2.2" => { day2_part2::run(); }
                "3.1" => { day3_part1::run(); }
                "3.2" => { day3_part2::run(); }
                "4.1" => { day4_part1::run(); }
                "4.2" => { day4_part2::run(); }
                
                _ => { println!("invalid Choice \"{}\"!", choice.trim()); }
            }
        }
        Err(e) => {
            println!("Failed to read line: {}", e);
        }
    }
}
