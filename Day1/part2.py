from set import data

def get_similarity(leftList:list[int], rightList:list[int]):
    similarity_score = 0
    for lc in range(len(leftList)):
        for rc in range(len(rightList)):
            if rightList[rc] == leftList[lc]:
                similarity_score += leftList[lc]
    return similarity_score;

if __name__ == "__main__":
    set_one = [x[0] for x in data]
    set_two = [x[1] for x in data]

    set_one.sort()
    set_two.sort()