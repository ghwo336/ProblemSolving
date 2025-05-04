const fs = require("fs")
const input=fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const n =input[0]
const li=input[1].split(" ")
const li2=input[2].split(" ")
for (let i=0;i<n;i++){
    let on =false;
    for (let j=0;j<n-1;j++){
        if (li[i]===li2[j]){
            on=true;
        }
    }
    if (!on){
        console.log(li[i]);
    }
}
