fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let [n,m]=input[0].split(" ").map(Number);
let graph=[]
for (let i =1 ; i<=n ; i++){
    let li=input[i].split('');
    graph.push(li);
}

let dap = 2501;
const sol=(startx,starty)=>{
    let startWhite = 0;
    let startBlack = 0;
    //시작이 W일때
    for (let i=0;i<8;i++){
        for (let j=0;j<8;j++){
            if((i+j)%2==0){
                if (graph[starty+j][startx+i]=="B") startWhite++;
                if (graph[starty+j][startx+i]=="W") startBlack++;
            }
            else{
                if (graph[starty+j][startx+i]=="B") startBlack++;
                if (graph[starty+j][startx+i]=="W") startWhite++;
            }
        }
    }
    dap=Math.min(dap,startWhite);
    dap=Math.min(dap,startBlack);
}



for (let startx=0; startx+8<=m;startx++){
    for (let starty=0;starty+8<=n;starty++){
        sol(startx,starty);
    }
}


console.log(dap);