#include <iostream>
using namespace std;


void sol(){
    int g,p;
    cin>>g>>p;
    cout<<"Games: "<<g<<'\n';
    cout<<"Points: "<<p<<'\n';
    cout<<"Possible records:"<<'\n';
    int a = p/3;
    for (int i=a;i>=0;i--){
        int j = p-3*i;
        int k =g-i-j;
        if (j>=0 && k>=0 && 3*i+j==p)
            cout<<i<<'-'<<j<<'-'<<k<<'\n';       
    }
    cout<<'\n';
}


int main() {
    int n;
    cin>>n;
    for (int i =0; i<n;i++){
        cout<<"Team #"<<i+1<<'\n';
        sol();
    }
    
    return 0;
}