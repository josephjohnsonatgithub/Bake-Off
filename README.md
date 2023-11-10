# Bake-Off
Explores process of selecting best methods for time series prediction in chaotic systems.

'OSA' employess 36 simple autoregressive methods to forecast number of state-based attacks across 32 countries.
The question is `How do we know which method to choose for future prediction?'
We show how the employment of a validation period to select a method outperforms the random choice of a model or using no model at all.

We train 36 autoregressive methods proposed by Takens (1), each based on number of lags, from 1 to 36.
All methods will be trained on 48 months of data.
The test set involves 36 months.
Sequentially, the test set occurs directly after the training set.
In order to forecast 36 months into the future, we use one-step-ahead forecasting employed by Hegre (2).

We use three simple methods for choosing:
  1. Naive prediction: We do not choose any of the 36. We simply chooses the last training 'y' sample. Surprisingly hard to beat because it uses the most relevant sample for chaotic systems -- the last one.
  2. No use of validation: We train all methods on the training data, then deploy on the test data. The average prediction represents the expected performance of randomly choosing a method.
  3. Use of validation: We use a 36 month validation period (occurs prior to test period) to test each of the 36 methods. We select the most accurate method for each country and each lag (step into the future) over the validation data to predict the test set. (the selected method is retrained on the combined training and validation data).

As the last cell of `OSA` shows, the validation method outperforms the others.


1. Floris Takens. Detecting strange attractors in turbulence. In Dynamical
systems and turbulence, Warwick 1980, pages 366–381. Springer, 1981.
2. H˚avard Hegre, Marie Allansson, Matthias Basedau, Michael Colaresi,
Mihai Croicu, Hanne Fjelde, Frederick Hoyles, Lisa Hultman, Stina
H¨ogbladh, Remco Jansen, et al. Views: A political violence earlywarning system. Journal of peace research, 56(2):155–174, 2019.
