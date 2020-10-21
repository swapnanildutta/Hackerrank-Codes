// Apple and Orange
// https://www.hackerrank.com/challenges/apple-and-orange/problem

func solveApplesOranges(values: [Int], apples: [Int], oranges: [Int]) {
    var newapples = [Int]()
    var neworanges = [Int]()
    newapples = apples.map {values[2] + $0}
    neworanges = oranges.map {values[3] + $0}
    newapples = newapples.filter {$0 >= values[0] && $0 <= values[2]}
    neworanges = neworanges.filter {$0 >= values[0] && $0 <= values[1]}
    print(neworanges.count)
    print(neworanges.count)
}

let apples = [-2, 2, 1]
let oranges = [5, -6]
let objectData = [7, 11, 5, 15] // s, t, a, b

solveApplesOranges(values: objectData, apples: apples, oranges: oranges)
