fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().trim().split('\n');
let [king,stone,n]=input[0].split(' ');
n=Number(n);
//king좌표 파싱(x,y)
king=king.split('');
king[1]=Number(king[1])
king[0]=king[0].charCodeAt(0)-65;

//stone 좌표 파싱
stone=stone.split('');
stone[1]=Number(stone[1])
stone[0]=stone[0].charCodeAt(0)-65;

//이동 (dx,dy)
move={
    'R':[1,0],
    'L':[-1,0],
    'B':[0,-1],
    'T':[0,1],
    'RT':[1,1],
    'LT':[-1,1],
    'RB':[1,-1],
    'LB':[-1,-1]
}
const go=(s)=>{
    let moving = move[s];
    let kingx=king[0]+moving[0];
    let kingy=king[1]+moving[1];
    //애초에 킹이 못 가면 걍 리턴 해버리기~
    if (kingx>=8 || kingx<0||kingy>8||kingy<=0) return;
    //만약 겹치면
    if (kingx==stone[0]&& kingy==stone[1]){
        let stonex=stone[0]+moving[0];
        let stoney=stone[1]+moving[1];
        //안되면 걍 리턴 해버리기~
        if (stonex>=8 || stonex<0||stoney>8||stoney<=0) return;
        //되니까 움직이시자
        stone[0]=stonex;
        stone[1]=stoney;
        king[0]=kingx;
        king[1]=kingy;
        return;
    }
    //안겹치면 king 만 이동
    king[0]=kingx;
    king[1]=kingy;
    return;
}


for (let i = 1; i <=n; i++){
    go(input[i])
}


let kx= String.fromCharCode(king[0] + 65)
let sx =String.fromCharCode(stone[0] + 65)
console.log(kx+king[1]);
console.log(sx+stone[1]);

