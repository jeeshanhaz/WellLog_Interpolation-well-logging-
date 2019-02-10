from sklearn.linear_model import LinearRegression,LogisticRegression,RandomizedLogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, BaggingRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.model_selection import cross_val_score

class interpolation():

    def __init__(self, train_df):
        self.train_df = train_df


    def validation(self, algorithm = RandomForestRegressor,kwds ={},cv=3,scoring='r2'):
        clf = algorithm(**kwds)
        scores = cross_val_score(clf, self.train_df[['DEPTH', 'lat', 'long']], self.train_df['RHOB'], cv=cv,
                                 scoring=scoring)
        print("Scoring ("+ scoring+") : %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))



    def prediciton(self,test_df,property_ = 'RHOB',algorithm=RandomForestRegressor,kwds={}):
        clf = algorithm(**kwds)
        clf.fit(self.train_df[['DEPTH', 'lat', 'long']], self.train_df[property_])
        pred = clf.predict(test_df)
        test_df['RHOB'] = pred
        return test_df





