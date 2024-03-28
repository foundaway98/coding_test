function solution(n) {
    let direction = ["r", "d", "l", "u"]
    let answer = []
    for(let i = 0; i<n;i++){
        let tmp = []
        for (let j = 0; j<n; j++){
            tmp.push(0)
        }
        answer.push(tmp)
    }
    let dirIdx = 0
    let i1 = 0
    let i2 = 0
    let cnt = n
    for (let num = 1; num <= n*n;){
        if (direction[dirIdx] == "r"){
            if(cnt != n){
                i2 += 1
            }
            for(let i = 0; i<cnt; i++){
                answer[i1][i2++] = num++;
            }
            cnt -= 1
            i2 -= 1
            dirIdx = 1
        } else if (direction[dirIdx] == "d"){
            i1 += 1
            for(let i = 0; i<cnt;i++){
                answer[i1++][i2] = num++;
            }
            i1 -= 1
            dirIdx = 2
        } else if (direction[dirIdx] == "l"){
            i2 -= 1
            for(let i=0;i<cnt;i++){
                answer[i1][i2--] = num++;
            }
            i2 += 1
            dirIdx = 3
            cnt -=1
        } else if (direction[dirIdx] == "u"){
            i1 -= 1
            for(let i = 0; i<cnt; i++){
                answer[i1--][i2] = num++;
            }
            i1 += 1
            dirIdx = 0
        }
    }
    
    return answer;
}