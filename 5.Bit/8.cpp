#include <stdio.h>
#include <iostream>
#include <bitset>
#include <list>
using namespace std;

void drawLine(char* screen, int width, int x1, int x2, int y) {
	int widthbyte = width / 8;
	int index = widthbyte * (y - 1); // y번째줄 첫번째 바이트

	int x1Byte = x1 / 8 + index;
	int x1Bit = x1 % 8;
	int x2Byte = x2 / 8 + index;
	int x2Bit = x2 % 8;

	if (x1Byte == x2Byte) {
		screen[x1Byte + 1] = (0xff >> x1Bit - 1) & (0xff << (8 - x2Bit));
	}

	else {
		for (int i = x1Byte + 2; i <= x2Byte; i++) {
			screen[i] = 0xff;
		}
		screen[x1Byte + 1] = 0xff >> (x1Bit + 1);
		screen[x2Byte + 1] = 0xff << (8 - x2Bit);
	}


}

int main()
{
	// 80*80 스크린이라 하면
	int width = 64;
	int height = 20;
	int x1 = 20;
	int x2 = 33;
	int y = 5;
	char* screen = new char[width * height / 8];

	fill_n(screen, width * height / 8, 0);

	drawLine(screen, width, x1, x2, y);

	for (int i = 0; i < width * height / 8; i++) {
		cout << bitset<8>(screen[i])<< " ";
		if (i % 8 == 7) {
			cout <<";"<< endl;
		}
	}

	return 0;
}