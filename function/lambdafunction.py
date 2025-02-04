# Lambda function ဆိုတာက ပုံမှန် function တစ်ခုလိုမျိုး formally ရေးစရာမလိုတာပါ။
# Lambda expressions are functions without a name that are quick to create and use. They are written in just one line using the lambda keyword and are often used for small, simple tasks.


# Normal function
def greet(name):
    return f"Hello {name}"


print(greet("Thet Tun"))


# Lambda function
greet = lambda name: f"Hello {name}"
print(greet("Thet Tun"))


# Lambda function ကိုသုံးပြီးတော့ Higher Order Function တစ်ခုကိုပြန်လည်ပေးပါတယ်
def multiply(n):
    return lambda a: a * n


double = multiply(2)
print(double(5))

triple = multiply(3)
print(triple(5))
