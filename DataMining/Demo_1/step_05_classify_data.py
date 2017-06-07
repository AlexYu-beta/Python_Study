from numpy import zeros
from numpy import mean
from step_02_data_analyzer import data, target
from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.cross_validation import cross_val_score


t = zeros(len(target))
t[target == 'setosa'] = 1
t[target == 'versicolor'] = 2
t[target == 'virginica'] = 3

classifier = GaussianNB()
classifier.fit(data,t) # training on the iris dataset


train, test, t_train, t_test = cross_validation.train_test_split(data, t, test_size=0.4, random_state=0)

# train the classifier
classifier.fit(train,t_train) # train
print classifier.score(test,t_test) # test

# confusion matrix
print confusion_matrix(classifier.predict(test),t_test)

# full-detailed report
print classification_report(classifier.predict(test), t_test, target_names=['setosa', 'versicolor', 'virginica'])

scores = cross_val_score(classifier, data, t, cv=6)
print scores
print mean(scores)