/*	Created by Sercan Degirmenci on 29.04.2014
	degirmencisercan@gmailcom					*/
#include <stdlib.h>
#include <stdio.h>
/*
&  And
|  OR
-  Not
>  -> ise
=  isEqual
(  open bracket
)  close bracket
*/

#define EXP(e) int exp##e(char* c,int n);
EXP(And)/* & */
EXP(Or)/* | */
EXP(Not)/* - */
EXP(IfThen)/* > */
EXP(IsEqual)/* = */
int expression(char* c, int n);
int resize_input(char *c, int n);/* Returns new size of input*/
int * characters;
int ** inputs;
char * input;
int index_of_input = 1, size_of_chacters = 0;

int main(int argc, char ** argv)
{
	
	return 0;
}

int expAnd(char* c, int n)
{
	return 0;
}
int expOr(char* c, int n)
{
	return 0;
}
int expNot(char* c, int n)
{
	return 0;
}
int expIfThen(char* c, int n)
{
	return 0;
}
int expIsEqual(char* c, int n)
{
	return 0;
}
int expression(char* c, int n)
{
	return 0;
}
int resize_input(char *c, int n)
{
	return 0;
}
