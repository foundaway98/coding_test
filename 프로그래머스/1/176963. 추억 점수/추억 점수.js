function solution(name, yearning, photo) {
    let answer = [];
    const nameTable = {};
    for(let i = 0; i < name.length; i++){
        nameTable[name[i]] = yearning[i]
    }
    for(p of photo){
        let pointSum = 0
        for(person of p){
            if(nameTable[person]){
                pointSum += nameTable[person]
            }
        }
        answer.push(pointSum)
    }
    return answer;
}