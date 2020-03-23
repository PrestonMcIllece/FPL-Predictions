import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

#%matplotlib inline
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso

DATAPATH = 'fantasy-premier-league-20182019/FPL_2018_19_Wk0.csv'
data = pd.read_csv(DATAPATH)

# data.drop(['Name', 'Position'], axis = 1, inplace = True)
# print(data.head())


def scatter_plot(x_variable, y_variable):
    plt.figure(figsize=(4, 4))
    plt.scatter(
        data[x_variable],
        data[y_variable],
        c='black'
    )
    plt.xlabel("{}".format(x_variable))
    plt.ylabel("{}".format(y_variable))
    plt.show()


# scatter_plot('Cost', 'Points')
# scatter_plot('Creativity', 'Points')
# scatter_plot('Influence', 'Points')
# scatter_plot('Threat', 'Points')
# scatter_plot('ICT', 'Points')
# scatter_plot('Goals_conceded', 'Points')
# scatter_plot('Goals_scored', 'Points')
# scatter_plot('Assists', 'Points')
# scatter_plot('Own_goals', 'Points')
# scatter_plot('Penalties_missed', 'Points')
# scatter_plot('Penalties_saved', 'Points')
# scatter_plot('Saves', 'Points')
# scatter_plot('Yellow_cards', 'Points')
# scatter_plot('Red_cards', 'Points')
# scatter_plot('TSB', 'Points')
# scatter_plot('Minutes', 'Points')
# scatter_plot('Bonus', 'Points')

Xs = data.drop(['Name', 'Position', 'Team'], axis = 1)
y = data['Points'].values.reshape(-1,1)

lasso = Lasso()
parameters = {'alpha': [1e-15, 1e-10, 1e-8, 1e-4, 1e-3, 1e-2, 1, 5, 10, 20]}
lasso_regressor = GridSearchCV(lasso, parameters, scoring ='neg_mean_squared_error', cv = 5)
lasso_regressor.fit(Xs, y)
print(lasso_regressor.best_params_)
print(lasso_regressor.best_score_)
print(lasso_regressor.cv_results_)