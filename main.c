#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main ()
{
	FILE *fp;
	long double val;
	fp = fopen("test", "r");

	while (fscanf(fp,"%Lf", &val) > 0)
	{
		printf("%Lf\n",rintl(val));
	}
	fclose(fp);
	return 0;
}
