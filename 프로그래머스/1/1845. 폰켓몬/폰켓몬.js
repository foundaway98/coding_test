function solution(nums) {
    let monsters = {}
    for(let monster of nums){
        if(!monsters[monster]){
            monsters[monster] = 1
        } else {
            monsters[monster] += 1
        }
    }
    if(Object.keys(monsters).length < nums.length/2){
        return Object.keys(monsters).length
    } else {
        return nums.length / 2
    }
}