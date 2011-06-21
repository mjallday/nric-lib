class NricValidator () {

  val multiples = 2 :: 7 :: 6 :: 5 :: 4 :: 3 :: 2 :: Nil

  def isNricValid(theNric: String): Boolean = {

    if (theNric == Nil || theNric.length != 9)
      return false

    val first = theNric(0)
    val last = theNric(theNric.length - 1)
    var outputs: List[String] = Nil

    if (!(Array('S', 'T') contains first))
      return false

    var numeric: Int = 0
    try {
      numeric= theNric.slice(1, theNric.length - 1).toInt
    } catch { 
      case e => return false 
    }

    checkMod11(last, numeric, getArray(first) )
  }

  def isFinValid(theFin: String): Boolean = {
    if (theFin == Nil || theFin.length != 9)
      return false

    val first = theFin(0)
    val last = theFin(theFin.length -1)
    
    if (!(Array('F', 'G') contains first))
      return false
    
    var numeric: Int = 0
    try {
      numeric = theFin.slice(1, theFin.length - 1).toInt
    } catch { 
      case e =>return false 
    }
    
    checkMod11(last, numeric, getArray(first))
  }

  def getArray(first: Char): List[Char] = { 
    if (first == 'S')
      'J' :: 'Z' :: 'I' :: 'H' :: 'G' :: 'F' :: 'E' :: 'D' :: 'C' :: 'B' :: 'A' :: Nil
    else if (first == 'F')
      'X' :: 'W' :: 'U' :: 'T' :: 'R' :: 'Q' :: 'P' :: 'N' :: 'M' :: 'L' :: 'K' :: Nil
    else if (first == 'G')
      'R' :: 'Q' :: 'P' :: 'N' :: 'M' :: 'L' :: 'K' :: 'X' :: 'W' :: 'U' :: 'T' :: Nil
    else
      'G' :: 'F' :: 'E' :: 'D' :: 'C' :: 'B' :: 'A' :: 'J' :: 'Z' :: 'I' :: 'H' :: Nil
  }

  def checkMod11(last: Char, numeric: Int, outputs: List[Char]): Boolean = {
    var total = 0
    var count = 0
    var num = numeric

    while (num != 0) {
      total += (num % 10) * multiples(multiples.length - (1 + count))
      count += 1
      num /= 10
    }

    last == outputs(total % 11)

  }
}


object NricValidatorTest {
  def main(args: Array[String]) {

    val validator = new NricValidator()
    
    assert ( validator.isNricValid("S8944027J") == true) // True
    assert ( validator.isNricValid("G6046409Q") == false) // False
    assert ( validator.isNricValid("123") == false)       // False
    assert ( validator.isFinValid("G6046409Q") == true)  // True
    assert ( validator.isFinValid("123") == false)        // False
    assert ( validator.isFinValid("G6046a09Q") == false)  // False

  }
}
