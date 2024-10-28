#include <iostream>
using namespace std;

void sol(){
    int dap=0;
    string s;
    cin>>s;
    for (char a:s){
        if (a=='D') {cout<<dap<<'\n'; return;}
        dap++;
    }
    cout<<dap<<'\n';
    
}


int main() {
    int N;
    cin>>N;
    for (int i = 0 ; i < N ; i++){
        sol();
    }
    return 0;
}

