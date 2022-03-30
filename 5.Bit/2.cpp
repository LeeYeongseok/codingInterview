#include <stdio.h>
#include <iostream>
#include <bitset>
using namespace std;

string binary(double number) {
	if (number >= 1 || number <= 0) {
		return "ERROR";
	}

	string ans = "0.";
	int count = 0;

	while (number != 0.0 && count < 32){
		number *= 2;
		if (number >= 1) {
			ans += "1";
			number -= 1;
		}
		else {
			ans += "0";
		}
		count++;
	}
	if (number != 0.0 && count == 32) {
		return "ERROR";
	}
	return ans;
}

int main()
{
	double number = 0.625;

	cout << binary(number) << endl;

	return 0;
}