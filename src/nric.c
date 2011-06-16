#include <stdio.h>
#include <stdlib.h> /* atoi */
#include <string.h> /* strlen */

int multiples[7] = { 2, 7, 6, 5, 4, 3, 2 };

int is_nric_valid(char* the_nric) {
	char* first;
	char* last;

	int numeric;
	int i;
	char outputs[11] = { 'J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A' };
	char outputs2[11] = { 'G', 'F', 'E', 'D', 'C', 'B', 'A', 'J', 'Z', 'I', 'H' };
	char *output;

	if (the_nric == NULL) {
		return 0;
	}

	if (strlen(the_nric) != 9) {
		return 0;
	}

	first = &the_nric[0];
	last = &the_nric[strlen(the_nric) - 1];

	if (*first != 'S' && *first != 'T') {
		return 0;
	}

	numeric = atoi(&the_nric[1]);

	if (*first == 'S') {
		output = outputs;
	} else {
		output = outputs2;
	}

	return check_mod_11(last, numeric, output);

}

int is_fin_valid(char* the_fin) {
	char* first;
	char* last;

	int numeric;
	int i;
	char outputs[11] = {  'X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K' };
	char outputs2[11] = { 'R', 'Q', 'P', 'N', 'M', 'L', 'K', 'X', 'W', 'U', 'T' };
	char* output;

	if (the_fin == NULL) {
		return 0;
	}

	if (strlen(the_fin) != 9) {
		return 0;
	}

	first = &the_fin[0];
	last = &the_fin[strlen(the_fin) - 1];

	if (*first != 'F' && *first != 'G') {
		return 0;
	}

	numeric = atoi(&the_fin[1]);

	if (*first == 'F') {
		output = outputs;
	} else {
		output = outputs2;
	}

	return check_mod_11(last, numeric, output);

}

int check_mod_11 (char* last, int numeric, char* outputs) {
	int total = 0;
	int count = 0;
	int len = 7;

	while (numeric != 0) {
		total += (numeric % 10) * multiples[len - (1 + count)];
		count ++;

		numeric /= 10;
	}

	if (*last == outputs[total % 11]) {
		return 1;
	}

	return 0;
}

main() {

	int a = is_nric_valid("G6046409Q");

	printf("0 == %d\n", a);

	a = is_nric_valid("S8944027J");

	printf("1 == %d\n", a);

	a = is_fin_valid("G6046409Q");

	printf("1 == %d\n", a);

	a = is_fin_valid("G604a409Q");

	printf("0 == %d\n", a);

	a = is_nric_valid("G604a409Q");

	printf("0 == %d\n", a);
}
