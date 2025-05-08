fs=require("fs");
input=fs.readFileSync('/dev/stdin').toString().trim().split('\n')
n=input.length
for (let i=0;i<n-1;i++){
    let [a,b]=input[i].split(' ');
    console.log(`${Math.floor(a/b)} ${a%b} / ${b}`)
}