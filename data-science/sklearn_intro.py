#!/usr/bin/env python


from sklearn import datasets as skd
from sklearn import svm
import matplotlib.pyplot as plt


def main():
    iris = skd.load_iris()
    digits = skd.load_digits()
    clf = svm.SVC(gamma=0.001, C=100)
    clf.fit(digits.images[:-1], digits.targets[:-1])

    p = clf.predict(digits.data[-1:])

    print p

    plt.figure(1, figsize=(3, 3))
    plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
    plt.show()


if __name__ == '__main__':
    main()
