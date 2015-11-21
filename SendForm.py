import re
from mechanize import Browser

watchlist = [("COMPSCI", "34840")]

br = Browser()
br.set_handle_robots(False)
br.open("http://www.reg.uci.edu/perl/WebSoc")
br.select_form(nr=1)

inp = watchlist[0]
if 1:
#def scrape(inp):
    forms = [f for f in br.forms()]
    f = forms[1]
    dept, course = inp
    f["Dept"] = [dept]
    submit_response = br.submit(name="Submit", label="Display Web Results")
    out=submit_response.read()
    
    start = out.find(course)
    end = out.find('\n', start)
    line = out[start:end]
    aa=line.split(r'</td>')
    
    bb=[]
    for i in aa:
        if i.find(r'</') >=0:
            temp=i[:i.find(r'</')]
            bb.append(temp[temp.rfind(r'>')+1:])
        else:
            bb.append(i[i.find(r'>')+1:])
    
    MAXSTRENGTH = int(bb[8])
    curr = bb[9]
    waitlist = int(bb[10])
    if '/' in curr:
        t=curr.split('/')
        curr = int(t[-1])
    
    
    print MAXSTRENGTH, curr
    
    print len(bb)
#    print out[locstart:locend]
#    locend = out[loc:].find('\n')
#    line = out[loc:loc+locend]
#    print line
#    o=line
    
    
#    print out[loc:loc+100]



#for i in watchlist:
#    dept, course = i
#    scrape(i)


a=r'34840</td><td  nowrap="nowrap">Lec</td><td bgcolor="#D5E5FF"  nowrap="nowrap">A</td><td  nowrap="nowrap">4</td><td bgcolor="#D5E5FF"  nowrap="nowrap">LOPES, C.</td><td  nowrap="nowrap">MW &nbsp;  9:30-10:50 </td><td bgcolor="#D5E5FF"  nowrap="nowrap"><a href="http://www.classrooms.uci.edu/GAC/ICS174.html" target="_blank">ICS 174</a></td><td  nowrap="nowrap">Wed, Mar 16, 8:00-10:00am</td><td bgcolor="#D5E5FF" align="right" nowrap="nowrap">120</td><td align="right" nowrap="nowrap">65 / 78</td><td bgcolor="#D5E5FF" align="right" nowrap="nowrap">0</td><td align="right" nowrap="nowrap">83</td><td bgcolor="#D5E5FF" align="right" nowrap="nowrap">0</td><td  nowrap="nowrap">K and L</td><td bgcolor="#D5E5FF"  nowrap="nowrap"><a href="http://book.uci.edu/ePOS?this_category=76&amp;store=446&amp;form=shared3/gm/main.html&amp;design=446"  target="_blank">Bookstore</a></td><td  nowrap="nowrap">&nbsp;</td><td bgcolor="#D5E5FF" nowrap="nowrap"><b><font color="green">OPEN</font></b></td></tr> 990'
