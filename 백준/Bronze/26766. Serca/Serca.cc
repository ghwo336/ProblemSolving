#include <iostream>
using namespace std;




void sol() {
    cout<<" @@@   @@@"<<'\n'<<"@   @ @   @"<<'\n'<<"@    @    @"<<'\n'<<"@         @"<<'\n'<<" @       @ "<<'\n'<<"  @     @  "<<'\n'<<"   @   @   "<<'\n'<<"    @ @    "<<'\n'<<"     @     ";
}





int main() {
    int n;
    cin>>n;
    for(int i=0; i<n;i++){
        sol();
        if (i!=n-1){
            cout<<'\n';
        }
    }
    return 0;
}