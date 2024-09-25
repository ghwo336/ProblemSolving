#include <iostream>
using namespace std;
int dap=10000;

void sol(){
    int a,b;
    cin>>a>>b;
    if (a<=b){
        dap=min(dap,b);
    }
}



int main() {
    int N;
    cin>>N;
    for (int i=0;i<N;i++){
        sol();
    }
    if (dap<1011)
        cout<<dap;
    else
    cout<<-1;
}