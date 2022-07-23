#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
/*
    Código em C para a implementação de linked lists
    Estruturas de Dados - UFS 
    Pedro Vinícius de Araújo Barreto
*/

typedef struct element element;

struct element{
    // Nome da pessoa na rede social
    const char* nome;
    // Ponteiro para o próximo element
    element *P;
};

// Por ser lista cíclica, será interessante ter função para identificar o ultimo elemento atual da lista:

element last(element* cabeca_lista){
    element temp = *cabeca_lista;
    do {
        temp = *(temp.P);
    } while (temp.P != cabeca_lista);
    return temp;
}

// TODO: Função para verificar se um nome já está presente na lista linkada


// Função para adicionar uma nova pessoa na lista, inclusive no meio dela
// lista atual refere ao elemento ao qual vc quer posicionar o novo elemento imediatamente a direita dele
void add_elem(element *elem_atual, char *nome_novo){
    // Alocamos espaço pra um novo elemento
    element *nova_pessoa = (element *)malloc(sizeof(element));
    // Primeiro colocamos o nome desse elemento como o nome passado como argumento
    // Depois, essa nova pessoa (p2) irá apontar (dar as mãos) para a pessoa (p3) a qual o elem/pessoa atual (p1) estava apontando
    // p1 -> p3    queremos adicionar p2 após p1:
    // p2 -> p3
    // p1 -> p2 
    // p1 -> p2 -> p3     feito  
    nova_pessoa->nome = nome_novo;
    nova_pessoa->P = elem_atual->P;
    elem_atual->P = nova_pessoa;
}

// Aqui, elem_inicial representa o elemento em que a iteração irá começar. Não precisa ser o primeiro elemento da lista
// Assume-se que o nome da pessoa removida está presente na lista ligada
void remove_elem(element *elem_inicial, char *nome_pessoa_removida){
    element* temp = elem_inicial;
    element* predecessor;
    do
    {
        predecessor = temp;
        temp = temp->P;
    } while (temp->nome != nome_pessoa_removida);
    // Armazenamos o endereço do sucessor de temp
    element *sucessor = temp->P;
    // Desalocamos/removemos o elemento de predecessor e apontamos para um novo, sucessor.
    free(predecessor->P);
    predecessor->P = sucessor;
}

int main(void){
    element primeiro = {"Pedro", &primeiro};
    add_elem(&primeiro, "Carlos");
    printf("%p\n%p\n", (primeiro.P)->P, &primeiro);
    printf("%s\n", primeiro.P->nome);
    printf("%s\n", last(&primeiro).nome );
    remove_elem(primeiro.P, "Carlos");
    printf("%s\n", last(&primeiro).nome );
    return 0;
}