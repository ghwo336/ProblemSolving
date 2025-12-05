#include <iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    for (int i = 1 ; i<=3; i++){
        for (int j=1 ; j<=n;j++){
            cout<<j<<' ';
        }
    }
    return 0;
}