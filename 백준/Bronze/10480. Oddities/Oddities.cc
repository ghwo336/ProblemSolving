#include <iostream>
using namespace std;




void sol(){
    int N;
    cin>>N;
    if (N%2 ==0){
        cout<<N<<" is even"<<'\n';
        return;
    }
    cout<<N<<" is odd"<<'\n';
}




int main() {
    int T;
    cin>>T;
    for (int i =0 ; i <T ; i++){
        sol();
    }
    return 0;
}