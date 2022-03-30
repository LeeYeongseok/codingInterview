#include <stdio.h>
#include <iostream>
#include <bitset>
using namespace std;


int main()
{
	int N = 0b10000000000;
	int M = 0b10011;

	int allOne = ~0;

	int i = 2;
	int j = 6;

	M <<= i;

	int left = allOne << j+1;
	int right = (1 << i) - 1;
	int mask = left | right;

	int blankN = N & mask;

	int ans = blankN | M;

	cout << bitset<32>(ans) << endl;

	return 0;
}