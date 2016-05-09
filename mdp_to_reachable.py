import sys
import random
import mdp

# Takes in an mpd, returns if terminal is reachable
# from init without hitting something along the way
def get_reachable(mdp):
    reachable_states = [mdp.init]
    new_rs = []
    policy = policy_iteration(mdp)
    while True:
        for state in reachable_states:
            if state in policy:
                for (result_state, prob) in mdp.T(state, policy[state]).iteritems():
                    new_rs = new_rs + [result_state, state]
                #new_rs = new_rs + [policy[state]]
        new_rs = list(set(new_rs))
        if new_rs == reachable_states:
            print "returning: " + str(new_rs)
            return new_rs
        else:
            reachable_states = new_rs
    return True # Let's make sure the whole loop works first
    #return terminal in reachable_states ## this probably doesn't work yet
