# methods for performance comparison
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression



# Takens, F. (1981). Dynamical systems and turbulence, Warwick 1980: Proceedings of a Symposium Held at the 
#   University of Warwick 1979/80, chap. Detecting strange attractors in turbulence, pp. 366–381. Springer 
#   Berlin Heidelberg, Berlin, Heidelberg. https://doi.org/10.1007/BFb0091924.
# x,y pair is x = {y_1,y_2,...,y_p}, y = {y_p+1}
# vanilla autoregressive method
class EmbedDimRegressor:
    
    def __init__(self, num_trunc, num_lag, embed_dimension, num_test):
        
        self.embed_dimension = embed_dimension
        
        assert num_lag > 0, f"lag must be at least 1, input lag: {num_lag}"
            
        
        self.num_lag = num_lag
        self.num_trunc = num_trunc
        self.num_test = num_test
        self.reg = RandomForestRegressor()
        
        
    def CreateOffsetData(self,X):
        
        # truncate
        X_trunc_train = X[self.num_trunc-self.num_lag-self.embed_dimension:-self.num_test-self.num_lag+1]
        # always the same vector, regardless of the lag
        X_test = X[-self.num_test-self.embed_dimension:-self.num_test]
        
        num_train_samples = len(X_trunc_train) - self.embed_dimension
        
        # X will be the embed_dimension lag offset of y; dimension will be (n,1)
        # convert X to lagged features
        X_lagged_features_train = np.array([X_trunc_train[i:i+self.embed_dimension] for i in range(num_train_samples)])
        #X_lagged_features_test = np.array([X_trunc_test[i:i+self.embed_dimension] for i in range(self.num_test)])
        
        # offset y from X
        #    X has already been offset from y
        y_train = X[self.num_trunc-1:-self.num_test]
        y_test_all = X[-self.num_test:]
        y_test = y_test_all[self.num_lag-1]
        
        return X_lagged_features_train, X_test, y_train, y_test
    
    
    def CreatePrequentialData(self,X):
        # Under construction
        pass
        
        
        
        
    
    
    