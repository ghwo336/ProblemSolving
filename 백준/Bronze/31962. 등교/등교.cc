#include <iostream>
using namespace std;
int num=0;

int max( int x, int y){
    if (x>y) return x;
    return y;
}


void sol(int timelimit){
    int x,y;
    cin>>x>>y;
    if (x+y<=timelimit){
        num=max(num,x);
    }
    
}



int main() {
    int N,X;
    cin>>N>>X;
    for (int i =0 ; i < N ; i ++){
        sol(X);
    }
    if (num){
        cout<<num;
    } else cout<<-1;


    
    return 0;
}