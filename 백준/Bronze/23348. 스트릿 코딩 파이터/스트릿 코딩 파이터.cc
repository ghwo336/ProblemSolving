#include <iostream>
using namespace std;

int max(int a, int b){
    if (a>b) return a;
    return b;
}

int main() {
    int A,B,C;
    cin>>A>>B>>C;
    int N;
    int dap=0;
    cin>>N;
    for(int j=0; j<N;j++){
        int hubo=0;
        for(int i =0;i<3;i++){
            int a,b,c;
            cin>>a>>b>>c;
            hubo+=(A*a+B*b+c*C);
        }
        dap=max(dap,hubo);
    }
    

    cout<<dap;
    return 0;
}