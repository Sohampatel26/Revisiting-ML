# -*- coding: utf-8 -*-
"""Decision tree using Scikitlearn.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Vo4ro3J2ts4wFnSlzTDxlmMLMiLHbA3N
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'FeatureA': [2, 1, 3, 2],
    'FeatureB': [3, 4, 2, 1],
    'Label': [0, 0, 1, 1]
}
df = pd.DataFrame(data)
X = df[['FeatureA', 'FeatureB']]
y = df['Label']

# Train a decision tree classifier using entropy
clf = DecisionTreeClassifier(criterion='entropy', min_samples_split=2, max_depth=3)
clf.fit(X, y)

# Predict
predictions = clf.predict(X)
print("Predictions:", predictions)

# Plot the tree
plt.figure(figsize=(10, 6))
tree.plot_tree(clf, feature_names=['FeatureA', 'FeatureB'], class_names=['0', '1'], filled=True)
plt.show()