/*Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of
 the number and for the multiples of five output “Buzz”. For numbers which are multiples 
 of both three and five output “FizzBuzz”.
*/
class Solution {
    var ans: [String] = []
    func fizzBuzz(_ n: Int) -> [String] {
        (1...n).forEach {
    ans.append($0 % 3 == 0 ? $0 % 5 == 0 ? "FizzBuzz": "Fizz": $0 % 5 == 0 ? "Buzz": "\($0)")
}
return ans
        }
        
    }