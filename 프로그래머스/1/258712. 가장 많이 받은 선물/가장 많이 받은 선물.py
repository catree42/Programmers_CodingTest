friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]


def make_giverList(gifts) : 
    giverList = []
    for gift in gifts :
        giver, receiver = gift.split()
        giverList.append(giver)
    print(giverList)
    return giverList

def make_receiverList(gifts) : 
    receiverList = []
    for gift in gifts :
        giver, receiver = gift.split()
        receiverList.append(receiver)
    return receiverList

def make_GiftIndexList(friends, giverList, receiverList) : 
    giftIndexList=[]
    for friend in friends :
        count1 = giverList.count(friend)
        count2 = receiverList.count(friend)
        giftIndexList.append(count1 - count2)
    print(giftIndexList)
    return giftIndexList

def cal_nextGiftCounts(gifts, friends) :   
    # 친구 모두를 1대1로 비교 -> gifts에 둘 관계가 있는 만큼 giver ++, 없으면 둘 중 선물 지수 높은 쪽 ++ 
    nextGiftCounts = [ 0 for i in friends]
    giftIndexList = make_GiftIndexList(friends, make_giverList(gifts),make_receiverList(gifts))
    print(giftIndexList)
    for idx1 in range(len(friends)-1) :
        for idx2 in range(idx1+1, len(friends)) : 
            str1 = friends[idx1] + ' ' + friends[idx2]
            str2 = friends[idx2] + ' ' + friends[idx1]
            count1 = gifts.count(str1)
            count2 = gifts.count(str2)
            if count1 > count2 :
                nextGiftCounts[idx1] += 1
            elif count1 < count2 :
                nextGiftCounts[idx2] += 1
            else : 
                if giftIndexList[idx1] > giftIndexList[idx2] : 
                    nextGiftCounts[idx1] += 1
                elif giftIndexList[idx1] < giftIndexList[idx2] : 
                    nextGiftCounts[idx2] += 1
    print(nextGiftCounts)
    return nextGiftCounts
            
    

def solution(friends, gifts):
    answer = 0
    nextGiftCounts = cal_nextGiftCounts(gifts, friends)
    answer = max(nextGiftCounts)
    return answer

solution(friends, gifts)