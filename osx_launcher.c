#include<stdlib.h>
#include <stdio.h>
#include <sys/dir.h>
#include <string.h>
#include <libgen.h>

#define MAXPATH 50
int main(int argc, char const *argv[]) {
	char *buffer = dirname(argv[0]);
	char path[MAXPATH];
	strcpy(path,buffer);
	free(buffer);
	strcat(path,"/entry.py");
	system(path);
	return 0;
}
