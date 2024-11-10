"""
Suppose you want to fit different models to the data 
and 
you want to be able to add new models without changing the existing code.

First let's see an example of how not to do it.
"""

class Model:
    def __init__(self, model):
        self.model = model

    def fit(self, X, y):
        if self.model == 'linear':
            return self.fit_linear(X, y)
        elif self.model == 'logistic':
            return self.fit_logistic(X, y)
        else:
            raise ValueError('Invalid model')

    def fit_linear(self, X, y):
        print('Fitting linear model')
        return X + y

    def fit_logistic(self, X, y):
        print('Fitting logistic model')
        return X + y
    
"""
In this Model class, you have methods to fit linear and logistic models.
But suppose later on you want to add Naive Bayes Model.

In the current implementation, 
you would have to modify the Model class to add a new method 
fit_naive_bayes and modify the fit method to include the new model.

This violates the Open-Closed Principle, which states that 
a "Well Designed" class should be open for extension but closed for modification.

The way to solve this problem is to make the Model class an interface 
and have concrete classes for each model.
This way when you want to add a new model you can just implement the interface
"""

from abc import ABC, abstractmethod

class Model:
    
    @abstractmethod
    def fit(self, X, y):
        pass

class LinearModel(Model):
    def __init__(self, model:str) -> None:
        self.model = model

    def fit(self, X, y):
        print('Fitting linear model')
        return X + y
    
class LogisticModel(Model):
    def __init__(self, model:str) -> None:
        self.model = model

    def fit(self, X, y):
        print('Fitting logistic model')
        return X + y
    
# Add a new model class
class NaiveBayesModel(Model):
    def __init__(self, model:str) -> None:
        self.model = model

    def fit(self, X, y):
        print('Fitting Naive Bayes model')
        return X + y
    
if __name__ == '__main__':
    linear = LinearModel('linear')
    logistic = LogisticModel('logistic')
    naive_bayes = NaiveBayesModel('naive_bayes')
    
    print( linear.fit(1, 2) )
    print( logistic.fit(1, 2) )
    print( naive_bayes.fit(1, 2) )