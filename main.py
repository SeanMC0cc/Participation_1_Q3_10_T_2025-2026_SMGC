# If-Elif-Else Statement Example

from pyscript import display, document

def convert_temperature(event):
    Fahrenheit = document.getElementById("Temperature").value
    document.getElementById("output").innerHTML = ""

    celsius = (float(Fahrenheit) - 32) * 5/9

    if celsius > 37.9:
        result = "a fever."

    elif celsius < 33:
        result = "hypothermia."
    else:
        result = "no fever."

    display(f'Your temperature in celsius is {celsius} and you have {result}', target="output")