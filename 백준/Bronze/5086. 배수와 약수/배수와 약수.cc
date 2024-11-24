#include <iostream>
#include  <string>
#include <vector>
using namespace std;
int main() {
    while(true){
        int a,b;
        cin>>a>>b;
        if (a==0 and b==0){
            return 0;
        }   
        if (a%b ==0) cout<<"multiple"<<'\n';
        else if (b%a==0) cout <<"factor"<<'\n';
        else cout<<"neither"<<'\n';
    }
    
}