from mimetypes import init
from flask import Flask
from collections import deque
import decimal

app = Flask(__name__)

def calcPi(limit):  # Generator function
    """
    Prints out the digits of PI
    until it reaches the given limit
    """

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0
    result2 = ""
    while counter != decimal + 1:
            if 4 * q + r - t < n * t:
                    # yield digit
                    result2 = result2 + str(n)
                    # insert period after first digit
                    if counter == 0:
                            result2 = result2 + "."
                    # end
                    if decimal == counter:
                            #print('')
                            break
                    counter += 1
                    nr = 10 * (r - n * t)
                    n = ((10 * (3 * q + r)) // t) - 10 * n
                    q *= 10
                    r = nr
            else:
                    nr = (2 * q + r) * l
                    nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
                    q *= k
                    t *= l
                    l += 2
                    k += 1
                    n = nn
                    r = nr
                    #print(nr)
    return result2

def factorial(n):
  count = 1
  prod = 1
  while count <= n:
    prod *= count
    count += 1
  return str(prod)

def fib(number_of_terms):
  counter = 0

  first = 0
  second = 1
  temp = 0
 
  while counter <= number_of_terms:
      #print(first)
      temp = first + second
      first = second
      second = temp
      counter = counter + 1
  return str(first)

def A(m, n):
    stack = []
    stack.append(m)
    while stack:
        m = stack.pop()
        if m == 0:
            n = n + 1
        elif n == 0:
            n = 1
            stack.append(m-1)
        else:
            n = n - 1
            stack.append(m-1)
            stack.append(m)
    return str(n)

def factorial1(n):
    factorials = [1]
    for i in range(1, n + 1):
        factorials.append(factorials[i - 1] * i)
    return factorials


def compute_e(n):
    decimal.getcontext().prec = n + 1
    e = 2
    factorials = factorial1(2 * n + 1)
    for i in range(1, n + 1):
        counter = 2 * i + 2
        denominator = factorials[2 * i + 1]
        e += decimal.Decimal(counter / denominator)
    return str(e)

@app.route("/get-fib/<number>")
def getFib(number):
  return {"fib": fib(int(number))}

@app.route("/get-factorial/<number>")
def getFactorial(number):
  return {"factorial": factorial(int(number))}

@app.route("/get-pi/<number>")
def getPi(number):
  return {"pi": calcPi(int(number))}

@app.route("/get-ackermann/<number1>/<number2>")
def getA(number1, number2):
  return {"A": A(float(number1), float(number2))}

@app.route("/get-e/<number>")
def getE(number):
  return {"e": compute_e(int(number))}