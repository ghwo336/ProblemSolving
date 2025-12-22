#include<bits/stdc++.h>
using namespace std;


void sol(){
    int a,b,c;
    cin>>a>>b>>c;
    int d = gcd(a,b);
    if (a<c and b<c) cout<<"NO"<<'\n';
    else if (c%d==0){
        cout<<"YES"<<'\n';
    }
    else cout<<"NO"<<'\n';
    
}

int main() {
    int t;
    cin>>t;
    for (int i = 0 ; i <t; i ++){
        sol();
    }
    return 0;
}