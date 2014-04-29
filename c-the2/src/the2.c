/*	Created by Sercan Degirmenci on 29.04.2014
	degirmencisercan@gmailcom					*/
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#define FALSE 0
#define TRUE 1
#define bool int
#define string char*
#define EXP(e) bool exp##e(string c,int n);
EXP(And)/* & */
EXP(Or)/* | */
EXP(Not)/* - */
EXP(IfThen)/* > */
EXP(IsEqual)/* = */
int expression(string c, int n); /* run an expression such as (x & y) or (x | y) */
int resize_input(string c, int n);/* returns new size of input*/
int has_input_character(int c);
void init_characters();
void init_inputs();
void print_result();
void sort_characters();
string characters; /* all characters in input*/
int ** inputs; /*an array consist all inputs. inputs[n][n*n] */
string input;
int * results;
int index_of_input = 1, size_of_characters = 0, size_of_input = 0;

int main(int argc, char ** argv)
{
	char a;
	int i;
	input = (char*)malloc(0);
	while (1)
	{
		a = getchar();
		size_of_input++;
		input = realloc(input, size_of_input*sizeof(char));
		if (a != -1)
		{
			input[size_of_input - 1] = a;
		}
		else
		{
			input[size_of_input - 1] = 0;
			break;
		}
	}
	size_of_input = resize_input(input, size_of_input);
	init_characters();
	init_inputs();
	for (i = 1; i <= size_of_characters*size_of_characters; i++)
	{
		index_of_input = i;
		results[i - 1] = expression(input, size_of_input);
	}
	print_result();
	return 0;
}

bool expAnd(string c, int n)
{
	return FALSE;
}
bool expOr(string c, int n)
{
	return FALSE;
}
bool expNot(string c, int n)
{
	return FALSE;
}
bool expIfThen(string c, int n)
{
	return FALSE;
}
bool expIsEqual(string c, int n)
{
	return FALSE;
}
bool expression(string c, int n)
{
	return FALSE;
}
int resize_input(string c, int n)
{
	int i = 0, j = 0, t = 0;
	char * newi;
	for (; j < n; j++)
	{
		char cc = c[j];
		if (cc != ' '&&cc != '\n'&&cc != '\t'&&cc != '\r')
			i++;
	}
	newi = malloc(sizeof(char)*i);
	for (j = 0; j < n; j++)
	{
		char cc = c[j];
		if (cc != ' '&&cc != '\n'&&cc != '\t'&&cc != '\r'){
			newi[t] = cc;
			t++;
		}
	}
	input = newi;
	return i;
}
void init_characters()
{
	int i = 0;
	for (; i < size_of_input; i++)
	{
		if (islower(input[i]) && !has_input_character(input[i]))
		{
			size_of_characters++;
			characters = realloc(characters, size_of_characters*sizeof(char));
			characters[size_of_characters - 1] = input[i];
		}
	}
	sort_characters();
}
void init_inputs()
{
	int i = 0, j, k, l, m, n, t = 1;
	inputs = (int **)malloc(size_of_characters*sizeof(int*));
	n = size_of_characters*size_of_characters + 1;
	for (i = 0; i < size_of_characters; i++)
	{
		inputs[i] = (int*)malloc(n*sizeof(int));
	}
	results = (int*)malloc(n*sizeof(int));

	for (i = 0; i < size_of_characters; i++)
	{
		j = (size_of_characters - i) - 1;
		k = 1 << i;
		inputs[j][0] = characters[j];
		t = 1;
		for (l = 1; l < n;)
		{
			for (m = 0; m < k && l < n; m++, l++)
			{
				inputs[j][l] = t;
			}
			t = !t;
		}
	}
}
void print_result()
{
	int i = 0, j = 0, n = size_of_characters*size_of_characters;
	for (; i < size_of_characters; i++)
	{
		printf("%c ", characters[i]);
	}
	printf("R\n");
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < size_of_characters; j++)
		{
			printf("%c ", inputs[j][i + 1] ? 'T' : 'F');
		}
		printf("%c\n", results[i] ? 'T' : 'F');
	}
}
int has_input_character(int c)
{
	int i = 0;

	for (; i < size_of_characters; i++)
	{
		if (characters[i] == c)
		{
			return TRUE;
		}
	}
	return FALSE;
}

void sort_characters()
{
	int i, j, temp;

	for (i = 0; i < (size_of_characters - 1); i++)
	{
		for (j = 0; j < size_of_characters - i - 1; j++)
		{
			if (characters[j] > characters[j + 1])
			{
				temp = characters[j];
				characters[j] = characters[j + 1];
				characters[j + 1] = temp;
			}
		}
	}
}