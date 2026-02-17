#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct _node{
    char elem;
    struct _node *next;
}Node;
typedef struct _stack{
    Node *head;
}Stack;
void initStack(Stack *pstack){
    pstack->head = NULL;
    return;
}
int isEmpty(Stack *pstack){
    if(pstack->head == NULL)
        return 1;
    return 0;
}
Node *makeNode(char elem){
    Node *newNode = (Node *)calloc(1,sizeof(Node));
    if(newNode == NULL){
        printf("Not enough memory");
        return NULL;
    }
    newNode->elem = elem;
    return newNode;
}
void push(Stack *pstack, char elem){
    Node *newNode = makeNode(elem);
    newNode->next = pstack->head;
    pstack->head = newNode;
    return;
}
char pop(Stack *pstack){
    if(isEmpty(pstack)){
        printf("EmptyStackException");
        return '0';
    }
    Node *pdelete = pstack->head;
    char ret = pdelete->elem;
    pstack->head=  pstack->head->next;
    free(pdelete);
    pdelete = NULL;
    return ret;
    
}
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
bool solution(const char* s) {
    Stack stack;
    initStack(&stack);
    bool answer = true;
    for(int i = 0; s[i] != '\0'; i++){
        char elem = s[i];
        if(s[i] == '('){
            push(&stack, elem);
            
        }
        else{
            char e = pop(&stack);
            if(e == '0')
            {
                answer = false;
                return answer;
            }
            
        }
                
    }
    if(!isEmpty(&stack)){
        answer = false;
    }
    return answer;
}