var nric = [];

nric.multiples = [ 2, 7, 6, 5, 4, 3, 2 ];

nric.isNricValid = function (theNric) {

    if (!theNric || theNric == '')
    {
        return false;
    }

    if (theNric.length != 9)
    {
        return false;
    }

    var total = 0
        , count = 0
        , numericNric;
    var first = theNric[0]
        , last = theNric[theNric.length - 1];

    if (first != 'S' && first != 'T')
    {
        return false;
    }

    numericNric = theNric.substr(1, theNric.length - 2);

    if (isNaN(numericNric)) {
        return false
    }

    while (numericNric != 0)
    {
        total += (numericNric % 10) * nric.multiples[nric.multiples.length - (1 + count++)];

        numericNric /= 10;
        numericNric = Math.floor(numericNric);
    }

    var outputs;
    if (first == 'S')
    {
        outputs = [ 'J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A' ];
    }
    else
    {
        outputs = [ 'G', 'F', 'E', 'D', 'C', 'B', 'A', 'J', 'Z', 'I', 'H' ];
    }

    return last == outputs[total % 11];

}

nric.isFinValid = function(fin)
{
    if (!fin || fin == '')
    {
        return false;
    }

    if (fin.length != 9)
    {
        return false;
    }

    var total = 0
        , count = 0
        , numericNric;
    var first = fin[0]
        , last = fin[fin.length - 1];

    if (first != 'F' && first != 'G')
    {
        return false;
    }

   numericNric = fin.substr(1, fin.length - 2);

    if (isNaN(numericNric)) {
        return false;
    }

    while (numericNric != 0)
    {
        total += (numericNric % 10) * nric.multiples[nric.multiples.length - (1 + count++)];

        numericNric /= 10;
        numericNric = Math.floor(numericNric);
    }

    var outputs;
    if (first == 'F')
    {
        outputs = [ 'X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K' ];
    }
    else
    {
        outputs = [ 'R', 'Q', 'P', 'N', 'M', 'L', 'K', 'X', 'W', 'U', 'T' ];
    }

    return last == outputs[total % 11];
}