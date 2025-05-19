fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().trim().split(`\n`);
let [n,m]= input[0].split(" ").map(Number);
let visit=new Array(n).fill(false);
let songs=new Array(m).fill(0);
let p = new Array(m+1).fill(100);

let guiters = new Array();
for (let i =1 ; i<=n; i++){
    let[guiter,possible]=input[i].split(" ");
    guiters.push(possible);
}



backTracking=(num)=>{
    // n개 되면 리턴 이걸 쓴 순간 이 함수 내에서 방문 후 처리 로직을 짜야함
    if (num==n) return;
    for (let i = 0 ; i < n ; i ++){
        if (!visit[i]){
            visit[i]=true;
            for (let j = 0 ; j <m ; j++){
                if (guiters[i][j]=="Y"){
                    songs[j]+=1;
                }   
            }
            let fiv = 0;
            for (let j = 0 ; j<m ; j++){
                if (songs[j]!=0) fiv=fiv+1;
            }
            p[fiv]=Math.min(p[fiv],num+1);
            backTracking(num+1);
            visit[i]=false;
            for (let j = 0 ; j <m; j++){
                if (guiters[i][j]=="Y") songs[j]-=1;
            }
        }
    } 
}

backTracking(0);

for (let  i =m ; i>0;i--){
    if (p[i]!=100) {
        console.log(p[i])
        break;
    }
    if (i==1) console.log(-1);
}
