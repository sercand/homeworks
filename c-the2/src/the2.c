/*	Created by Sercan Degirmenci on 29.04.2014
	degirmencisercan@gmailcom					*/
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#define bool int
#define string char*
bool expression(const string c, const int index, int *end);			/* run an expression such as (x & y) or (x | y) */
int index_of_character(int c);										/* returns index of character in cases*/
void init_cases(), print_result();									/* necessary functions*/
string characters;													/* all characters in input*/
int ** cases;														/* an array consist all cases. cases[n][1<<n] */
string input;														/* input string to process*/
int * results;														/* all results will be saved to this*/
int case_number = 0, size_of_characters = 0, size_of_input = 2, size_of_cases = 0;
int compare(const void * a, const void * b)
{
	return (*(int*)a - *(int*)b);
}
int main(int argc, char ** argv)
{
	int a = 0, n = 0, t = 1;
	input = (string)malloc(sizeof(char)*size_of_input);
	characters = (string)malloc(0);
	input[0] = '(';			/*it is a small bug in algorithm so every input must be in (***) */
	while (a != EOF){		/*if a is not EndOfFile than continue*/
		a = getchar();		/*get next char*/
		if (a > 32){		/*it is a valid char. Not a space or new line or tab character*/
			size_of_input++;/*increase input size*/
			input = realloc(input, size_of_input*sizeof(char));		/* realloc input string*/
			input[t++] = a; /*save new char*/
			if (islower(a) && index_of_character(a) == -1){			/*Register character if it is not in character list*/
				characters = realloc(characters, (++size_of_characters)*sizeof(char)); /*increase character size*/
				characters[size_of_characters - 1] = a;				/* save new char*/
			}
		}
	}
	input[t] = ')';			/*Close brucket which is opened before*/
	qsort(characters, size_of_characters, sizeof(char), compare);/*Result must be sorted so sort it*/
	init_cases();			/*initialize of cases according to characters*/
	for (case_number = 0; case_number < size_of_cases; case_number++){
		results[case_number] = expression(input, 0, &n); /*Run case*/
	}
	print_result();			/*job is finished it is time to print it!*/
	return 0;
}

bool expression(const string s, const int index, int *end)
{
	int res1, res2, out, next;
	if (s[index] == '-'){
		return !(expression(s, index + 1, end));
	}
	else if (s[index] == '('){
		res1 = expression(s, index + 1, &out);
		next = s[out];
		if (next == ')'){
			(*end) = out + 1;
			return res1;
		}
		res2 = expression(s, out + 1, &out);
		(*end) = out + 1;
		if (next == '&') return res1 && res2;
		else if (next == '|') return res1 || res2;
		else if (next == '=') return res1 == res2;
		else if (next == '>') return (!res1) || res2;
	}
	else if (index_of_character(s[index]) > -1){
		(*end) = index + 1;
		return cases[index_of_character(s[index])][case_number];
	}
	return 0;
}

void init_cases()
{
	int i = 0, k, l, m, t = 1;
	cases = (int **)malloc(size_of_characters*sizeof(int*));
	size_of_cases = 1 << size_of_characters;
	for (i = 0; i < size_of_characters; i++){
		cases[i] = (int*)malloc(size_of_cases*sizeof(int));
	}
	results = (int*)malloc(size_of_cases*sizeof(int));
	for (i = 0; i < size_of_characters; i++, t = 1){
		k = 1 << i;
		for (l = 0; l < size_of_cases;)	{
			for (m = 0; m < k && l < size_of_cases; m++, l++){
				cases[(size_of_characters - i) - 1][l] = t;
			}
			t = !t;
		}
	}
}

void print_result()
{
	int i = 0, j = 0;
	for (; i < size_of_characters; i++)
		printf("%c ", characters[i]);
	printf("R\n");
	for (i = 0; i < size_of_cases; i++){
		for (j = 0; j < size_of_characters; j++)
			printf("%c ", cases[j][i] ? 'T' : 'F');
		printf("%c\n", results[i] ? 'T' : 'F');
	}
}

int index_of_character(int c)
{
	int i = 0;
	for (; i < size_of_characters; i++){
		if (characters[i] == c) return i;
	}
	return -1;
}