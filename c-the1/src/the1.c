/*	Created by Sercan Degirmenci on 07.04.2014
	degirmencisercan@gmailcom					*/
#include <stdlib.h>
#include <stdio.h>
#define MIN(a,b)(((a) < (b)) ? (a) : (b))
typedef struct virus virus;
struct virus{
	int width,height, initial,position,speed, interval,remain;
	virus *next;
};
virus *first, *temp = 0;
int * membranes;

void add_virus(int width, int height, int time, int pos, int speed, int interval, int amount)
{
	virus**temp2 = &first;
	for (; *temp2 != 0; temp2 = &(*temp2)->next){}
	(*temp2) = (virus*)malloc(sizeof(virus));
	(*temp2)->width = width;
	(*temp2)->height = height;
	(*temp2)->initial = time;
	(*temp2)->position = pos;
	(*temp2)->speed = speed;
	(*temp2)->interval = interval;
	(*temp2)->remain = amount;
	(*temp2)->next = 0;
}
void read_virus()
{
	int w, h, t, p, s, a, n;
	scanf("%d %d %d %d %d %d %d", &w, &h, &t, &p, &s, &a, &n);
	add_virus(w, h, t, p, s, a, n);
}
void attack(int start, int end, int power)
{
	for (; start <= end; start++){
		if (start < 0) continue;
		if (membranes[start] < power) membranes[start] = power;
	}
}
int step(virus * v, int time, int length)
{
	int t = time - v->initial;
	if (v->remain <= 0)return 0;
	if (t < 0)return 1;
	if (t%v->interval == 0)
	{
		v->remain--;
		attack(v->position, MIN(v->position + v->width - 1, length), v->height);
	}
	v->position += v->speed;
	return v->remain > 0;
}

int main(int argc, char ** argv)
{
	int r, v, i, cont = 1, time = 0;
	scanf("%d", &r);
	scanf("%d", &v);
	r += 1;
	membranes = (int*)malloc(sizeof(int)*r);
	for (i = 0; i < r; i++)	membranes[i] = 1;
	for (i = 0; i < v; i++)	read_virus();
	while (cont)
	{
		time++;
		cont = 0;
		for (temp = first; temp != 0; temp = temp->next)
			cont |= step(temp, time, r);
	}
	for (i = 0; i < r; i++)
		printf((i == r - 1) ? "%d" : "%d ", membranes[i]);
	return 0;
}