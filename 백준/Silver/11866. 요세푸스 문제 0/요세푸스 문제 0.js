class Queue {
    constructor(){
        this.q=[];
        this.head=0;
    }
    push(value){
        this.q.push(value);
    }
    popleft(){
        if(this.isEmpty())  return undefined;
        return this.q[this.head++];
    }
    isEmpty(){
        return this.size()===0;
    }
    size(){
        return this.q.length-this.head;
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');
const n =Number(input[0])
const k =Number(input[1])

const q = new Queue();
for (let i =1; i<=n; i++){
    q.push(i);
}
const li= [];

for (let i =1; i<=n; i++){
    let num = k;
    while (num>0){
        let p=q.popleft();
        num--;
        if (num==0){
            li.push(p)
            break;
        }
        q.push(p);
    }
}

console.log(`<${li.join(', ')}>`)

