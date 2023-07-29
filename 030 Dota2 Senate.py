# DDRRR
# DRRD  # D removes first R and goes to end of queue
# RDD   # D removes second R and goes to end of queue
# DR    # R removes D and goes to end
# D     # D removes R
        # D declares itself the winner
    
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        Dqueue , Rqueue = deque(), deque()

        for i, c in enumerate(senate):
            if  c == "R":
                Rqueue.append(i)
            else:
                Dqueue.append(i)
        
        while Dqueue and Rqueue:
            dTurn = Dqueue.popleft()
            rTurn = Rqueue.popleft()
            if rTurn < dTurn:
                Rqueue.append(dTurn+len(senate))
            else:
                Dqueue.append(rTurn+len(senate))

        return "Radiant" if Rqueue else "Dire"