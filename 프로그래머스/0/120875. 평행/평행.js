/*
1,2 3,4
1,3 2,4
1,4 2,3
*/

function solution(dots) {
    var answer = 0;
    let possible = [
        [dots[0], dots[1], dots[2], dots[3]],
        [dots[0], dots[2], dots[1], dots[3]],
        [dots[0], dots[3], dots[1], dots[2]]
    ]
    for(let ps of possible){
        let x1 = ps[0][0] - ps[1][0]
        let y1 = ps[0][1] - ps[1][1]
        let x2 = ps[2][0] - ps[3][0]
        let y2 = ps[2][1] - ps[3][1]
        if(x1/y1 == x2/y2){
            answer = 1
            break
        }
    }
    return answer
}