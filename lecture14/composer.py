def happy(text):
    return "☻" + text + "☻"

def sad(text):
    return "☹" + text + "☹"

def composer(f, g):
    def composed(x):
        return f(g(x))
    return composed

msg1 = composer(sad, happy)("CS 111!")
msg2 = composer(happy, sad)("CS 240!")

msg3 = composer(lambda text: "0"+text+"0", happy)("Prof Connole")
print(msg3)