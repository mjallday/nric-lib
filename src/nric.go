/*
 * Compile and run with 6g nric.go && 6l nric.6 && ./6.out
*/

package main

import (
    "fmt"
    "strconv"
)

var multiples = []int { 2, 7, 6, 5, 4, 3, 2 }

func isNricValid (theNric string) bool {

        if len(theNric) != 9 {
                return false
        }

        var first int = int(theNric[0])
        var last  int = int(theNric[len(theNric)-1])
        var outputs []int

        if first != 'S' && first != 'T' {
            return false
        }

        numeric, err := strconv.Atoi(theNric[1:len(theNric)-1])

        if err != nil {
                return false
        }

        if first == 'S' {
            outputs = []int{ 'J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A' }
        } else {
            outputs = []int{ 'G', 'F', 'E', 'D', 'C', 'B', 'A', 'J', 'Z', 'I', 'H' }
        }

        return checkMod11(last, numeric, outputs)

}

func isFinValid(theFin string) bool {

        if len(theFin) != 9 {
                return false
        }

        var first int = int(theFin[0])
        var last int = int(theFin[len(theFin)-1])
        var outputs []int

        if first != 'G' && first != 'F' {
            return false
        }

        numeric, err := strconv.Atoi(theFin[1:len(theFin)-1])

        if err != nil {
                return false
        }

        if first == 'F' {
            outputs = []int{ 'X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K' }
        } else {
            outputs = []int{ 'R', 'Q', 'P', 'N', 'M', 'L', 'K', 'X', 'W', 'U', 'T' }
        }

        return checkMod11(last, numeric, outputs)

}

func checkMod11 (last int, numeric int, outputs []int) bool {

        total := 0
        count := 0

        for numeric != 0 {
            total += (numeric % 10) * multiples[len(multiples) - (1 + count)]

            count += 1

            numeric /= 10
        }

        return last == outputs[int(total % 11)]

}

func main () {
        fmt.Printf("Hello, Go!\n")

        fmt.Printf("true==%t\n", isNricValid("S8944027J"))
        fmt.Printf("false==%t\n", isNricValid("S89a4027J"))
        fmt.Printf("false==%t\n", isNricValid("123"))
        fmt.Printf("true==%t\n", isFinValid("G6075119Q"))
        fmt.Printf("false==%t\n", isFinValid("G60721a9Q"))
        fmt.Printf("false==%t\n", isFinValid("G619Q"))
}

