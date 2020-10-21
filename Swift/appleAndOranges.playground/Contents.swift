// Apple and Orange
// https://www.hackerrank.com/challenges/apple-and-orange/problem

func solveApplesAndOranges(s: Int, t: Int, a: Int, b: Int, apples: [Int], oranges: [Int]) -> Void {
    
    var new_apples = [Int]()
    var new_oranges = [Int]()
    
    new_apples = apples.map{a + $0}
    new_oranges = oranges.map{b + $0}
    new_apples = new_apples.filter{$0 >= s && $0 <= t}
    new_oranges = new_oranges.filter{$0 >= s && $0 <= t}
    
    print(new_oranges.count)
    print(new_oranges.count)
    
}

let apples = [-2,2,1]
let oranges = [5,-6]

solveApplesAndOranges(s: 7, t: 11,
                      a: 5, b: 15,
                      apples: apples,
                      oranges: oranges)
