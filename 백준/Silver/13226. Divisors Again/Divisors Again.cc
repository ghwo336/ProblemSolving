#include <iostream>
using namespace std;

int box[10000001] ;


void sol(){
    int a, b;
    cin>>a>>b;
    int dap=-1;
    for (int i = a; i<=b ; i++){
        if(dap<box[i]) dap=box[i];
    }
    cout << dap <<'\n';
    
}



int main() {
    for (int i =1 ; i <10000001 ; i++){
        for (int j =1 ; i*j <10000001 ; j++){
            box[i*j]+=1;
        }
    }

    int T;
    cin>>T;
    for (int i = 0 ; i < T ; i++){
        sol();
    }
}