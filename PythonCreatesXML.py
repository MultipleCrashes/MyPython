from xml.dom.minidom import Document
doc=Document()

Employee=doc.createElement("Employee")
doc.appendChild(Employee)
firstName=doc.createTextNode("Harish")
middleName=doc.createTextNode("kumar")
lastName=doc.createTextNode("upadhyay")
fname=doc.createElement("fname")
Employee.appendChild(fname)
fname.appendChild(firstName)
lname=doc.createElement("lname")
Employee.appendChild(lname)
lname.appendChild(lastName)
mname=doc.createElement("mname")
Employee.appendChild(mname)
mname.appendChild(middleName)


filename="employee.xml"
f=open(filename,"w")
f.write(doc.toprettyxml(indent=" "))
f.close()
