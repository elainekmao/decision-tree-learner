decision-tree-learner
=====================

Decision tree learner takes training data and outputs a decision tree classifier (Artificial Intelligence, Spring 2013)

I implemented this project in Python 3.1 using the Python IDLE GUI. All of the code is in a single file, "ekm2133.py." To run the code, open the file in IDLE and select "Run Module." Once the code has been loaded, type the following into the IDLE window:

>>>decision_tree_learner ("INSERT NAME OF CSV WITH TRAINING DATA HERE")

Note: the CSV with the training data must be located in the same folder as "ekm2133.py," or you will have to specify the filepath.

This will create a new file called, "decision_tree_classifier.py." To run this code, open the file and select "Run Module." You can then call decision_tree_classifier.py on test cases. The function only takes one test case at a time, in the form of a list of the test case's attributes. For instance:

>>>decision_tree_classifier (('Full', 'Yeah', 'Yeah', 'Yeah', '$$$', 'Yeah', 'Italian', '>60'))

The decision_tree_learner function calls the recursive dst function to create a decision tree, which I chose to implement as a dictionary of key-value pairs. The keys correspond to the indices for the attributes, and the values correspond to the subtrees (which are also dictionaries) formed by splitting the tree on a particular attribute. In a decision tree, the attribute indices correspond to nodes, and the tree branches off according to the values. The decision_learner_function creates and writes to the "decision_tree_classifier.py" output file. 

The decision_tree_classifier function created by the decision_tree_learner program calls dtc, a recursive function which traverses the tree (dictionary) until it finds a leaf node, at which point, it returns the leaf node. Leaf nodes contain target values. My program assumes that the target value will always be the last attribute. 

Other functions, such as plurality_value, information_gain, entropy, and remainder are implemented as described in the book, for multi-class problems. The choose_attribute function selects the attribute which has the greatest information gain. 
