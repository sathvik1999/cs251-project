#include <bits/stdc++.h>
using namespace std;
double fib(int n){
	double a=0,b=1;
	double count=0;
	while(count<n-1)
	{
		double c=a;
		a=b;
		b=b+c;
		count++;
	}
	return a;
}
int main()
{
float a=fib(102)*1.0/fib(101);
printf("%.7f",a);
}