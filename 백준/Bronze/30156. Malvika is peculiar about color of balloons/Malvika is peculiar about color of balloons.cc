#include <iostream>
#include <string>
using namespace std;


void sol(){
    int a=0;
    int b=0;
    string s;
    cin>>s;
    for (char c: s){
        if (c=='a')
            a+=1;
        else b+=1;
    }
    if (a>b) cout<<b<<'\n';
    else cout<<a<<'\n';
    
}

int main() {
    int N;
    cin>>N;
    for( int i = 0 ; i <N ; i++){
        sol();
    }
    return 0;
}