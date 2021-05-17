import re
import flask
from flask import jsonify, request
import urllib.parse


# NOTE :: This calculator program was built under some assumptions.
# Kindly refer, README file for more information.


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/calc', methods=['GET'])
def calculator():

    
    # extract required data and unquote(decode) string.
    expression = urllib.parse.unquote(request.args.get('expression')).strip()


    if len(re.findall(r"^\d.+\d$",expression)) == 0:
        # expression does not starts or ends with numbers
        output = {  "Error":"Invalid Expression",
                    "Reason":"Expression does not starts or ends with digit"
                }
        return jsonify(output)
    

    #preprocess and get operators and operands
    operators = re.findall(r"[+\-*/]",expression)
    operands = re.findall(r"[0-9]+", expression)

    
    if len(operators)==0 or len(operands)==0:
        output = {  "Error": "Invalid Expression",
                    "Reason":"Does not contain operators or operands"
                }


    if len(operators)+1 != len(operands):
        # Expression is invalid
        output = {"Error": "Invalid Expression",
                "Reason":"Number of Operators are not matching to perform operations."
                }
        return jsonify(output)

    
    # Using BODMAS rule,
    # First preference is for '/', followed by '*', then '+', and '-'

    # count nubmer of multiplication operators and division operators
    mul_count = operators.count('*')
    div_count = operators.count('/')


    # compute all divisions
    while div_count:
        
        # get index of '/' for popping operands
        pos = operators.index('/')
        
        # get two operands at the position of '/'
        a = float(operands.pop(pos))
        b = float(operands.pop(pos))
        
        # insert the result at position
        operands.insert(pos, a/b)

        # eliminate operator
        operators.pop(pos)
        
        div_count -= 1
    
    
    while mul_count:

        # get index of '*' for popping operands
        pos = operators.index('*')
        
        # get operands at position of '*'
        a = float(operands.pop(pos))
        b = float(operands.pop(pos))
        
        # insert result at pos
        operands.insert(pos, a*b)

        #eliminate operator
        operators.pop(pos)

        mul_count -= 1


    # Calculate additions and subtractions
    for x in (operators):

        a = float(operands.pop(0))
        b = float(operands.pop(0))
        
        #
        if x == '+':    
            operands.insert(0,a+b)
        else:
            operands.insert(0,a-b)

    # operands list then contains one item, which is the final result.

    output = {}
    output['Answer'] = operands[0]
    output['Message'] = "Happy Calculations"
    
    # return output in json format
    return jsonify(output)

app.run()
