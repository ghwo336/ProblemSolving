fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().trim().split(`\n`);
let graph= Array.from({length:100001},()=>[]);
let jinip = new Array(100001).fill(0);

let len=input.length;

if(input[0]!=''){
for (let i =0 ; i<len; i++){
    let [start,end,value]=input[i].split(' ').map(Number);
    jinip[start]+=1;
    jinip[end]+=1;
    graph[start].push([end,value]);
    graph[end].push([start,value]);
}
// 가장 부모노드와 가장 자식노드 (문제 조건이 트리임)
let hubo = [];
for (let i = 0 ; i<=100001;i++){
    if (jinip[i]==1) hubo.push(i);
}
let start = hubo[0];
let dap=0;


let storage = new Array(100001).fill(0);
for (let i of hubo){
    storage.fill(0);
    storage[i]=-1;
    const dfs = (now,value)=>{
    for (let [next,cost] of graph[now]){
        if (storage[next]==0){
            storage[next]=value+cost;
            dfs(next,value+cost)
            }
        }
    }
    dfs(i,0);
    dap=Math.max(dap,Math.max(...storage));
}
console.log(dap)}
else console.log(0)

