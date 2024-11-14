#include <iostream>
#include <string>
using namespace std;
int main() {
    while(true){
        int a;
        cin>>a;
        if(a==0)break;
        for(int i =1 ; i<=a; i++){
            string k(i,'*');
            cout<<k<<'\n';
    }
}
}