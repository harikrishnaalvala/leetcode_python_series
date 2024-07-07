class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q, bank = collections.deque([(startGene,0)]), set(bank)

        while q:
            g, m = q.popleft()
            if g == endGene : return m
            
            # [2] try all possible mutations, namely,
            #     try every nucleotide in each position
            for i in range(len(g)):
                for n in "ATGC":
                    gm = g[0:i] + n + g[i+1:]
                    # [3] successful branches are added to
                    #     the queue for further mutagenesis
                    if gm in bank:
                        bank.remove(gm)
                        q.append((gm, m+1))
        
        return -1
