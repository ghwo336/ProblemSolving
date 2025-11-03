#include <iostream>
using namespace std;
int main() {
    int n,m;
    cin>>n>>m;
    int base = m/n;
    if (base%2==1) cout << n-m%n;
    else cout <<m%n;
    return 0;
}