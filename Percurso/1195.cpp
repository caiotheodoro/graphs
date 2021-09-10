#include <iostream>

using namespace std;

typedef struct no
{
    int dado;
    struct no* esq;
    struct no* dir;

}No;


No* insere(No* n1, int dado)
{
    if (n1 == NULL)
    {
        n1 = (No*) malloc(sizeof(No));
        n1->dado = dado;
        n1->esq = NULL;
        n1->dir = NULL;
    }
    else if (n1->dado > dado)
        n1->esq = insere(n1->esq, dado);
    else if (n1->dado < dado)
        n1->dir = insere(n1->dir, dado);
    return n1;
}


 int tamTree(No* n1)
{
    if (n1 == NULL)
        return 0;
    else
    {
        int ltamTree = tamTree(n1->esq);
        int rtamTree = tamTree(n1->dir);
 
        if (ltamTree > rtamTree)
        {
          return(ltamTree + 1);
        }
        else {
          return(rtamTree + 1);
        }
    }
}
void printNivel(No* n1, int level)
{
    if (n1 == NULL)
        return;
    if (level == 1)
        cout << n1->dado << " ";
    else if (level > 1)
    {
        printNivel(n1->esq, level-1);
        printNivel(n1->dir, level-1);
    }
}

void printPosfixo(No* n1)
{
    if (n1 == NULL)
        return;
 
    printPosfixo(n1->esq);
    printPosfixo(n1->dir);
    cout << n1->dado << " ";
}
 
void printInfixo(No* n1)
{
    if (n1 == NULL)
        return;

    printInfixo(n1->esq);
    cout << n1->dado << " ";
    printInfixo(n1->dir);
}
 
void printPrefixo(No* n1)
{
    if (n1 == NULL)
        return;

    cout << n1->dado << " ";
    printPrefixo(n1->esq);
    printPrefixo(n1->dir);
}

void printTam(No* n1)
{
    int h = tamTree(n1);
    int i;
    for (i = 1; i <= h; i++)
        printNivel(n1, i);
}
 

No* libera(No *h1)
{
    if (h1){
    h1->esq = libera(h1->esq);
    h1->dir = libera(h1->dir);
    free(h1);
    };

    return NULL;
}

int main()
{
    int loops,n, x,caso = 1;
    No *h = NULL;
    cin >> loops;
    while(loops--)
    {
        cin >> n;
        for (int i = 0 ; i < n ; i++)
        {
            cin >> x;
            h = insere(h, x);
            if(i == n-1) cout<<"\n";
        }
  
        cout <<"Case "<< to_string(caso)<<":" << endl;
        caso++;
      cout << "Pre.:";
      printPrefixo(h);
      cout << "\n";
      cout << "In..:";
      printInfixo(h);
      cout << "\n";
      cout << "Post:";
      printPosfixo(h);

        h = libera(h);

    }    
  cout << "\n";
}