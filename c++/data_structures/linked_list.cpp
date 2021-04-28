#include <cstdlib>
#include <cstdio>
#include <iostream>

struct Node 
{
    int item;
    Node *next;
};

typedef Node* nodePtr;
void insert(nodePtr& head, int data)
{
    nodePtr tempPtr;
    tempPtr = new Node;
    tempPtr->item = data;
    tempPtr->next = head;
    head = tempPtr;

}
int main()
{
    nodePtr head;
    head = new Node;
    head->item = 20;
    head->next = NULL;

    insert(head, 30);
    insert(head, 40);

    nodePtr temp;
    temp = head;

    while (temp != NULL)
    {
        std::cout << temp->item << std::endl;
        temp = temp->next;
    }
}