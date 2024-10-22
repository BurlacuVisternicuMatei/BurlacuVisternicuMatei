
def build_xml_function(tag, content, **kargs):
    s = "<"
    s += tag
    s += " "

    for i in kargs:
        s += i
        s += "="
        s += "\""
        s += kargs.get(i)
        s += "\""
        s += " "
    s += ">"
    s += content
    s += "</"
    s += tag
    s += ">"
    return s

tag = "a"
content = "Hello World"
print(build_xml_function(tag, content, href =" http://python.org ", _class =" my-link ", id= " someid "))