#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>
#include <assert.h>


typedef struct node {

    int32_t data;
    struct node* previous_element;

} Node;

typedef struct stack {

    Node* stack_pointer;

} Stack;

/* Push a new node onto the stack. (The node is heap allocated and will be freed by pop) */
void stack_push(Stack* stack, int32_t data) {
    // Allocate the new node onto the heap
    Node* n = malloc(sizeof(Node));

    assert(n != NULL);

    // Initialize the new node with the appropriate data
    n -> data = data;
    n -> previous_element = stack -> stack_pointer; //if root, should be NULL

    // Update the stack pointer
    stack -> stack_pointer = n;

}

/* Pops the top node from the stack returning it's value and freeing it from the heap. If the stack is empty, it returns INT_MIN. */
int32_t stack_pop(Stack* stack) {
    // Check if the stack is empty
    assert( stack -> stack_pointer != NULL);

    // Assign the stored stack pointer into a node pointer
    Node* n = stack -> stack_pointer;

    // Pull the data and the previous_element's pointer from the node
    int32_t return_val = n -> data;
    Node* previous_e = n -> previous_element;

    // Free the node from the heap
    free(n);

    // Update the stack pointer
    stack -> stack_pointer = previous_e;

    // Return the value of the popped node
    return return_val;

}

/* Returns the value of top node found on the stack, or returns INT_MIN if the stack is empty (does not free the node memory). */
int32_t stack_peek(const Stack* stack) {
    // Check if the stack is empty
    assert(stack -> stack_pointer != NULL);

    // Assign the stored stack pointer into a node pointer
    Node* n = stack -> stack_pointer;

    // Assign the node value to the output var
    int32_t top_val = n -> data;

    // Return  the top node value
    return top_val;

}

/* Checks if the stack is empty, if yes returns a boolean false, otherwise a boolean true (does not free the node memory). */
bool stack_is_empty(const Stack* stack) {
    // Check if the stack is empty
    if (stack -> stack_pointer == NULL) {
        return true;
    } else {
        return false;
    }

}



int32_t main(void) {


    Stack mainStack = {
        .stack_pointer = NULL
    };


    if (stack_is_empty(&mainStack) == false) {
        printf("The value of the top node is %i\n", stack_peek(&mainStack));
    }

    stack_push(&mainStack, 5);
    stack_push(&mainStack, 10);

    if (stack_is_empty(&mainStack) == false) {
        printf("The value of the top node is %i\n", stack_peek(&mainStack));
    }

    printf("The popped value of the top node is %i\n", stack_pop(&mainStack));

    if (stack_is_empty(&mainStack) == false) {
        printf("The value of the top node is %i\n", stack_peek(&mainStack));
    }

    printf("The popped value of the top node is %i\n", stack_pop(&mainStack));

    if (stack_is_empty(&mainStack) == false) {
        printf("The value of the top node is %i\n", stack_peek(&mainStack));
    }


    return 0;

}
