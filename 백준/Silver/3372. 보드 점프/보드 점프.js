fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let n = Number(input[0]);
let graph=[];
let dp=new Array();

for (let i =1 ; i<=n; i++){
    let li = input[i].split(' ').map(Number);
    let li2= new Array(n).fill(0n);
    dp.push(li2);
    graph.push(li);
}

dp[0][0]=1n

let sol=(i,j)=>{
    for (let y =0; y<i; y++ ){
        if(graph[y][j]+y==i){
            dp[i][j]+=dp[y][j];
        }
    }
    for (let x=0;x<j;x++){
        if(graph[i][x]+x==j){
            dp[i][j]+=dp[i][x];
        }
    }
}


for(let i =0; i<n;i++){
    for(let j =0; j<n;j++){
        
        sol(i,j);
    }
}

console.log(dp[n-1][n-1].toString())
