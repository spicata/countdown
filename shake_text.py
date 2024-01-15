import random

in_text = input("> ")
time = float(input("> "))
in_text = in_text.replace(" ", "⠀")
out_text = ""
front_wrapper = "<div><p>"
back_wrapper = "</p></div>"
for i in range(len(in_text)):
    time_delay = str(random.uniform(0, time))[:6]
    out_text = out_text + "<span style=\"animation-delay: " + time_delay + "s\">" + list(in_text)[i] + "</span>"
print(out_text)
