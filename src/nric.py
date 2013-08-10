from math import floor


class NRICValidator(object):
    """
    Validates a Singaporean FIN or NRIC to ensure that it's algorithmically correct
    
    >>> NRICValidator.is_nric_valid('S8944027J')
    True
    >>> NRICValidator.is_fin_valid('G6046409Q')
    True
    >>> NRICValidator.is_nric_valid('S814A299Z')
    False
    >>> NRICValidator.is_fin_valid('G6075119Q')
    False
    >>> NRICValidator.is_nric_valid('123')
    False
    >>> NRICValidator.is_fin_valid('123')
    False
    """
    multiples = [2, 7, 6, 5, 4, 3, 2]
    
    @classmethod
    def is_valid(cls, nric_or_fin):
        validator = cls()
        if validator.is_nric_valid(nric_or_fin):
            return True
        elif validator.is_fin_valid(nric_or_fin):
            return True
        else:
            return False

    @classmethod
    def is_nric_valid(cls, the_nric):
    
        if not the_nric:
            return False
    
        if len(the_nric) != 9:
            return False;
    
        first = the_nric[0]
        last = the_nric[-1];
    
        if first not in ['S','T']:
            return False
    
        try:
            numeric = int(the_nric[1:-1])
        except ValueError:
            return False
                
        if first == 'S':
            outputs = ['J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
        else:
            outputs = ['G', 'F', 'E', 'D', 'C', 'B', 'A', 'J', 'Z', 'I', 'H']
    
        return cls.check_mod_11(last, numeric, outputs)
        
    @classmethod
    def is_fin_valid (cls, fin):
        
        if not fin:
            return False
    
        if len(fin) != 9:
            return False
    
        first = fin[0]
        last = fin[-1]
    
        if first not in ['F', 'G']:
            return False

        try:
            numeric = int(fin[1:-1])
        except ValueError:
            return False
    
        if first == 'F':
            outputs = ['X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K']
        else:
            outputs = ['R', 'Q', 'P', 'N', 'M', 'L', 'K', 'X', 'W', 'U', 'T']
    
        return cls.check_mod_11(last, numeric, outputs)
        
    @classmethod
    def check_mod_11(cls, last, numeric, outputs):

        total = count = 0
 
        while numeric != 0:
            total += (numeric % 10) * self.multiples[len(self.multiples) - (1 + count)]
            
            count += 1
    
            numeric /= 10
            numeric = floor(numeric)
        
        return last == outputs[int(total % 11)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
