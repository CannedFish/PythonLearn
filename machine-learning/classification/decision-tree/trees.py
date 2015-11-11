#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import log

def calcShannonEnt(dataSet):
    """calculate the shannon entropy"""
    numEntries = len(dataSet);
    labelCounts = {};
    for featVec in dataSet:
        currentLable = featVec[-1];
        if currentLable not in labelCounts.keys():
            labelCounts[currentLable] = 0;
        labelCounts[currentLable] += 1;

    shannonEnt = 0.0;
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries;
        shannonEnt -= prob * log(prob, 2);

    return shannonEnt;

def createDataSet():
    """Create dataset and class labels"""
    dataSet = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']
    ];
    labels = ['no surfacing', 'flippers'];
    return dataSet, labels;

def splitDataSet(dataSet, axis, value):
    """split the data set"""
    retDataSet = [];
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis];
            reduceFeatVec.extend(featVec[axis + 1 :]);
            retDataSet.append(reduceFeatVec);
    return retDataSet;

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1;
    baseEntropy = calcShannonEnt(dataSet);
    bestInfoGain = 0.0;
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet];
        uniqueVals = set(featList);
        newEntropy = 0.0;
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value);
            prob = len(subDataSet) / float(len(dataSet));
            newEntropy += prob * calcShannonEnt(subDataSet);
        infoGain = baseEntropy - newEntropy;
        if infoGain > bestInfoGain:
            baseInfoGain = infoGain;
            bestFeature = i;
    return bestFeature;

"""entropy test"""
myData, labels = createDataSet();
print myData;
# print calcShannonEnt(myData);
print splitDataSet(myData, 0, 1);
print splitDataSet(myData, 0, 0);

