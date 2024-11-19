#include <iostream>
#include <string>
using namespace std;
int main() {
    int n;
    cin>>n;
    string v(n/5,'V');
    string i(n%5,'I');
    cout<<v<<i;
    
    return 0;
}