import sys
import random
import mdp
import generate_mdp

# Takes in an mpd, returns if terminal is reachable
# from init without hitting something along the way
def get_reachable(m):
    reachable_states = [m.init]
    new_rs = []
    policy = mdp.policy_iteration(m)
    while True:
        for state in reachable_states:
            if state in policy:
                for (result_state, prob) in m.T(state, policy[state]).iteritems():
                    new_rs = new_rs + [result_state, state]
                #new_rs = new_rs + [policy[state]]
        new_rs = list(set(new_rs))
        if new_rs == reachable_states:
            print "breaking: " + str(new_rs)
            #return new_rs
            break
        else:
            reachable_states = new_rs
    return True # Let's make sure the whole loop works first
    #return terminal in reachable_states ## this probably doesn't work yet

my_mdp = mdp.read_mdp("fig17.mdp")

print get_reachable(my_mdp)
