#include "palindrome.h"
/**
 * is_palindrome - checks whether or not a
 * given unsigned integer is a palindrome.
 * @n: number
 * Return: palindrome
 */
int is_palindrome(unsigned long n)
{
	int long nCopy = n;
	int long nCopy2 = n;
	int long divider = 1;
	int palindrome = 1;

	while (nCopy2 > 9)
	{
		nCopy2 /= 10;
		divider *= 10;
	}

	while (n > 9 && palindrome != 0)
	{
		int digit_1 = n / divider;
		int digit_2 = nCopy % 10;

		if (digit_1 == digit_2)
		{
			n %= divider;
			nCopy /= 10;
			divider = divider / 10;
		}
		else
			palindrome = 0;
	}

	return (palindrome);
}
