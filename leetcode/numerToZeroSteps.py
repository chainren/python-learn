def numberOfSteps (num):
        """
        :type num: int
        :rtype: int
        """
        time =0
        while num!=0:
            if num%2==0:
                num = num/2
            else:
                num = num-1
            time+=1
        return time

print(numberOfSteps(17))

def game(guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
        time = 0
        for i in range(0,3):
            if guess[i] == answer[i]:
                time+=1
        return time

print(game([1,2,3],[3,2,3]))