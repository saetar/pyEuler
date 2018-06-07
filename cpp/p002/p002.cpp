#include "stdafx.h"
#include <iostream>
using namespace std;

int fib(int n)
{
	if (n < 2) return n;
	return fib(n - 1) + fib(n - 2);
}

int p002() {
	int cur = 0;
	int count = 1;
	int total = 0;
	while (cur < 4000000) {
		cur = fib(count);
		if (cur % 2 == 0) total += cur;
		count++;
	}
	return total;
}

int main()
{
	int ANSWER = p002();
	cout << ANSWER << endl;
	return 0;
}