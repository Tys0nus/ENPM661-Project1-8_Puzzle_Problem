import numpy as np
import collections as co

global count 
# GOAL
# goal = np.array([[5, 2, 0], [8, 3, 4], [7, 1, 6]]) # Goal Case 0
# goal = np.array([[1, 4, 7], [2, 5, 8], [3, 0, 6]]) # Goal Case 1
# goal = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 0]]) # Goal Case 2

goal = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 0]]) # Enter Goal State

# START NODE
# p = np.array([[8, 3, 2], [7, 4, 6], [0, 5, 1]]) # Test Case 0
# p = np.array([[1, 6, 7], [2, 0, 5], [4, 3, 8]]) # Test Case 1
# p = np.array([[4, 7, 8], [2, 1, 5], [3, 6, 0]]) # Test Case 2

p = np.array([[4, 7, 8], [2, 1, 5], [3, 6, 0]]) # Enter Initial State

############################################
# PARSE NODES:
parse_goal = np.reshape(goal,9)

p = np.reshape(p,9)
parse_p = np.transpose(p)
parse_p = np.reshape(parse_p,9)
############################################

count = 1
############################################

def main():
    print("Executing:")
    
    ## Function: Find Blank
    def fb(y):
        return np.argwhere(y==0)

    ## Function: Move Left
    def act_move_left(y):
        r,c = fb(y)[0,0], fb(y)[0,1]
        if c>0:
            y[r,c-1],y[r,c] = y[r,c],y[r,c-1]
            return y
        return

    ## Function: Move Right
    def act_move_right(y):
        r,c = fb(y)[0,0], fb(y)[0,1]
        if c<(len(y[0])-1):
            y[r,c],y[r,c+1] = y[r,c+1],y[r,c]
            return y
        return

    ## Function: Move Up
    def act_move_up(y):
        r,c = fb(y)[0,0], fb(y)[0,1]
        if r>0:
            y[r-1,c],y[r,c] = y[r,c],y[r-1,c]
            return y
        return

    ## Function: Move Down
    def act_move_down(y):
        r,c = fb(y)[0,0], fb(y)[0,1]
        if r<(len(y)-1):
            y[r,c],y[r+1,c] = y[r+1,c],y[r,c]
            return y
        return
    ############################################

    poplist = co.deque()
    index = co.deque()
    seq = []
    parent ={}
    node = {}

    index.append(count)
    parent[tuple(p)] = None
    node[tuple(p)] = 1
    poplist.append(p)

    ## Function: Explore States
    def states(op):
        act_list = [act_move_left, act_move_right, act_move_up, act_move_down]

        for act in act_list:
            result = act(op.copy())

            if result is not None:
                result = np.reshape(result,9) # RESHAPE
                if tuple(result) not in parent:
                    if tuple(parse_goal) in parent:
                        return
                    feed = np.reshape(result,9)
                    parent[tuple(feed)] = idx
                    global count
                    count +=  1
                    index.append(count)
                    node[tuple(feed)] = count
                    poplist.append(feed)
                    
    ##############################################

    # Function: Tracking Path
    def tracking(seq):
        track = []

        loc = len(seq)-1
        ele = seq[loc][-1]
        track.insert(0,ele)

        while True:
            ele = seq[loc-1][0]
            track.insert(0,ele)

            if track[0]==1:
                break
            loc_list = [seq.index(subseq) for subseq in seq for val in subseq if val == ele]
            loc = loc_list[0]
        
        return track

    ##############################################
    while True:
        tr = [*index]
        seq.append(tr)
        if tuple(parse_goal) in parent:
            break
        check = poplist.popleft()
        idx = index.popleft()
        check_arr = np.reshape(check,(3,3)) # RESHAPE
        check_arr_new = np.transpose(check_arr) # Corrected
        states(check_arr)

    track_path = tracking(seq)

    ##############################################
    # Creating OUTPUT Files:
    with open('NodesInfo.txt', 'w') as file:
        for key, value in parent.items():
            nodeval = ' '.join(map(str, key))
            file.write(f"{nodeval}\n")

    with open('Nodes.txt', 'w') as file:
        file.write('C\tP\tNode\n')
        for key, value in parent.items():
            cnode = node.get(key, 'unknown')
            nodeval = ' '.join(map(str, key))
            file.write(f"{cnode}\t{value}\t{nodeval}\n")

    with open('nodePath.txt', 'w') as file:
        for key, value in node.items():
            if value in track_path:
                nodeval = ' '.join(map(str, key))
                file.write(f"{nodeval}\n")

if __name__ == "__main__":
    main()
    