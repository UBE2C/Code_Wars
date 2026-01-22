
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <assert.h>
#include <stdbool.h>


// -- Structures --

typedef struct Node {
    int32_t data;
    struct Node* next_element;

} Node;

typedef struct Queue {
    Node* front_p;
    Node* back_p;

} Queue;


// -- Function prototypes --

void queue_enqueue(Queue* queue, int32_t data);
int32_t queue_dequeue(Queue *queue);
int32_t queue_front(const Queue *queue);
bool queue_is_empty(const Queue *queue);


int32_t main(void) {
    Queue mainQueue = {
        .front_p = NULL,
        .back_p = NULL

    };

    if (queue_is_empty(&mainQueue) == false) {
        printf("The value of the first node is %i\n", queue_front(&mainQueue));
    }

    queue_enqueue(&mainQueue, 5);
    queue_enqueue(&mainQueue, 10);

    if (queue_is_empty(&mainQueue) == false) {
        printf("The value of the first node is %i\n", queue_front(&mainQueue));
    }

    printf("The dequeued value of the first node is %i\n", queue_dequeue(&mainQueue));

    if (queue_is_empty(&mainQueue) == false) {
        printf("The value of the first node is %i\n", queue_front(&mainQueue));
    }

    printf("The dequeued value of the first node is %i\n", queue_dequeue(&mainQueue));

    if (queue_is_empty(&mainQueue) == false) {
        printf("The value of the first node is %i\n", queue_front(&mainQueue));
    }

    return 0;

}


// -- Function definitions --

/* Enqueues a new node onto the queue from the back. The links are pointing forward.
RETURN: none */
void queue_enqueue(Queue* queue, int32_t data) {
    // Create a new node on the heap
    Node* n = malloc(sizeof(Node));
    assert(n != NULL); //check if the memory allocation was successful

    // Initialize the new node variables
    n -> data = data;
    n -> next_element = NULL; //next node pointer is null as there is no next node

    // If the new node is the first one, set the front and back queue pointers accordingly
    if (queue -> front_p == NULL) {
        queue -> front_p = n;
        queue -> back_p = n;

    // Else set the back pointer accordingly
    } else {
        Node* prev_node = queue -> back_p; //take the previous node's pointer
        prev_node -> next_element = n; //update the previous node to point to the new node

        queue -> back_p = n; //move the back pointer to point to the new node

    }

}

/* Dequeues the first node from the queue and frees it's memory. Moves the front pointer to the next element.
RETURN: int32_t Node data */
int32_t queue_dequeue(Queue *queue) {
    // Assert that the queue is not empty before dequeueing
    assert(queue -> front_p != NULL);

    // Assign the front node's address to a pointer
    Node* n =  queue -> front_p;

    // Retrieve the data from the front node
    int32_t ret_data = n -> data;

    // Move the front pointer
    queue -> front_p = n -> next_element;

    // Check if the element was the last in queue and if yes set the back pointer to NULL
    if (queue -> front_p == NULL) {
        queue -> back_p = NULL;

    }

    // Free the memory of the first node
    free(n);

    // Return the output value
    return ret_data;

}

/* Retrieve the data from the first node of the queue. Does not frees it's memory. Does not move the front pointer to the next element.
RETURN: int32_t Node data */
int32_t queue_front(const Queue *queue) {
    // Assert that the queue is not empty before peeking
    assert(queue -> front_p != NULL);

    // Assign the front node's address to a pointer
    Node* n = queue -> front_p;

    // Retrieve the data from the front node
    int32_t ret_data = n -> data;

    // Return the output value
    return ret_data;

}

/* Checks if the queue is empty by based on the front pointer
RETURN: bool */
bool queue_is_empty(const Queue *queue) {
    return queue -> front_p == NULL ? true : false;

}
