use std::io::{self,Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut iter = input.split_whitespace();
    let h1 : i32 = iter.next().unwrap().parse().unwrap();
    let b1: i32 = iter.next().unwrap().parse().unwrap();
    let h2: i32 = iter.next().unwrap().parse().unwrap();
    let b2: i32 = iter.next().unwrap().parse().unwrap();
    let p1 = h1*3+b1;
    let p2 = h2*3+b2;
    if p1>p2{
        println!("1 {}",p1-p2);
    }else if p2 >p1 {
        println!("2 {}",p2-p1);
    }else{
        println!("NO SCORE")
    }
}