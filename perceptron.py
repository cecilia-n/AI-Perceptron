"""
Perceptron function accepts the following arguments: 
threshold, which is a number representing the threshold; 
adjust, which is a number representing the adjustment factor;
example, which is a list of numbers representing the initial weights on the inputs;
training, which is a list of examples for training the perceptron;
passes, which is the number representing the number of passes the perceptron should make throughthe list of examples.
What is outputted are print statements showing the perceptron algorithm ; 
given starting weights/example, for each pass, for each of the inputs in the training examples,
if the prediction is not the same as the answer, then calculations are made which results in
the adjusted weights
"""
def perceptron(threshold, adjust, example, training, passes):
    print("Starting weights:", example)
    print("Threshold:", threshold, end=" ")
    print("Adjustment:", adjust)
    for p in range(1, passes+1):  #increment when whole set training is done
        print()
        print("Pass:", p)
        print()
        for train in training:
            print("inputs:",
                  train[1])  #print second element of each list in training
            activation = calculate(example, train)
            if activation <= threshold:
                prediction = False
            else:
                prediction = True
            print("prediction:", prediction, end=" ")  #for each input, calculate sum #Use calculate to get prediction value
            answer = train[0]
            print("answer:", answer)
            if prediction == False and answer == True:
                example = updateWeightsIfActuallyTrue(example, adjust, train)
            elif prediction == True and answer == False:
                example = updateWeightsIfActuallyFalse(example, adjust, train)
            print("adjusted weights:", example)

           

"""
updateWeightsIfActuallyTrue function has arguments: 
example, which is a list of numbers representing the initial weights on the inputs;
adjustment, which is a number representing the adjustment factor;
train, which is a list of examples for training the perceptron.
The function returns an adjusted weighted list if the prediction was false, but the answerwas actually true
"""
def updateWeightsIfActuallyTrue(example, adjustment, train):
    s = []
    for numIndex in range(len(example)):
        num = example[numIndex]
        # print("train:",train[1][numIndex])
        # print("num:",num)
        s.append(train[1][numIndex] * adjustment + num)
    return s  #list of adjusted weights
    #don't add or subtract if input 0
    #print out adjusted weights

"""
updateWeightsIfActuallyFalse function has arguments: 
example, which is a list of numbers representing the initial weights on the inputs;
adjustment, which is a number representing the adjustment factor;
train, which is a list of examples for training the perceptron.
The function returns an adjusted weighted list if the prediction was true, but the answer was actually false
"""
def updateWeightsIfActuallyFalse(example, adjustment, train):
    s = []
    for numIndex in range(len(example)):
        num = example[numIndex]
        # print("train:",train[1][numIndex])
        # print("num:",num)
        if train[1][numIndex] == 0:
            s.append(num)
        if train[1][numIndex] == 1:
            s.append(num - adjustment)
    return s

    #(Use numIndex) if element in input/trainingtest list is 0, add adjust value to example for element in same position
    #if element is 1, leave by itself

"""
Calculate function has arguments:
example, which is a list of numbers representing the initial weights on the inputs;
train, which is a list of examples for training the perceptron.
Function that calculates the value s (or activation) which will later help determine if the prediction 
is either true or false    
"""
def calculate(example, train):
    #for each element in the weight list, multiply by values in training (the second element in each list)
    s = 0
    for numIndex in range(len(example)):
        num = example[numIndex]
        # print("train:",train[1][numIndex])
        # print("num:",num)
        s += train[1][numIndex] * num
    return s



# ######TEST perceptron####
# initalexample = [-0.5, 0, 0.5, 0, -0.5]
# trainingTest = [[True, [1, 1, 1, 1, 0]], [False, [1, 1, 1, 1, 1]],
#                 [False, [0, 0, 0, 0, 0]], [False, [0, 0, 1, 1, 0]],
#                 [False, [1, 0, 1, 0, 1]], [False, [1, 0, 1, 0, 0]],
#                 [False, [0, 1, 0, 1, 1]], [False, [0, 1, 0, 1, 0]],
#                 [False, [0, 0, 1, 0, 0]], [False, [0, 0, 0, 1, 0]]]

# print()
# print("Perceptron:")
# print(perceptron(0.5, 0.1, initalexample, trainingTest, 4))

######TEST perceptron####
examples = [[True, [1,1]],
 [False, [0,0]],
 [True, [0,1]],
 [True, [1,0]]]

weights = [0.3, -0.6]

perceptron(0.4, 0.09, weights, examples, 10)


