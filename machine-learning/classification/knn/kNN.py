#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *
import operator, sys
from os import listdir

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

try:
    k = int(sys.argv[1]);
except Exception:
    k = 3;

# Handwriting recognition
def img2vector(filename):
    returnVect = zeros((1, 1024));
    fr = open(filename);
    for i in range(32):
        lineStr = fr.readline();
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j]);
    return returnVect;

def handwritingClassTest():
    hwLabels = [];
    trainingFileList = listdir('trainingDigits');
    m = len(trainingFileList);
    trainingMat = zeros((m, 1024));
    for i in range(m):
        fileNameStr = trainingFileList[i];
        fileStr = fileNameStr.split('.')[0];
        classNumStr = int(fileStr.split('_')[0]);
        hwLabels.append(classNumStr);
        trainingMat[i, :] = img2vector('trainingDigits/%s' % fileNameStr);
    
    testFileList = listdir('testDigits');
    errorCount = 0.0;
    mTest = len(testFileList);
    errorRecord = [];
    for i in range(mTest):
        fileNameStr = testFileList[i];
        # if fileNameStr == '': continue;
        fileStr = fileNameStr.split('.')[0];
        try:
            classNumStr = int(fileStr.split('_')[0]);
        except Exception:
            print 'Error:', fileNameStr;
            continue;
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr);
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, k);
        # print 'The classifier came back with: %d, the real answer is: %d.'\
                # % (classifierResult, classNumStr);
        if classifierResult != classNumStr:
            errorRecord.append('Error: %d -> %d, in %s'\
                    % (classNumStr, classifierResult, fileNameStr));
            errorCount += 1.0;

    errorRate = errorCount / float(mTest);
    print '\nThe total number of errors is: %d' % errorCount;
    print '\nThe total error rate is: %.1f%%' % (errorRate * 100);
    return errorRecord, errorRate;

errorRecord, errorRate = handwritingClassTest();
def show(s):
    print s;
map(show, errorRecord);
        
# Error rate test
# def datingClassTest():
    # hoRatio = 0.10;
    # datingDataMat, datingLabels = file2matrix('datingTestSet.txt');
    # normMat, ranges, minVals = autoNorm(datingDataMat);
    # m = normMat.shape[0];
    # numTestVecs = int(m * hoRatio);
    # errorCount = 0.0;
    # for i in range(numTestVecs):
        # classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :]
                # , datingLabels[numTestVecs:m], k);
        # print "The classifier came back with: %s, the real answer is: %s"\
                # % (classifierResult, datingLabels[i]);
        # if classifierResult != datingLabels[i]:
            # print classifierResult, datingLabels[i];
            # errorCount += 1.0;
    # print "The total error rate is: %.1f%%, with K is: %d."\
            # % (errorCount / float(numTestVecs) * 100, k);

# datingClassTest();

# Real app
# def classifyPerson():
    # percentTats = float(raw_input('percentage of time spent playing video games? '));
    # ffMiles = float(raw_input('frequent flier miles earned per year? '));
    # iceCream = float(raw_input('liters of ice cream consumed per year? '));
    # datingDataMat, datingLabels = file2matrix('datingTestSet.txt');
    # normMat, ranges, minVals = autoNorm(datingDataMat);
    # inArr = array([ffMiles, percentTats, iceCream]);
    # classifierResult = classify0((inArr - minVals) / ranges, normMat, datingLabels, k);
    # print 'You will probably like this person', classifierResult;
   
# classifyPerson();

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

