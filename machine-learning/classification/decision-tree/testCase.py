#!/usr/bin/env python
# -*- coding: utf-8 -*-

import treePlotter, trees

"""generate the test case tree"""
# with open('lenses.txt') as fr:
  # lenses = [inst.strip().split('\t') for inst in fr.readlines()];
  # lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate'];
  # lensesTree = trees.createTree(lenses, lensesLabels);
  # trees.storeTree(lensesTree, 'testCaseTree.txt');
  # treePlotter.createPlot(lensesTree);

"""show the tree"""
tree = trees.grabTree('./testCaseTree.txt');
labels = ['age', 'prescript', 'astigmatic', 'tearRate'];
treePlotter.createPlot(tree);
print "['pre', 'hyper', 'no', 'normal'] -> %s"\
    % trees.classify(tree, labels, ['pre', 'hyper', 'no', 'normal']);
print "['young', 'myope', 'no', 'reduced'] -> %s"\
    % trees.classify(tree, labels, ['young', 'myope', 'no', 'reduced']);

