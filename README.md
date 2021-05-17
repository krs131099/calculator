# SIMPLE CALCULATOR api

@author: K R S Nandhan.

This is a simple calcluator api, user can call the api with a expression as a input parameter and,

gets the answer for the expression in JSON format. This program was written in Python using Flask.



### Some assumptions were made in making this program:

* This calculator can only perfom operations of addition, subtration, multiplication, and division.
* Scientific Expressions are not handled by this calculator.
* Brackets are neglected due to complex expressions.
* The first element is always a positive number.
* Number of operators should be sufficient for operands.
* The expression should be encoded before calling api.
* All integers are considered as unsigned.


### Approach:
1. First, a raw quoted string is unquoted and any white spaces around string is trimmed.
2. Check that, expression does not violate assumptions.
3. Using regular expressions, list of operators and operands was extracted.
4. With BODMAS rule to calculate expressions,
   ( i). First all the divisions were made.
   (ii). Next all the divisions were made.
   (iii).Perform addition or subtraction on the remaining elements.
   (iv). Return result in json format.


### api information

GET url/calc
Performs the calculation and returns answer in json format.

Input : "expression" -> string containing the expression

Output : dictionary in json format.
    "Answer"    -> Contains answer if the input expression is valid.
    "Message"   -> Happy message.
    "Error"     -> If the expression is invalid, this key is generated.
    "Reason"    -> Explanation for the Error.


### api usage

**NOTE : Please read the assumptions before performing calculaitons**
**NOTE : Please encode the expression before sending request manually.**
examples:
(i). Expression = "12+3"
    `GET url/calc?expression=12%2B3` 

    `{
        "Answer"    =   15.0,
        "Message"   =   "Happy Calculations"
    }`

(ii).Expression = "100 + 58 * 13/13"
    `GET url/calc?expression=100%20%2B%2058%20%2A%2013%20/13`

    `{
        "Answer"    =   158.0 ,
        "Message"   =   "Happy Calculations"
    }`

(iii). Expression = (100+2)
    `GET url/calc?expression=%28100%2B2%29`

    `{
        "Error"     =   "Invalid Expression",
        "Reason"    =   "Expression does not starts or ends with digit"
    }`

(iv). Expression = 100 58 * 13
    `GET url/calc?expression=100%2058%20%2A%2013`

    `{
        "Error"     =   "Invalid Expression",
        "Reason"    =   "Number of Operators are not matching to perform operation."
    }`


*If given extra time, support for complex expressions is implemented.*
