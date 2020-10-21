// Get the Most frequenly character
func mostFreq(array: [AnyHashable]) -> String {
    // Dictionary to map value to count
    var counts = [AnyHashable: Int]()

    // Count the values with forEach function
    myArray.forEach { counts[$0] = (counts[$0] ?? 0) + 1 }

    // Find most frequent value and and the number of times it appears using max(by:)
    if let (value, count) = counts.max(by: {$0.1 < $1.1}) {
        return "the value: \(value) occurs \(count) times"
    }
    return ""
}

// Given the array
let myArray = ["a", 2, 4, 2, "b", 2, 3, 4, 2] as [AnyHashable]

// Let's print the result
let result = mostFreq(array: myArray)
print("result", result)
