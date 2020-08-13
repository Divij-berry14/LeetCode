class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        def combinations(combination, i):
            print(combination)
            if len(combination) == combinationLength:
                self.combinations.append(combination)
            elif len(combination) < combinationLength:
                for j in range(i+1, len(characters)):
                    combinations(combination+characters[j], j)

        for i in range(len(characters)):
            combinations(characters[i], i)
    def next(self) -> str:
        return self.combinations
    def hasNext(self) -> bool:
        pass

c=CombinationIterator("abc", 2)
print(c.next())