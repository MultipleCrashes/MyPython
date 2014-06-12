from nntplib import *    # network news transfet library 
s = NNTP('web.aioe.org')  # server which store netword news ,there are many free servers
(resp,count,first,last,name)=s.group('comp.lang.python') # connecting to the above server
# connection to server ,count of articles , first article ,last article etc in above line 

(resp,subs) =s.xhdr('subject',(str(first)+'-'+str(last)))   # for getting subject of news letter 1-10 ( first to last number of article 

for subject in subs[-10:]:  # last 10 out of all 
    print subject 

number = input('Which artilce you want ?')
(reply,num, id, list)= s.body(str(number))   # get the body

for line in list:
    print line


