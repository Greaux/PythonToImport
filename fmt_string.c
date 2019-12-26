#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void foo(const char *v)
{
	const size_t l = strlen(v);
	printf("* &l: %lX, l: %zu\n", &l, l);
	printf(v);
	printf("^ &l: %lX, l: %zu\n", &l, l);
}
int main(int argc, char *argv[])
{
	if (argc != 2) exit(1);
	foo(argv[1]);
	return 0;
}
