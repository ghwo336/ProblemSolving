#include <iostream>
using namespace std;

int main() {
    cin.tie(0);
    ios_base :: sync_with_stdio(0);
    long long n;
    cin>>n;
    long long hap=n*(n-1)/2;
    long long sum=0;
    for (int i=0;i<n;i++){
        long long a;
        cin>>a;
        sum+=a;
    }
    cout<<sum-hap;





    return 0;
}