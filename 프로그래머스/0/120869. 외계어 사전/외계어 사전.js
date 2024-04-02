function solution(spell, dic) {
    var answer = 0;
    let cnt = 0
    for(let word of dic){
        let wordFlag = true
        for(let s of spell){
            if(!word.includes(s)){
                wordFlag = false
                break
            }
        }
        if(wordFlag){
            cnt++
            break
        } else {
            wordFlag = true
        }
    }
    if(cnt === 1){
        return cnt
    } else {
        return 2
    }
}