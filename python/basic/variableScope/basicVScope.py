'''
Based on the scope, we can classify Python variables into three types:
Local Variables - inside a function
Global Variables - out side of funtion, over context
Nonlocal Variables - nonlocal is a keyword used to inform inner funtion about the varible is form parent function, 

If we change the value of a nonlocal variable, the changes appear in the local variable.
'''

def parentM (name):
    testLocalVariable = "I'm Local variable"

    def childM(childName):
        testLocalChildVariable = "I'm local variable for inner child"

        nonlocal testLocalVariable
        testLocalVariable = "new data changed"

        print("I have recieved",childName,"as argument and my local child var is ",testLocalChildVariable," and the nonlocal that is my parent local var is ",testLocalVariable," and parent has recived ",name)

    childM(name)


parentM("I'm Argument")

# nonlocal is the key word which is first define that u r going to manipulate parent variable then u do rest.