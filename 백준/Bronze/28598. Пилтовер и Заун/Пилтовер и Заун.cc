#include <iostream>
using namespace std;
int main() {
    int a,b,c;
    cin>>a>>b>>c;
    if ((a-b)%(2)==0 and((a-b)/2)>=c){
        cout<<"YES";
    } else{
        cout<<"NO";
    }
}