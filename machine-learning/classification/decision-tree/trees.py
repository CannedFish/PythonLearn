#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import log
import operator

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
    bestFeature = -1;
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
            bestInfoGain = infoGain;
            bestFeature = i;
    return bestFeature;

def majorityCnt(classList):
    classCount = {};
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0;
        classCount[vote] += 1;
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True);
    return sortedClassCount[0][0];

def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet];
    if classList.count(classList[0]) == len(classList):
        return classList[0];
    if len(dataSet[0]) == 1:
        return majorityCnt(classList);
    bestFeat = chooseBestFeatureToSplit(dataSet);
    bestFeatLabel = labels[bestFeat];
    myTree = {bestFeatLabel: {}};
    del(labels[bestFeat]);
    featValues = [example[bestFeat] for example in dataSet];
    uniqueVals = set(featValues);
    for value in uniqueVals:
        subLabels = labels[:];
        myTree[bestFeatLabel][value] = createTree(
                splitDataSet(dataSet, bestFeat, value), subLabels);
    return myTree;

def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0];
    secondDict = inputTree[firstStr];
    featIndex = featLabels.index(firstStr);
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec);
            else:
                classLabel = secondDict[key];
    return classLabel;

def storeTree(inputTree, filename):
    import pickle;
    with open(filename, 'w') as fw:
        pickle.dump(inputTree, fw);

def grabTree(filename):
    import pickle;
    with open(filename) as fr:
        tree = pickle.load(fr);
    return tree;

if __name__ == '__main__':
    """console test"""
    myData, labels = createDataSet();
    print myData;
    # print calcShannonEnt(myData);
    # print splitDataSet(myData, 0, 1);
    # print splitDataSet(myData, 0, 0);
    # print chooseBestFeatureToSplit(myData);

    # labels2 = labels[:];
    # generate and store tree
    tree = createTree(myData, labels);
    print tree;
    # storeTree(tree, 'mytree.txt');

    # restore tree
    # tree = grabTree('mytree.txt');
    # print '(0, 0) -> %s' % classify(tree, labels, [0, 0]);
    # print '(1, 1) -> %s' % classify(tree, labels, [1, 1]);

