import re
from mechanize import Browser

watchlist = [("COMPSCI", "34840")]

br = Browser()
br.set_handle_robots(False)
br.open("http://www.reg.uci.edu/perl/WebSoc")
br.select_form(nr=1)

def scrape(inp):
    forms = [f for f in br.forms()]
    f = forms[1]
    dept, course = i
    f["Dept"] = [dept]
    submit_response = br.submit(name="Submit", label="Display Text Results")
    out=submit_response.read()
    print out    


# Browser passes through unknown attributes (including methods)
# to the selected HTMLForm (from ClientForm).


for i in watchlist:
    dept, course = i
#    print dept, course
    scrape(i)
#