#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

typedef struct node {
	int val;
	struct node *next;
} node;

typedef struct stack {
	node *head;
} stack;

stack *createStack()
{
	stack *newStack = (stack *)malloc(sizeof(stack));
	newStack->head = NULL;

	return newStack;
}

void push(stack *myStack, int val)
{
	node *newNode = (node *)malloc(sizeof(node));
	newNode->val = val;
	newNode->next = myStack->head;
	myStack->head = newNode;
}

node *pop(stack *myStack)
{
	node *toPop;

	if (myStack->head)
	{
		toPop = myStack->head;
		myStack->head = myStack->head->next;
		toPop->next = NULL;
		return (toPop);
	}
	return (NULL);
}

node *peek(stack *myStack)
{
	node *toPeek = NULL;

	if (myStack->head)
		toPeek = myStack->head;
	return (toPeek);
}

int main (void)
{
	int i;
	stack *myStack = createStack();
	node *temp;

	for (i = 0; i < 5; i++)		//populate stack
	{
		push(myStack, i);
		printf("Pushing: %d\n", i);
		usleep(200000);
		temp = peek(myStack);
		printf("peeking at head of myStack: %d\n", temp->val);
		usleep(200000);
	}
	printf("\n");
	sleep(1);
	while (myStack->head)		// peek and pop all values from stack
	{
		temp = peek(myStack);
		printf("peeking at head of myStack: %d\n", temp->val);
		usleep(200000);
		temp = pop(myStack);
		printf("Popping: %d\n", temp->val);
		usleep(200000);
		free(temp);
	}

	free(myStack);
	return (0);
}
