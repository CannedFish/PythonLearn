#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *
import operator, sys

# def createDataSet():
    # group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]]);
    # labels = ['A', 'A', 'B', 'B'];
    # return group, labels;

# group, labels = createDataSet();
# print 'Data set: \n', group;
# print 'Labels: ', labels;

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0];
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet;
    sqDiffMat = diffMat ** 2;
    sqDistances = sqDiffMat.sum(axis = 1);
    distances = sqDistances ** 0.5;

    sortedDistIndicies = distances.argsort();
    classCount = {};
    for i in range(k):
        voteIlable = labels[sortedDistIndicies[i]];
        classCount[voteIlable] = classCount.get(voteIlable, 0) + 1;

    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True);
    return sortedClassCount[0][0];

# p = [float(sys.argv[1]), float(sys.argv[2])];
# print 'Point to test: ', p;
# print 'Classify result: ', classify0(p, group, labels, 3);

def autoNorm(dataSet):
    minVals = dataSet.min(0);
    maxVals = dataSet.max(0);
    ranges = maxVals - minVals;
    normDataSet = zeros(shape(dataSet));
    m = dataSet.shape[0];
    normDataSet = dataSet - tile(minVals, (m, 1));
    normDataSet = normDataSet / tile(ranges, (m, 1));
    return normDataSet, ranges, minVals;

def file2matrix(filename):
    fr = open(filename);
    numberOfLines = len(fr.readlines());
    returnMat = zeros((numberOfLines, 3));
    classLabelVector = [];
    fr = open(filename);
    index = 0;
    for line in fr.readlines():
        line = line.strip();
        listFromLine = line.split('\t');
        returnMat[index, :] = listFromLine[0:3];
        classLabelVector.append(listFromLine[-1]);
        index += 1;
    return returnMat, classLabelVector;

def datingClassTest():
    hoRatio = 0.10;
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt');
    normMat, ranges, minVals = autoNorm(datingDataMat);
    m = normMat.shape[0];
    numTestVecs = int(m * hoRatio);
    errorCount = 0.0;
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :]
                , datingLabels[numTestVecs:m], 3);
        print "The classifier came back with: %s, the real answer is: %s"\
                % (classifierResult, datingLabels[i]);
        if classifierResult != datingLabels[i]:
            errorCount += 1.0;
    print "The total error rate is: %.1f%%" % (errorCount / float(numTestVecs) * 100);

datingClassTest();

# show in plot
# datingDataMat, datingLabels = file2matrix('datingTestSet.txt');
# normMat, ranges, minVals = autoNorm(datingDataMat);
# import matplotlib
# import matplotlib.pyplot as plt

# fig = plt.figure();
# ax = fig.add_subplot(111);
# labelTrans = {'largeDoses': 1, 'smallDoses': 2, 'didntLike': 3};
# labels = [labelTrans[label] for label in datingLabels];
# ax.scatter(normMat[:, 0], normMat[:, 1]
        # , 15.0 * array(labels), 15.0 * array(labels));
# plt.show();

