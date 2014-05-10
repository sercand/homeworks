/*	Created by Sercan Degirmenci on 29.04.2014
	degirmencisercan@gmailcom					*/
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#define bool int
#define string char*
bool expression(string c, int index, int *end); /* run an expression such as (x & y) or (x | y) */
int resize_input(string c, int n);/* returns new size of input*/
int index_of_character(int c); /*Returns index of character in cases*/
void init_characters(), init_cases(), print_result(), sort_characters();
string characters; /* all characters in input*/
int ** cases; /*an array consist all cases. cases[n][n*n] */
string input;
int * results;
int case_number = 0, size_of_characters = 0, size_of_input = 0, size_of_cases = 0;

int main(int argc, char ** argv)
{
	int a, i, n = 0;
	input = (char*)malloc(0);
	while (1){
		a = getchar();
		size_of_input++;
		input = realloc(input, size_of_input*sizeof(char));
		if (a != EOF){
			input[size_of_input - 1] = a;
		}
		else{
			input[size_of_input - 1] = 0;
			break;
		}
	}
	size_of_input = resize_input(input, size_of_input);
	init_characters();
	init_cases();
	for (i = 0; i < size_of_cases; i++){
		case_number = i;
		results[i] = expression(input, 0, &n);
	}
	print_result();
	return 0;
}

bool expression(string s, int index, int *end)
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

int resize_input(string s, int n)
{
	int i = 0, j = 0, t = 1;
	string newi;
	for (; j < n; j++) if (s[j] > 32) i++; /* Count number of invalid chars */
	newi = malloc(sizeof(char)*(i + 3)); /* Init new init string. +3 is for first and last elements */
	for (j = 0; j < n; j++)	{
		if (s[j] > 32) newi[t++] = s[j]; /*If cc is bigger than 32 than it is valid*/
	}
	newi[0] = '(';
	newi[t] = ')';
	newi[t+1] = 0;
	input = newi;
	return i;
}

void init_characters()
{
	int i = 0;
	for (; i < size_of_input; i++){
		if (islower(input[i]) && index_of_character(input[i]) == -1){
			characters = realloc(characters, (++size_of_characters)*sizeof(char));
			characters[size_of_characters - 1] = input[i];
		}
	}
	sort_characters();
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

void sort_characters()
{
	int i, j, temp;
	for (i = 0; i < (size_of_characters - 1); i++){
		for (j = 0; j < size_of_characters - i - 1; j++){
			if (characters[j] > characters[j + 1]){
				temp = characters[j];
				characters[j] = characters[j + 1];
				characters[j + 1] = temp;
			}
		}
	}
}
