from itertools import permutations

def solution(k, dungeons):
    
    all_dun = len(dungeons)
    answer = -1
    
    for lst in permutations(dungeons, all_dun):
        hp = k
        count = 0
        
        for item in lst:
            if hp >= item[0]:
                hp -= item[1]
                count += 1
        if count > answer:
            answer = count
    

    return answer