fs=require("fs")
input=fs.readFileSync("/dev/stdin").toString().split("\n");
let n = Number(input[0])
let [s1,s2]=input[1].split(' ').map(Number);
let dap = 0;
for (let i = 1; i<=n; i++){
    let [n1,n2] = input[i].split(' ').map(Number);
    dap=dap+(Math.abs(s1-n1)+Math.abs(s2-n2));
    s1=n1;
    s2=n2;
}
let [d1,d2]=input[1].split(' ').map(Number);
dap+=Math.abs(s1-d1)+Math.abs(s2-d2)

console.log(dap)