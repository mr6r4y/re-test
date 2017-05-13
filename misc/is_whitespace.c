int is_whitespace(char c) {
	switch (c) {
		case ' ': // fallthrough
		case '\t': // fallthrough
		case '\r': // fallthrough
		case '\n':
			return 1;
		default: // not whitespace
			return 0;
	}
}

int main(void) {
	is_whitespace('a');
	is_whitespace(' ');
	return 0;
}
