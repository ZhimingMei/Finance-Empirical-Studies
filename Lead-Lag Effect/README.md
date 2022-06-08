### Introduction
This project is the recurrence of paper *Industry Information Diffusion and the Lead-Lag Effect in Stock Returns* by Kewei Hou. Paper link: https://academic.oup.com/rfs/article-abstract/20/4/1113/1615954

In this empirical recurrence, we choose industries in China, and typically, we choose the exploitation of real estate as our target.

We use CSMAR as our database, and we use weekly data, same as the reference paper, to conduct this test. Please refer to https://www.gtarsc.com for more details.

And stocks are chosen in the range of Chinese A share stock market.

### Conclusion
In China, still, there exists the lead-lag effect in some industries, especiallt in real estate and internet industries.

And further, we will use this effect to develop a quantitative strategy.

### Reference
In this empirical study, Machine Learning + provides comprehensive guide on implementing VAR test by Python. See https://www.machinelearningplus.com/time-series/vector-autoregression-examples-python/ for details

*May 8, 2022 Updates*     
The previous empirical test was based on weekly data, however, the conclusion might be biased if the whole industry performed well (on the whole) during the testing period. Hence, we move forward to **intraday data** to further explore the lead-lag effect.
