#include "palindrome.h"
/**
 * is_palindrome - checks whether or not a
 * given unsigned integer is a palindrome.
 * @n: number
 * Return: palindrome
 */
int is_palindrome(unsigned long n)
{
	unsigned long aux = 0, n1 = n;

	while (n1)
	{
		aux = (aux * 10) + (n1 % 10);
		n1 /= 10;
	}
	return (n == aux ? 1 : 0);
}
