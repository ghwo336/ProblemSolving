#include <iostream>
using namespace std;
int main() {
    long long n;
    cin >>n;
    long long a,pa,b,pb;
    cin >>a>>pa>>b>>pb;
    long long attacker=0;
    long long tanker = 0;
    long long dap = 0;
    for (long long i = 0 ; i <= n/pa ; i++){
        long long defender = (n-pa*i)/pb;
        long long combatpower = a*i+ b * defender;
        if (dap<combatpower) {
            attacker=i;
            dap=combatpower;
            tanker=defender;
        }
    }
     
    cout<<attacker<<' '<<tanker;
    return 0;
}