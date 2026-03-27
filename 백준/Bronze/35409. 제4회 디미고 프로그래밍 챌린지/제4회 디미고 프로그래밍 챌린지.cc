#include <iostream>
using namespace std;

int main() {
    int H, M;
    cin >> H >> M;
    int t=H*60+M;
    if (t >= 6*60+30 && t <= 9*60+0) cout<<"Yes";
    else if (t >= 9*60+50 && t <= 10*60+0) cout<<"Yes";
    else if (t >= 10*60+50 && t <= 11*60+0) cout<<"Yes";
    else if (t >= 11*60+50 && t <= 12*60+0) cout<<"Yes";
    else if (t >= 12*60+50 && t <= 13*60+50) cout<<"Yes";
    else if (t >= 14*60+40 && t <= 14*60+50) cout<<"Yes";
    else if (t >= 15*60+40 && t <= 15*60+50) cout<<"Yes";
    else if (t >= 16*60+40 && t <= 22*60+50) cout<<"Yes";
    else cout<<"No";
    
}