# Reproducing Notes



## Contribution

- Since there's no large database of factor returns in Chinese stock market, they build a unique and comprehensive set of factors.
- Use machine learning methods with modern empirical asset pricing research to understand the dynamics of risk premia for stock returns



## Data

- Daily and monthly stock returns data
- Quarterly financial statement data
- One year government bond -- risk-free rate

**Note:** According to CSMAR and Wind, we cannot upload the data aquired from these two database.

## Empirical Analysis

The vector of predictors, $z_{i,t}$, can be represented as
$$
z_{i,t} = [\matrix{c_{i,t}\\x_t\otimes c_{i,t}\\d_{i,t}}]
$$
where $c_{i,t}$ is a vector of stock-level characteristics, $x_t$ is a vector of macroeconomic predictors, and $d_{i,t}$ is a vector of industry dummies.



To evaluate the performance, they use the out-of-sample $R^2$.

### 4 types of models 

Figure out the out-of-sample predictability

- OLS
- Regularized (linear) models (PLS, LASSO, Enet)
- Tree models (GBRT, RF)
- Neural network models (NN1-NN5)



### Analysis group

- Full sample analysis
- Small and large stocks (by market equity, top 70% and bottom 30%)
- Small and large shareholders (by average market capitalization per shareholder (A.M.C.P.S) = market capitalization / number of shareholders. Top 70% threshold)
- SOEs and non-SOEs



- Monthly and annually



### Predictors

**Note:** Construct the factors that are used in this empirical analysis.

**How to measure the performance (variable importance)**:

For a specific model, we calculate the reduction in predictive $R^2$ when setting all values of a given predictor to zero within each training sample, and average them into a single importance measure for each predictor.



### Model selection (measure model performance)

- ~~Unconditional superior predictive ability (USPA) test of Hansen (2005)~~
  - fail to distinguish some model performance
  - the same case as Diebold and Mariano (1995) test
- Conditional superior predictive ability (CSPA) test of Li et al. (2020)



## Portfolio analysis

(TO BE CONTINUED)