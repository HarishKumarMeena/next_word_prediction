# next_word_prediction
Predict the next word based on the given input

// Known issue
not able to traverse the same line after getting the match for word

ex:

there is a line in dataset => "Hello my name is my name is my name is blabla"

and input is => "hello everyone my name"

output => "is"

dictionary key value => {"is": 1}


dictionary key value if we traverse through whole line => {"is": 3}


// add on
take the whole input string to predict the next word
