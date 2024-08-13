#include <iostream>
using namespace std;

void solve(){
    int a,b;
    cin>>a>>b;
    if (a<b){
        cout<<"NO BRAINS\n";
    } else{
        cout<<"MMM BRAINS\n";
    }
}

int main() {
    int N;
    cin>>N;
    for (int i=0;i<N;i++){
        solve();
    }
}