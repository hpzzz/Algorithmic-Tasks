import UIKit

var str = "Hello, playground"
var ans: [String] = []
//    print($0 % 3 == 0 ? $0 % 5 == 0 ? "FizzBuzz": "Fizz": $0 % 5 == 0 ? "Buzz": "\($0)")
        (1...100).forEach {
            ans.append($0 % 3 == 0 ? $0 % 5 == 0 ? "FizzBuzz": "Fizz": $0 % 5 == 0 ? "Buzz": "\($0)")
}
print(ans)
