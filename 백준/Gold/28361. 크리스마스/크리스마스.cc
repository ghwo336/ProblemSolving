 #include <iostream>
#include <vector>
using namespace std;
int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    cin >> N;
    cout << N<<'\n';
    if (N%6!=5 && N%6!=2){
    cout<<1<<' '<< 3 <<' '<<2<<' ';
    int now = 2;
    int pandan = 0;
    while (true){
        if (pandan==2){
            now-=1;
            pandan=0;
            cout<<now<<' ';
        }
        else{
            pandan+=1;
            now+=2;
            if (now>N){
                cout<<1;
                return 0;
            }
            cout<<now<<' ';
            
        }
    }
    }
    else{
        cout<<1<<' '<< 2 <<' '<<4<<' '<<3<<' ';
        int now = 3;
        int pandan = 0;
        while (true){
            if (pandan==2){
                now-=1;
                pandan=0;
                cout<<now<<' ';
            }
            else{
                pandan+=1;
                now+=2;
                if (now>N){
                    cout<<1;
                    return 0;
                }
                cout<<now<<' ';
                
            }
    }

    }




    return 0;
}