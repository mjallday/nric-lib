require "test/unit"

class NRICValidator

    @@multiples = [ 2, 7, 6, 5, 4, 3, 2 ]

    def is_nric_valid(the_nric)

        return false if not the_nric
        return false if the_nric.length != 9

        total = count = 0
        first = the_nric[0]
        last = the_nric[the_nric.length - 1];

        return false if not ['S', 'T'].include?(first)

        begin
            numericNric = the_nric[1..the_nric.length - 2].to_i
        rescue
            return false
        end

        while numericNric != 0
            total += (numericNric % 10) * @@multiples[@@multiples.length - (1 + count)]

            count += 1

            numericNric /= 10
            numericNric = numericNric.floor
        end

        if first == 'S' then
            outputs = [ 'J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A' ]
        else
            outputs = [ 'G', 'F', 'E', 'D', 'C', 'B', 'A', 'J', 'Z', 'I', 'H' ]
        end

        return last == outputs[(total % 11).floor]

    end

    def is_fin_valid (fin)

        return false if not fin
        return false if fin.length != 9


        total = count = 0
        first = fin[0]
        last = fin[fin.length - 1]

        return false if not ['F', 'G'].include?(first)

        begin
            numericNric = fin[1..fin.length - 2].to_i
        rescue
            return false
        end

        while numericNric != 0
            total += (numericNric % 10) * @@multiples[@@multiples.length - (1 + count)]

            count += 1

            numericNric /= 10
            numericNric = numericNric.floor
        end

        if first == 'F' then
            outputs = [ 'X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K' ]
        else
            outputs = [ 'R', 'Q', 'P', 'N', 'M', 'L', 'K', 'X', 'W', 'U', 'T' ]
        end

        return last == outputs[(total % 11).floor]

    end

end



class TestSimpleNumber < Test::Unit::TestCase

    def test_fin
        v = NRICValidator.new

        puts 'unit test'
        assert_equal(true,  v.is_fin_valid('G6046409Q') )
        assert_equal(false, v.is_fin_valid('G60g6409Q') )
        assert_equal(false, v.is_fin_valid('123') )
        assert_equal(false, v.is_fin_valid(nil) )
    end

    def test_nric
        v = NRICValidator.new
        puts 'unit test'
        assert_equal(true,  v.is_nric_valid('S8944027J') )
        assert_equal(false, v.is_nric_valid('G60g2119Q') )
        assert_equal(false, v.is_nric_valid('123') )
        assert_equal(false, v.is_nric_valid(nil) )
    end

end