// -- Manage header files --

#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <assert.h>




// -- Manage structs --

typedef struct Node {
    int32_t data;
    struct Node* previous_node;
    struct Node* next_node;

} Node;


typedef struct Deque {
  Node* front_node;
  Node* back_node;

} Deque;


// -- Manage function prototypes --

void deque_push_front(Deque *deque, int data);
int32_t deque_pop_front(Deque *deque);
int32_t deque_peek_front(const Deque *deque);
void deque_push_back(Deque *deque, int data);
int32_t deque_pop_back(Deque *deque);

int32_t deque_peek_back(const Deque *deque);
bool deque_is_empty(const Deque *deque);


// -- Main function --
//
int32_t main(void) {

    // Init the main deque
    Deque mainDeque = {
        .front_node = NULL,
        .back_node = NULL
    };


    // Test deque operations - front operations
    if (deque_is_empty(&mainDeque) == false) {
        printf("The value of the first node is %i\n", deque_peek_front(&mainDeque));
    } else {
        printf("The deque is empty.\n");

    }

    deque_push_front(&mainDeque, 5);
    deque_push_front(&mainDeque, 10);

    if (deque_is_empty(&mainDeque) == false) {
        printf("The value of the first node is %i\n", deque_peek_front(&mainDeque));
    } else {
        printf("The deque is empty.\n");

    }

    printf("The popped value of the first node is %i\n", deque_pop_front(&mainDeque));

    if (deque_is_empty(&mainDeque) == false) {
        printf("The value of the first node is %i\n", deque_peek_front(&mainDeque));
    } else {
        printf("The deque is empty.\n");

    }

    printf("The popped value of the first node is %i\n", deque_pop_front(&mainDeque));

    if (deque_is_empty(&mainDeque) == false) {
        printf("The value of the first node is %i\n", deque_peek_front(&mainDeque));
    } else {
        printf("The deque is empty.\n");

    }


    // Test deque operations - back operations
    if (deque_is_empty(&mainDeque) == false) {
        printf("The value of the last node is %i\n", deque_peek_back(&mainDeque));
    } else {
        printf("The deque is empty.\n");

    }

    deque_push_back(&mainDeque, 5);
    deque_push_back(&mainDeque, 10);

    if (deque_is_empty(&mainDeque) == false) {
        printf("The value of the last node is %i\n", deque_peek_back(&mainDeque));
    } else {
        printf("The deque is empty.\n");

    }

    printf("The popped value of the last node is %i\n", deque_pop_back(&mainDeque));

    if (deque_is_empty(&mainDeque) == false) {
        printf("The value of the last node is %i\n", deque_peek_back(&mainDeque));
    } else {
        printf("The deque is empty.\n");

    }

    printf("The popped value of the last node is %i\n", deque_pop_back(&mainDeque));

    if (deque_is_empty(&mainDeque) == false) {
        printf("The value of the last node is %i\n", deque_peek_back(&mainDeque));
    } else {
        printf("The deque is empty.\n");

    }



    return 0;

}


// -- Function declarations --

/* Push the new node to the front of the deque. Allocates memory for the new node onto the heap.
 * RETURN: (void) none
 */
void deque_push_front(Deque *deque, int data) {
    // Declare and allocate the new node
    Node* n = malloc(sizeof(Node));
    assert(n != NULL);

    n -> data = data;

    // Check if the new node is the first one in the deque
    if (deque -> front_node == NULL) {
        deque -> front_node = n; //move the deque front pointer to the new node
        deque -> back_node = n; //move the deque front pointer to the new node

        n -> previous_node = NULL; //set the prev. node pointer of the new node to NULL
        n -> next_node = NULL; //set the next node pointer of the new node to NULL

    } else {
        Node* prev_n = deque -> front_node; //take the address of the prev. node
        prev_n -> next_node = n; //link the new node the prev. node

        n -> previous_node = prev_n; //link the prev. node to the new node
        n -> next_node = NULL; //set the next node pointer of the new node to NULL

        deque -> front_node = n; //move the deque front pointer to the new node

    }


}

/* Pop the node from the front of the deque. Frees the memory of the front node From the heap.
 * RETURN: (int32_t) node value/data
 */
int32_t deque_pop_front(Deque *deque) {
    // Assert that the deque is not empty
    assert(deque -> front_node != NULL);

    // Init a new pointer for the front node
    Node* n0 = deque -> front_node;


    // Manage node behaviour and pointers
    if (n0 -> previous_node == NULL) { //the node is the last node
        n0 -> next_node = NULL; //no dangling pointers

        // Retrieve the value of the front node (n0)
        int32_t ret_value = n0 -> data;

        // Free the front node
        free(n0);

        // Set the deque pointers to NULL
        deque -> front_node = NULL; //no more nodes
        deque -> back_node = NULL; //no more nodes

        // Return the output value
        return ret_value;

    } else { //the node is not the last node
        // Init a new pointer for the new front node
        Node* n1 = n0 -> previous_node;

        // Retrieve the value of the front node (n0)
        int32_t ret_value = n0 -> data;

        // Free the front node
        free(n0);

        // Manage the pointer of the next node (n1)
        n1 -> next_node = NULL; //no dangling pointers

        // Move the front node pointer
        deque -> front_node = n1;

        // Return the output value
        return ret_value;

    }

}

/* Reads the value/data from the front node of the deque. Does not free memory or modify the deque.
 * RETURN: (int32_t) node value/data
 */
int32_t deque_peek_front(const Deque *deque) {
    // Assert that the deque is not empty
    assert(deque -> front_node != NULL);

    // Init a new pointer for the front node
    Node* n0 = deque -> front_node;

    // Retrieve the value of the front node (n0)
    int32_t ret_value = n0 -> data;

    // Return the output value
    return ret_value;

}

/* Push the new node to the back of the deque. Allocates memory for the new node onto the heap.
 * RETURN: (void) none
 */
void deque_push_back(Deque *deque, int data) {
    // Allocate the new node onto the heap
    Node* n = malloc(sizeof(Node));
    assert(n != NULL);

    // Init the data field of the new node
    n -> data = data;

    // Check if the new node is the first one in the deque
    if (deque -> front_node == NULL) {
        deque -> front_node = n; //move the deque front pointer to the new node
        deque -> back_node = n; //move the deque back pointer to the new node

        n -> previous_node = NULL; //set the prev. node pointer of the new node to NULL
        n -> next_node = NULL; //set the next. node pointer of the new node to NULL

    } else {
        Node* next_n = deque -> back_node; //take the address of the next node
        next_n -> previous_node = n; //link the next node to the new node

        n -> next_node = next_n; //link the new node the next node
        n -> previous_node = NULL; //set the previous node to NULL as there is no previous node

        deque -> back_node = n; //move the deque back pointer to the new node

    }

}

/* Pop the node from the back of the deque. Frees the memory of the back node from the heap.
 * RETURN: (int32_t) node value/data
 */
int32_t deque_pop_back(Deque *deque) {
    // Check if the deque is empty
    assert(deque -> back_node != NULL);

    // Init a pointer to the back node (nn)
    Node* n0 = deque -> back_node;

    // Manage node behaviour and pointers
    if (n0 -> next_node == NULL) { //last node on the deque
        n0 -> previous_node = NULL; //no dangling pointers

        // Retrieve the data stored in the node
        int32_t ret_value = n0 -> data;

        // Free the node memory
        free(n0);

        // Reset the front and back node pointers of the deque
        deque -> front_node = NULL;
        deque -> back_node = NULL;

        // Return the retrieved node data/valie
        return ret_value;

    } else { //not the last node on the deque
        // Init the pointer to the n-1 node
        Node* n1 = n0 -> next_node;

        // Retrieve the data stored in the node
        int32_t ret_value = n0 -> data;

        // Free the node memory
        free(n0);

        // Set the new back node's prev. node pointer to NULL
        n1 -> previous_node = NULL;

        // Move the back pointer
        deque -> back_node = n1; //no dangling pointers

        // Return the output value
        return ret_value;

    }

}

/* Reads the value/data from the back node of the deque. Does not free memory or modify the deque.
 * RETURN: (int32_t) node value/data
 */
int32_t deque_peek_back(const Deque *deque) {
    // Check if the deque is empty
    assert(deque -> front_node != NULL);

    // Init a pointer var to the last node
    Node* n0 = deque -> back_node;

    // Retrieve the data/value stored in the node
    int32_t ret_val = n0 -> data;

    // Return the node data/value
    return ret_val;

}


/* Checks if the deque is empty and return true if it is and false if it is not.
 * RETURN: (bool) true/false
 */
bool deque_is_empty(const Deque *deque) {
    return deque -> front_node == NULL ? true : false;

}
