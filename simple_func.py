# Learner: James Caple
# 7/25/2021
#
# Compare the ML way to calculate the values defined in use_hello_world.py
# with this simple function.  Obviously this simple function requires less
# code and precisely calculates the correct value.  However, this is not really
# an apples-to-apples comparison as the complexity of the features potentially used
# to train an ML model would soon outpace our ability to program a comparable
# function to calculate similar answers with.

def model(x):
    result = x + ((x+1)+x)
    return result

# Should be exactly 31
print(model(10))

# Should be exactly 289
print(model(96))