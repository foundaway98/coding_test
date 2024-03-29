function solution(common) {
    
    if(common[common.length - 1] - common[common.length -2] === common[common.length-2] - common[common.length - 3]){
        return common[common.length-1] + common[common.length - 1] - common[common.length -2]
    } else {
        return common[common.length-1] * (common[common.length - 1] / common[common.length -2])
    }
}