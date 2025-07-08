#include <iostream>
#include <string>
using namespace std;
int main() {
    string s;
    cin>>s;
    for (char c:s){
        if ((int)c>=97){
            cout<<char((int)c-32);
        }
        else{
            cout<<char((int)c+32);
        }
            
    }
    
    return 0;
}