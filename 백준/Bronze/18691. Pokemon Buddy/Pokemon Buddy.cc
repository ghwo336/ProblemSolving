#include <iostream>

using namespace std;

int max(int a , int b){
    if (a>b){
        return a;
    }
    return b;
}


int main() {
    int N;
    cin >> N;
    for ( int i =0 ; i < N ; i ++ ){
        int a,b,c;
        cin>>a>>b>>c;
        cout<<max(((2*a-1)*(c-b)),0)<<'\n';
    }
    return 0;
}