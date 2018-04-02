#!/usr/bin/env python


from sklearn import datasets as skd
import random
from sklearn.neighbors import KNeighborsClassifier
from scipy.spatial import distance


def euc(a, b):
    return distance.euclidean(a, b)


class RandomClf(object):
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = random.choice(self.y_train)
            predictions.append(label)
        return predictions


class ScrappyKNN(object):
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self, row):
        best_dist = euc(row, self.X_train[0])
        best_index = 0

        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if best_dist > dist:
                best_dist = dist
                best_index = i

        return self.y_train[best_index]


def get_accuracy(classifier):
    iris = skd.load_iris()

    X = iris.data
    y = iris.target

    from sklearn.cross_validation import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)

    # Classifier
    clf = classifier()
    # ---------

    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)

    from sklearn.metrics import accuracy_score

    score = accuracy_score(y_test, predictions)

    return score


def main():
    print "RandomClf"
    print "=" * 15
    print "Accuracy score: %f.3" % get_accuracy(RandomClf)
    print "=" * 15
    print "KNeighborsClassifier"
    print "=" * 15
    print "Accuracy score: %f.3" % get_accuracy(KNeighborsClassifier)
    print "=" * 15
    print "ScrappyKNN"
    print "=" * 15
    print "Accuracy score: %f.3" % get_accuracy(ScrappyKNN)
    print "=" * 15


if __name__ == '__main__':
    main()
