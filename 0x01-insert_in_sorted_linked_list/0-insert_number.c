#include "lists.h"

/**
 * *insert_node - Function to insert a number in sorted linked list
 * @head:   the sorted linked list
 * @number: the number to be insert
 * Return:  the new linked list with the insert
 */


listint_t *insert_node(listint_t **head, int number)
{
    listint_t *current;
    listint_t *temp;

    if (head == NULL)
        return (NULL);
        
    temp = malloc(sizeof(listint_t));
    current = *head;

    while (current->next != NULL && current->next->n < number)
    {
        current = current->next;
    }
    temp->n = number;
    temp->next = current->next;
    current->next = temp;

    return(temp);
}