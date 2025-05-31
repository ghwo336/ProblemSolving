fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().split("\n");
let n =Number(input[0]);
for (let i = 1 ; i<= n ; i++){
    let li = input[i].split(" ").map(Number);
    let r=li[0];
    let e=li[1];
    let c =li[2];
    if (r+c<e) console.log("advertise");
    else if (r+c==e) console.log("does not matter");
    else console.log("do not advertise")
 
}