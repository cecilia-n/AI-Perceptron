# AI-Perceptron
Implemented and trained a perceptron learning model where: 

The perceptron learns the concept of logical-or (i.e., 1 or 1 is true, 0 or 0 is false, 0 
or 1 is true, 1 or 0 is true).

The function expects five arguments, in this order, left-to-right:
A number representing the threshold
A number representing the adjustment factor 
A list of numbers representing the initial weights on the inputs
A list of examples for training the perceptron
A number representing the number of passes the perceptron should make through
the list of example


Each example in the list of examples has two parts. The first part (True or False) indicates 
whether this example is a positive example (True) of the concept to be learned or a negative 
example (False). The second part is a list of 1’s or 0’s. This list (the 1's and 0's) must be the same 
length as the list of initial weights.

The variable weights is bound to the list of weights shown above, and that the 
variable examples is bound to that list of examples.
