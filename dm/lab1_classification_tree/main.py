#!/usr/bin/env python3.5

import pandas as pd
from names import *
from matplotlib.pyplot import show
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn import preprocessing

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

target = df.loc[:, expirations]
predictors = df.loc[:, features[0]:features[-1]]
X_train, X_test, y_train, y_test = train_test_split(predictors
    , target
    , test_size=0.4
    , random_state=42
)
clf = tree.DecisionTreeClassifier(
    random_state=17,
    max_depth=3,
    min_samples_leaf=10,
    class_weight='balanced',
    max_features=0.8
)

clf = clf.fit(X_train, y_train)
scores = cross_val_score(clf, X_test, y_test, cv=5, scoring='f1')
print(scores)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
ind = list(range(1000))
value = [list(predictors.loc[x]) for x in ind]
tar = [target.loc[x] for x in ind]
# [[2, 36, 2, 5, 2384, 1, 2, 4, 3, 1, 1, 4, 33, 3, 1, 1, 2, 1, 1, 1],
        #  [4, 24, 2, 3, 1533, 1, 2, 4, 2, 1, 3, 3, 38, 2, 2, 1, 3, 1, 2, 1]]
pred = list(clf.predict(value))

res = sum(1 if t == p else 0 for t, p in zip(tar, pred))
print(res, len(ind))


# dot_data = tree.export_graphviz(clf, feature_names=['laufkont', 'laufzeit', 'moral', 'verw', 'hoehe',
#                                                     'sparkont', 'beszeit', 'rate', 'famges', 'buerge', 'wohnzeit',
#                                                     'verm', 'alter', 'weitkred', 'wohn', 'bishkred', 'beruf',
#                                                     'pers', 'telef', 'gastarb'],
#                                 class_names=['credit', 'no_credit'],
#                                 out_file='small_tree.dot', filled=True)
# (graph,) = pydot.graph_from_dot_file('small_tree.dot')
# graph.write_png('example1_graph.png')
