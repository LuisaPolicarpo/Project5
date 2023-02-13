# Project5

Folders:
Asset - Images used for the dashboard
Dataset - EDA and datasets
Pages - pages for dashboard in Dash

Data Sets used:
Dataset - Nº disembarking passengers, nr of overnights and nr of guests.

Code: EDA, Timeseries, Prediction

EDA Files for time series were made 3 different analysis/scenarios:

Prediction_2020_2023_(1).ipynb) In this file we calculate the prediction from 2020 untill the end of 2023, based in the values from 01/2017 until 12/2019. The goal was to observe which values we would obtain, in case covid hadn't happened. So basically, first we calculated a test size and a train size. Second we decided which model (ARIMA, SARIMA, Exponential smoothing or linear regression+seasonality) had the smaller mean square error (MSE). Third we used that model with the train set, to predict the values from 2020 to 2023. Notes:

-Our real values dataset is from 01/2017 untill 11/2022.
-The model used in this case was the linear regression for the trend and the avg of the months for seasonality.
-Then we will have to predict future values from 11/2022 untill 12/2023, based in the values from 01/2020 untill 11/2022 (file Prediction 2022-2023 (2).ipynb) and also on the values from 01/2017 untill 11/2022 (file Prediction 2022-2023 (3).ipynb). For this we will have to create a new test and train set for each scenario, then train and test in all the models above and choose the one with smaller MSE to predict the values for the future time range.

Dashboard:
http://luisafreitas.pythonanywhere.com/how_much
