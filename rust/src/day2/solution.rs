use std::collections::HashMap;

#[derive(Clone)]
struct GamePower {
    score: u32,
    oponent_label: String,
    win: Vec<String>,
    lose: Vec<String>,
}

struct Weapons {
    items: HashMap<String, GamePower>,
}

impl Weapons {
    fn new() -> Weapons {
        let scissors = GamePower {
            score: 3,
            oponent_label: "C".to_string(),
            win: vec!["B".to_string(), "Y".to_string()],
            lose: vec!["A".to_string(), "X".to_string()],
        };
        let paper = GamePower {
            score: 2,
            oponent_label: "B".to_string(),
            win: vec!["A".to_string(), "X".to_string()],
            lose: vec!["C".to_string(), "Z".to_string()],
        };
        let rock = GamePower {
            score: 1,
            oponent_label: "A".to_string(),
            win: vec!["C".to_string(), "Z".to_string()],
            lose: vec!["B".to_string(), "X".to_string()],
        };
        Weapons {
            items: HashMap::from([
                ("A".to_string(), rock.clone()),
                ("B".to_string(), paper.clone()),
                ("C".to_string(), scissors.clone()),
                ("X".to_string(), rock.clone()),
                ("Y".to_string(), paper.clone()),
                ("Z".to_string(), scissors.clone()),
            ]),
        }
    }
}

pub fn solution1(data: Vec<String>) -> u32 {
    let mut total_score: u32 = 0;
    for line in data {
        let items: Vec<&str> = line.trim().split(" ").collect();
        let (oponent, me) = (items[0].to_string(), items[1]);
        let me_w = Weapons::new().items.get(me).unwrap().clone();
        if me_w.win.contains(&oponent) {
            total_score += 6 + me_w.score;
        } else if oponent == me_w.oponent_label {
            total_score += 3 + me_w.score;
        } else {
            total_score += me_w.score;
        }
    }
    total_score
}

pub fn solution2(data: Vec<String>) -> u32 {
    let mut total_score: u32 = 0;
    for line in data {
        let items: Vec<&str> = line.trim().split(" ").collect();
        let (oponent, outcome) = (items[0], items[1]);
        let oponent_w = Weapons::new().items.get(oponent).unwrap().clone();
        if outcome == "Z" {
            total_score += Weapons::new().items.get(&oponent_w.lose[0]).unwrap().score + 6;
        } else if outcome == "X" {
            total_score += Weapons::new().items.get(&oponent_w.win[0]).unwrap().score;
        } else {
            total_score += oponent_w.score + 3;
        }
    }
    total_score
}

#[test]
fn test_solution1() {
    assert_eq!(
        solution1(vec![
            "A X".to_string(),
            "C Z".to_string(),
            "B Y".to_string()
        ]),
        15
    );
}
#[test]
fn test_solution2() {
    assert_eq!(
        solution2(vec![
            "A X".to_string(),
            "C Z".to_string(),
            "B Y".to_string()
        ]),
        15
    );
}
