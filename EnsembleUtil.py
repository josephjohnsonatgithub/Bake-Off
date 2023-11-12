# various functions for creating ensembles

import itertools
import numpy as np

# generates an ensemble based on the n learners with the highest mutual diversity 
#  chosen from the K most accurate learners
def AccuracyDiversityEnsemble(acc_arr,pred_arr, K, n):
    ''' 
    acc_arr: num_learners, mse
    pred_arr: num_learners,num_preds
    K: top learners in terms of accuracy
    n: number of learners to choose whose mutual diversity is greatest'''
    
    # get most accurate learners
    learner_list = acc_arr.argsort()[:K].tolist()
    
    # https://stackoverflow.com/questions/8371887/making-all-possible-combinations-of-a-list
    outer_els = [list(x) for x in itertools.combinations(learner_list, n)]
    
    mutual_diff = np.zeros(len(outer_els))
    
    for t_idx,t_ens in enumerate(outer_els):
        
        # list of (i,j) pairs
        inner_els = [list(x) for x in itertools.combinations(t_ens, 2)]
        
        t_mutual_diff = np.zeros(len(inner_els))
        
        # calculate mutual difference
        for inner_idx,[i,j] in enumerate(inner_els):
            
            # index into pred_arr using actual learner index (embed_dim-1)
            t_diff = pred_arr[i] - pred_arr[j]
            t_mutual_diff[inner_idx] = np.sum(t_diff**2)
            
        mutual_diff[t_idx] = t_mutual_diff.mean()
    
    best_ens = outer_els[mutual_diff.argmax()]
    
    # convert to embedding dimensions
    best_embed_dims = (np.array(best_ens)+1).tolist()
    
    return best_embed_dims