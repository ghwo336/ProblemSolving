#include <iostream>
using namespace std;


void sol(){
    int a,b;
    cin>>a>>b;
    if (a>=12 && b>=4){
        cout<<11*b+4<<'\n';
        return;
    }
    cout<<-1<<'\n';
    
}


int main() {
    int N;
    cin>>N;
    for ( int i=0; i<N; i++){
        sol();
    }
    return 0;
}