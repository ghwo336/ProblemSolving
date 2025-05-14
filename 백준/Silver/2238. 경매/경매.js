fs=require("fs");
input= fs.readFileSync("/dev/stdin").toString().trim().split('\n');
let [u,n] = input[0].split(' ').map(Number);
let num= new Array(u+1).fill(0);
let names = new Array(u+1).fill('');
for (let i =1; i<=n;i++){
    let [name,price]=input[i].split(' ');
    price=Number(price);
    num[price]=num[price]+1;
    if (names[price]=='')names[price]=name;
}



for (let i =0 ; i<=u;i++){
    if (num[i]==0){
        num[i]=10000000
    }
}
let min = Math.min(...num);


for (let i =1 ; i<=u;i++){
    if (num[i]==min){
        console.log(names[i],i);
        break;
    }
}
