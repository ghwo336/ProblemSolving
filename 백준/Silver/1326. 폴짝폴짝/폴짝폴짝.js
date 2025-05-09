fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let n=Number(input[0])
let li=[0,...input[1].split(' ').map(Number)]
let [start,end]=input[2].split(' ').map(Number)

let dp = new Array(n+1).fill(100000);

dp[start]=0
let dfs=(now,num)=>{
    for (let i =1; now+i*li[now]<=n ||now-i*li[now]>0;i++){
        let next=now+i*li[now];
        if (next<=n){
            if (dp[next]>num+1){
                dp[next]=num+1;
                dfs(next,num+1);
        }
        }

        let next2=now-i*li[now];
        if (next2>0){
            if (dp[next2]>num+1){
            dp[next2]=num+1;
            dfs(next2,num+1);
        }
        }
    }
}
dfs(start,0)
if (dp[end]==100000){
    console.log(-1)
}
else{
    console.log(dp[end])
}