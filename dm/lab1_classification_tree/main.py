#!/usr/bin/env python3.5

import pandas as pd
from names import *
from matplotlib.pyplot import show
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn import preprocessing
import pydot

import numpy as np

from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("potreb.csv", header=0)#, parse_dates=[1])
le = preprocessing.LabelEncoder()
# data = pd.read_excel('credit.xls')

# print(df.columns.values)
# print(df)

for cat in categories:
    df[cat] = df[cat].astype("category")

values_to_encode = sum([list(df[cat].unique()) for cat in categories], [])
le.fit(values_to_encode)

for cat in categories:
    df[cat] = le.transform(df[cat])

# sclearn gridsearch

target = df.loc[:, expirations]
predictors = df.loc[:, features[0]:features[-1]]
# X_train, X_test, y_train, y_test = train_test_split(predictors
#     , target
#     , test_size=0.4
#     , random_state=42
# )
# clf = tree.DecisionTreeClassifier(
#     random_state=17,
#     min_samples_leaf=10,
#     class_weight='balanced',
#     max_features=0.8
# )
# clf = clf.fit(X_train, y_train)
# scores = cross_val_score(clf, X_test, y_test, cv=5, scoring='f1')
# print(scores)
# print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
#
# dot_data = tree.export_graphviz(
#     clf,
#     feature_names=features,
#     class_names=['Просрочка', 'нет'],
#     out_file='small_tree.dot',
#     filled=True
# )
# (graph,) = pydot.graph_from_dot_file('small_tree.dot')
# graph.write_png('example_graph.png')
# select p value | select k best
# features = SelectKBest(chi2 , k=14).fit_transform(predictors, target)
predictors = predictors.drop(code, axis=1)
print(target.value_counts())
print(
    pd.DataFrame(np.c_[(predictors.columns, *chi2(predictors, target))],
    columns=['var', 'chi2', 'p']
    ).sort_values('p').head(20))
features = SelectKBest(chi2 , k=5).fit_transform(predictors, target)
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.7, random_state=100)
# sample_weight_last_ten = abs(pd.np.random.randn(len(X_train)))
# sample_weight_last_ten[5:] *= 5
# sample_weight_last_ten[9] *= 15
clf4 = tree.DecisionTreeClassifier(class_weight=[4, 1])
tree_para = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [4, 5, 6, 7, 8, 9, 10, 11, 12, 15],
    # 'min_samples_split': [4, 10, 15, 20, 30, 40, 50, 90, 120, 150],
    'splitter': ['best', 'random'],
    'class_weight': ['balanced', {0: 1, 1: 4}, {0: 1, 1: 10}]
 }
clf4 = GridSearchCV(clf4, tree_para, cv=5, scoring=['neg_log_loss', 'roc_auc'], refit='neg_log_loss')
clf4.fit(X_train, y_train)
print(clf4.best_params_)
y_pred = clf4.predict(X_test)
print(classification_report(y_test, y_pred))
scores = cross_val_score(clf4, X_test, y_test, cv=2, scoring='f1')
print(confusion_matrix(y_test, y_pred))

# print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
# print()
