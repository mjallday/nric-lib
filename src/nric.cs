private static readonly int[] Multiples = { 2, 7, 6, 5, 4, 3, 2 };

public static bool IsNricValid(string nric)
{
	if (string.IsNullOrEmpty(nric))
	{
		return false;
	}

	//	check length
	if (nric.Length != 9)
	{
		return false;
	}

	int total = 0
		, count = 0
		, numericNric;
	char first = nric[0]
		, last = nric[nric.Length - 1];

	if (first != 'S' && first != 'T')
	{
		return false;
	}

	if (!int.TryParse(nric.Substring(1, nric.Length - 2), out numericNric))
	{
		return false;
	}

	while (numericNric != 0)
	{
		total += numericNric % 10 * Multiples[Multiples.Length - (1 + count++)];

		numericNric /= 10;
	}

	char[] outputs;
	if (first == 'S')
	{
		outputs = new char[] { 'J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A' };
	}
	else
	{
		outputs = new char[] { 'G', 'F', 'E', 'D', 'C', 'B', 'A', 'J', 'Z', 'I', 'H' };
	}

	return last == outputs[total % 11];

}

public static bool IsFinValid(string fin)
{
	if (string.IsNullOrEmpty(fin))
	{
		return false;
	}

	//	check length
	if (fin.Length != 9)
	{
		return false;
	}

	int total = 0
		, count = 0
		, numericNric;
	char first = fin[0]
		, last = fin[fin.Length - 1];

	if (first != 'F' && first != 'G')
	{
		return false;
	}

	if (!int.TryParse(fin.Substring(1, fin.Length - 2), out numericNric))
	{
		return false;
	}

	while (numericNric != 0)
	{
		total += numericNric % 10 * Multiples[Multiples.Length - (1 + count++)];

		numericNric /= 10;
	}

	char[] outputs;
	if (first == 'F')
	{
		outputs = new char[] { 'X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K' };
	}
	else
	{
		outputs = new char[] { 'R', 'Q', 'P', 'N', 'M', 'L', 'K', 'X', 'W', 'U', 'T' };
	}

	return last == outputs[total % 11];
}
