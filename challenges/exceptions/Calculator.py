from InvalidFormulaException import InvalidFormulaException
import re


def verify_formula(formula):
    result = re.split(r'[*+\-//](?=[^/*+/\-])', formula)
    return True if len(result) >= 2 else False


def evaluate(formula):
    if verify_formula(formula):
        print(eval(formula))
    else:
        raise InvalidFormulaException('The given formula is invalid')


try:
    evaluate('43/2')
except (InvalidFormulaException, SyntaxError) as e:
    print(e)
