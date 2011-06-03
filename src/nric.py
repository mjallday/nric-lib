from math import floor

class NRICValidator(object):
    """
    Validates a Singaporean FIN or NRIC to ensure that it's algorithmically correct
    
    >>> NRICValidator().is_nric_valid('S8944027J')
    True
    >>> NRICValidator().is_fin_valid('G6046409Q')
    True
    >>> NRICValidator().is_nric_valid('S814A299Z')
    False
    >>> NRICValidator().is_fin_valid('G6075119Q')
    False
    
    """
    multiples = [ 2, 7, 6, 5, 4, 3, 2 ]

    def is_nric_valid(self, the_nric):
    
        if not the_nric:
            return False
    
        if len(the_nric) != 9:
            return False;
    
        total = count = 0
        first = the_nric[0]
        last = the_nric[-1];
    
        if first not in ['S','T']:
            return False
    
        try:
            numeric_nric = int(the_nric[1:-1])
        except ValueError:
            return False
    
        while numeric_nric != 0:
            total += (numeric_nric % 10) * self.multiples[len(self.multiples) - (1 + count)]
            
            count += 1
    
            numeric_nric /= 10
            numeric_nric = floor(numeric_nric)
                
        if first == 'S':
            outputs = [ 'J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A' ]
        else:
            outputs = [ 'G', 'F', 'E', 'D', 'C', 'B', 'A', 'J', 'Z', 'I', 'H' ]
    
        return last == outputs[int(total % 11)]
    

    def is_fin_valid (self, fin):
        
        if not fin:
            return False
    
        if len(fin) != 9:
            return False
    
        total = count = 0
        first = fin[0]
        last = fin[-1]
    
        if first not in ['F', 'G']:
            return False

        try:
            numeric_nric = int(fin[1:-1])
        except ValueError:
            return False
            
        while numeric_nric != 0:
            total += (numeric_nric % 10) * self.multiples[len(self.multiples) - (1 + count)]
            
            count += 1
    
            numeric_nric /= 10
            numeric_nric = floor(numeric_nric)
    
        if first == 'F':
            outputs = [ 'X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K' ]
        else:
            outputs = [ 'R', 'Q', 'P', 'N', 'M', 'L', 'K', 'X', 'W', 'U', 'T' ]
    
        return last == outputs[int(total % 11)]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
