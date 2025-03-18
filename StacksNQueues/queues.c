#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

typedef struct node {
	int val;
	struct node *next;
	struct node *prev;
} node;

typedef struct queue {
	node *head;
	node *tail;
} queue;

queue *createQ()
{
	queue *myQ = (queue *)malloc(sizeof(queue));
	myQ->head = NULL;
	myQ->tail = NULL;

	return (myQ);
}

void enqueue(queue *myQ, int val)		// add to end
{
	node *newNode = (node *)malloc(sizeof(node));
	newNode->val = val;
	newNode->next = NULL;
	newNode->prev = myQ->tail;

	if (myQ->tail)
	{
		myQ->tail->next = newNode;
	}
	else
	{
		myQ->head = newNode;
	}

	myQ->tail = newNode;
}

node *dequeue(queue *myQ)			// pull from head
{
	if (!myQ->head) {
        return NULL;
    }

    node *rtn = myQ->head;
    myQ->head = myQ->head->next;

    if (myQ->head) {
        myQ->head->prev = NULL;
    } else {
        myQ->tail = NULL;
    }

    rtn->next = NULL;
    rtn->prev = NULL;
    return rtn;
}

node *peek(queue *myQ)
{
	node *rtn = myQ->head;

	return (rtn);
}

int main(void)
{
	int i;
	queue *myQ = createQ();
	node *temp;

	for (i = 0; i < 5; i++)		//populate queue
	{
		enqueue(myQ, i);
		printf("Enqueueing: %d\n", i);
		usleep(200000);
		temp = peek(myQ);
		printf("peeking at head of myQ: %d\n", temp->val);
		usleep(200000);
	}
	printf("\n");
	sleep(1);
	while (myQ->head)		// peek and dequeue all values from stack
	{
		temp = peek(myQ);
		printf("peeking at head of myQ: %d\n", temp->val);
		usleep(200000);
		temp = dequeue(myQ);
		printf("Dequeueing: %d\n", temp->val);
		free(temp);
		usleep(200000);
	}

	free(myQ);
	return (0);
}