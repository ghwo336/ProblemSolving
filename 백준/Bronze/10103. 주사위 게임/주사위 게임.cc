#include <iostream>
using namespace std;

int first=100;
int second=100;

void sol(){
    int a,b;
    cin>>a>>b;
    if (a<b) first-=b;
    if (a>b) second-=a;
    
}


int main() {
    int t;
    cin>>t;
    for (int i =0; i<t; i++){
        sol();
    }
    cout<<first<<'\n'<<second;
}