fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let[t,n,m]=input[0].split(' ').map(Number);
let graph=[]
let dp=[]
let move=[[1,0],[-1,0],[0,1],[0,-1]]

for (let i =1 ; i<=n;i++){
    let li2=new Array(m).fill(500);
    dp.push(li2);
}

// graph 만들기
for  (let i =1; i<=n; i++){
    graph.push(input[i].split(''))
}

let start=[0,0];
//시작점 찾기
for (let i =0; i<n; i++){
    for (let j = 0; j <m; j++){
        if(graph[i][j]=='S'){
            start=[i,j];
        }
    }
}

//1억
let dap=100000000

 const dfs = (nowy,nowx,num) =>{
     
     if (dp[nowy][nowx]<=num) return;
     else dp[nowy][nowx]=num;
     let nextNum=num+1;
     // 4방향 움직이기
     for (let i =0 ; i <4 ; i++){
         let nexty=nowy+move[i][0];
         let nextx=nowx+move[i][1];
         // 움직인 곳이 떨어진곳이면 답 갱신후 리턴
         if (nexty<0 || nexty>=n ){
             return;
         }
    
         if (nextx<0 || nextx>=m ){
             return;
         }

         //방향 키 나왔을 때
         if (graph[nexty][nextx]=='U'){
             if (move[i][0]==1){
                 dfs(nexty,nextx,nextNum);
             }
         }


         if (graph[nexty][nextx]=='D'){
             if (move[i][0]==-1){
                 dfs(nexty,nextx,nextNum);
             }
         }



         if (graph[nexty][nextx]=='L'){
             if (move[i][1]==1){
                 dfs(nexty,nextx,nextNum);
             }
         }

         if (graph[nexty][nextx]=='R'){
             if (move[i][1]==-1){
                 dfs(nexty,nextx,nextNum);
             }
         }

         //그냥 0 일때
         if (graph[nexty][nextx]=='0'){
             dfs(nexty,nextx,nextNum);
         }

         
     }
     
 }

dfs(start[0],start[1],0)

for (let i = 0; i<n; i++){
    for (let j =0; j<m;j++){
        if (i==0 || i==n-1 || j==0 || j==m-1){
            dap=Math.min(dap,dp[i][j])
        }
    }
}
if (dap>t) console.log("NOT POSSIBLE");
else console.log(dap);

