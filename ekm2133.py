#Elaine Mao
#ekm2133
#Project 4

#Import modules
import csv
import math

#Initialize global variables
dataset = list()
decision_tree = {}

#Create output file for new program
output_tree = open ("decision_tree_classifier.py", "w")

#Opens the training file and writes to the output file
def decision_tree_learner (data):
        with open(data, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                dataset.append([element.strip() for element in row])
        dst (dataset, range(len(dataset[0])), [])
        output_tree.write(\
\
"def decision_tree_classifier (instance):\n\
\tdtc (instance, "+str(choose_attribute(dataset))+", "+str(decision_tree)+")\n\n\
\
def dtc (instance, key, tree):\n\
\tvalue = instance [key]\n\
\tif type (tree [key]) is str:\n\
\t\tprint (tree[key])\n\
\t\treturn tree[key]\n\
\telif type (tree[key][value]) is str:\n\
\t\tprint (tree[key][value])\n\
\t\treturn tree[key][value]\n\
\telse:\n\
\t\tdtc (instance, list(tree[key][value].keys())[0], tree[key][value])") 
        output_tree.close()

#Main function which creates the decision tree (dictionary)
def dst (examples, attributes, parent_examples):
        global decision_tree
        if examples == ():
                return plurality_value(parent_examples)
        elif same_class (examples):
                return (decision_outcomes (examples) [0])
        elif len(attributes) - 1 == 0:
                return plurality_value (examples)
        else:
                A = choose_attribute (examples)
                tree = {A:{}}
                for attribute in attribute_values (A, examples):
                        subtree = dst (select_examples(A, attribute, examples), [attributes for attribute in attributes if attribute != A], examples) 
                        tree [A][attribute] = subtree
        decision_tree = tree
        return tree

#Given a list of examples, returns the most common target value
def plurality_value (examples):
        return max (decision_outcomes(examples), key = lambda v: count (v, examples))

#Counts the number of examples with a given target value   
def count (value, examples):
        count = 0
        for row in examples:
                if row[len(row)-1] == value:
                        count = count + 1
        return count

#Determines if every member of a set of examples is in the same class
def same_class (examples):
        if len (decision_outcomes (examples)) == 1:
                return True
        else:
                return False        

#Chooses the attribute which maximizes information gain
def choose_attribute (examples):
        attributes = range(len(examples[0]) - 1)
        return max (attributes, key = lambda a: information_gain (a, examples))

#Information gain function
def information_gain (attribute_index, examples):
        return entropy (dataset) - remainder (attribute_index, examples)

#Entropy function
def entropy (examples):
        total_entropy = 0
        values = decision_outcomes (examples)
        N = int(len(examples))
        for value in values:
                p = 0
                for row in examples:
                        if row[len(row)-1] == value:
                                p = p+1
                q = p/N
                if q == 0 or q == 1:
                        total_entropy = total_entropy
                else:
                        total_entropy = total_entropy + q*math.log(q,2)
        return -(total_entropy)

#Possible values for target variable 
def decision_outcomes (examples):
        outcome_list = []
        for row in examples:
                if row[len(row) - 1] not in outcome_list:
                        outcome_list.append (row [len(row) - 1])
        return outcome_list

#Remainder function
def remainder (attribute_index, examples):
        remainder = 0
        N = int(len(dataset))
        for value_list in attribute_split (attribute_index, examples):
                remainder = remainder + (int(len(value_list[1:]))/N)*(entropy(value_list[1:]))
        return remainder

#Splits the examples into lists grouped by attribute                
def attribute_split (attribute_index, examples):
        example_list = []
        for value in attribute_values (attribute_index, examples):
                temp_list = [value]
                for row in examples:
                        if row[attribute_index] == value:
                                temp_list.append (row)
                example_list.append (temp_list)
        return example_list

#Possible values for a given attribute                                                
def attribute_values (attribute_index, examples):
        value_list = []
        for row in examples:
                if row[attribute_index] not in value_list:
                        value_list.append (row[attribute_index])
        return value_list

#Selects the examples with a given value for a given attribute
def select_examples (attribute_index, value, examples):
        example_list = []
        for row in examples:
                if row[attribute_index] == value:
                        example_list.append (row)
        return example_list
