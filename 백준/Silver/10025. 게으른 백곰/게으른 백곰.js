fs=require("fs");
input=fs.readFileSync("/dev/stdin").toString().trim().split('\n');
let [n,k]=input[0].split(' ').map(Number);
let st = []
for (let i=1; i<=n;i++){
    let li=input[i].split(" ").map(Number);
    st.push(li)
}
st.sort((a,b)=>(a[1]-b[1]));
let li = new Array(1000001).fill(0);

for (let i = 0; i<n ; i++){
    li[st[i][1]]=st[i][0]
}

for (let i =1; i<=1000000; i++){
    li[i]+=li[i-1]
}

//li는 누적합

let dap = 0;
if(k>=500000){
    k=500000
    for (let i =0 ; i<n; i++){
        dap+=st[i][0];
    }
}
else{
    for (let i =2*k+1; i<=1000000; i++){
    dap=Math.max(dap,li[i]-li[i-2*k-1]);
}
}


console.log(dap)