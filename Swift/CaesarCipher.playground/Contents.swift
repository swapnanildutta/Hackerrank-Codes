//Problem Caesar Chiper
// https://www.hackerrank.com/challenges/caesar-cipher-1/problem

func encryptInput(input: String, rotation: Int) -> String {
    var encryptedString = String()
    for char in input.unicodeScalars {
        var code = Int(char.value)
        // is lowercased letter
        if (97...122).contains(char.value) {
            code += rotation
            while code > 122 {
                // reduce until in char range
                code -= (122 - 96)
            }
        // is uppercased letter
        } else if (65...90).contains(char.value) {
            code += rotation
            while code > 90 {
                // reduce until in char range
                code -= (90 - 64)
            }
        }
        encryptedString += String(Character(UnicodeScalar(code)!))
    }
    return encryptedString
}

encryptInput(input: "hola", rotation: 1)
