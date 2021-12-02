def win(FIVB, t1, t2): 
    # return True if team t1 won against team t2, otherwise return False
    return t2 in FIVB[t1]
    
def get_all_teams(FIVB):
    # return a list of teams that participated in the FIVB2021 in alphabetical order (A-Z).
    s = set()
    for x in FIVB:
      s.add(x)
      for y in FIVB[x]:
        s.add(y)
    return sorted(list(s))
    
def calculate_points(FIVB):
    # return a dictionary where key is each team and its value is points of the team.
    # 3 points for a win
    # A team that did not win any team gets 0 point.
    points = dict()
    temp = get_all_teams(FIVB)
    for x in temp:
        if x in FIVB:
            points[x] = 3 * len(FIVB[x])
        else:
            points[x] = 0
    return points
    
    
def read_fivb() :
    # build a dictionary FIVB from inputs, of which structure is shown in the example given above

    FIVB = dict()
    while True:
        d = input().split()
        if len(d) == 1 : break
        
        if d[0] in FIVB:
          FIVB[d[0]].append(d[1])
        else:
          FIVB[d[0]] = [d[1]]
    return FIVB
