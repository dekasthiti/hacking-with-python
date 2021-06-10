#
#                      Lambda Calculus Parsing
#
# The goal of this project is to make a Lambda Calculus parser. Lambda
# Calculus is an extremely simple "programming language" (if you can even
# call it that), which has historically been used for computer science proofs.
#
# LANGUAGE SPEC
#
# A Lambda Calculus program consists of a single expression:
#
#    expression
#
# An expression can be either a variable, a lambda, or an application:
#
#    expression = variable | lambda | application .
#
# A variable is just a string, representing the variable's name. For
# simplicity, we define a variable to be one or more lowercase letters.
#
#    variable = { lower-case-letter } .
#    lower-case-letter = "a" | "b" | ... | "z" .
#
# A lambda consists of a variable (the parameter) and an expression (the return
# value):
#
#    lambda = "(" variable "." expression ")" .
#
# An application consists of two expressions between brackets, separated by a
# space. Application represents evaluating a function (the first expression) at
# a specific value (the second expression).
#
#    application = "[" expression " " expression "]" .
#
# Examples/test cases start below at line 84.

class Expr:
    pass


class Variable(Expr):
    def __init__(self, name: str):
        self.name = name
    
    def __eq__(self, other):
        return isinstance(other, Variable) and self.name == other.name
    
    def __str__(self):
        return self.name


class Application(Expr):
    def __init__(self, function: Expr, value: Expr):
        self.function = function
        self.value = value
    
    def __eq__(self, other):
        return (isinstance(other, Application) and self.function == other.function and self.value == other.value)
    
    def __str__(self):
        return f"[{self.function} {self.value}]"


class Lambda(Expr):
    def __init__(self, parameter: Variable, return_value: Expr):
        self.parameter = parameter
        self.return_value = return_value
    
    def __eq__(self, other):
        return (isinstance(other,
                           Lambda) and self.parameter == other.parameter and self.return_value == other.return_value)
    
    def __str__(self):
        return f"({self.parameter}.{self.return_value})"


# PROGRAM

def parse(expr: str) -> Expr:
    #
    # Your code goes here!
    stack = []
    for char in reversed(expr):
        if char == "[":
            stack.append(Application(stack.pop(), stack.pop()))
        elif char == "(":
            stack.append(Lambda(stack.pop(), stack.pop()))
        elif char.isalpha():
            stack.append(Variable(char))
    
    return stack[-1]


# EXAMPLES / TEST CASES

prog0 = "x"
prog0Parsed = Variable("x")

prog1 = "(f.(x.x))"
prog1Parsed = Lambda(Variable("f"), Lambda(Variable("x"), Variable("x")))

prog2 = "[[[(x.(y.[(z.z) y])) a] b] c]"
prog2Parsed = Application(Application(Application(
    Lambda(Variable("x"), Lambda(Variable("y"), Application(Lambda(Variable("z"), Variable("z")), Variable("y")), )),
    Variable("a")), Variable("b")), Variable("c"))

prog3 = "[[(base.(exp.[exp base])) (two.(x.[two [two x]]))] (three.(x.[three [three [three x]]]))]"
prog3Parsed = Application(
    Application(Lambda(Variable("base"), Lambda(Variable("exp"), Application(Variable("exp"), Variable("base")))),
        Lambda(Variable("two"),
               Lambda(Variable("x"), Application(Variable("two"), Application(Variable("two"), Variable("x")))))),
    Lambda(Variable("three"), Lambda(Variable("x"), Application(Variable("three"),
        Application(Variable("three"), Application(Variable("three"), Variable("x")))))))


# MAIN FUNCTION

def main():
    assert parse(prog0) == prog0Parsed
    print("Program 0 passed!")
    
    assert parse(prog1) == prog1Parsed
    print("Program 1 passed!")
    
    assert parse(prog2) == prog2Parsed
    print("Program 2 passed!")
    
    assert parse(prog3) == prog3Parsed
    print("Program 3 passed!")
    
    print("All tests passed! Good work!")


if __name__ == "__main__":
    main()
