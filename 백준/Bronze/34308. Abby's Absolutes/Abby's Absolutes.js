const fs =require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
let [n,m]=input[0].split(' ').map(Number);
let li = input[1].split(' ').map(Number);
li=li.map(x=>{
    if (Math.abs(x-n)<Math.abs(x-1)){ return n;}
    else return 1;
})

console.log(li.join(' '))

