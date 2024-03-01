function solution(cards1, cards2, goal) {
    
    cards1.reverse()
    cards2.reverse()
    goal.reverse()
    
    while(goal.length > 0){
        if(cards1[cards1.length -1] === goal[goal.length-1]){
            cards1.pop()
            goal.pop()
        } else if(cards2[cards2.length -1] === goal[goal.length-1]){
            cards2.pop()
            goal.pop()
        } else if (cards1[cards1.length -1] !== goal[goal.length-1] && cards2[cards2.length -1] !== goal[goal.length-1]) {
            return "No"
        }
    }
    
    return "Yes";
}