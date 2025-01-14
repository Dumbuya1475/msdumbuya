from graphviz import Digraph

# Create a directed graph
db_schema = Digraph(format="png")
db_schema.attr(rankdir='LR', size='12')

# Define node attributes
db_schema.attr('node', shape='record', fontsize='10')

# Nodes
db_schema.node('Schools', '''{Schools|
SchoolID (PK) \\l
Name \\l
Address \\l
Contact \\l
SubscriptionPlan \\l}''')

db_schema.node('Staff', '''{Staff|
StaffID (PK) \\l
Name \\l
Email \\l
Phone \\l
RoleID (FK) \\l
SchoolID (FK) \\l}''')

db_schema.node('Roles', '''{Roles|
RoleID (PK) \\l
RoleName \\l}''')

db_schema.node('Students', '''{Students|
StudentID (PK) \\l
Name \\l
ParentEmail \\l
ClassID (FK) \\l
SchoolID (FK) \\l}''')

db_schema.node('Classes', '''{Classes|
ClassID (PK) \\l
ClassName \\l
SchoolID (FK) \\l}''')

db_schema.node('Attendance', '''{Attendance|
AttendanceID (PK) \\l
Date \\l
StudentID (FK) \\l
Status \\l}''')

db_schema.node('Grades', '''{Grades|
GradeID (PK) \\l
StudentID (FK) \\l
SubjectID (FK) \\l
Score \\l
Term \\l}''')

db_schema.node('Subjects', '''{Subjects|
SubjectID (PK) \\l
SubjectName \\l
ClassID (FK) \\l}''')

# Relationships
db_schema.edge('Schools', 'Staff', label='1:n')
db_schema.edge('Schools', 'Students', label='1:n')
db_schema.edge('Schools', 'Classes', label='1:n')

db_schema.edge('Staff', 'Roles', label='n:1')
db_schema.edge('Students', 'Classes', label='n:1')
db_schema.edge('Students', 'Attendance', label='1:n')
db_schema.edge('Students', 'Grades', label='1:n')

db_schema.edge('Classes', 'Attendance', label='1:n')
db_schema.edge('Classes', 'Grades', label='1:n')
db_schema.edge('Classes', 'Subjects', label='1:n')

db_schema.edge('Subjects', 'Grades', label='1:n')

# Render diagram
diagram_path = '/mnt/data/School_DB_Architecture'
db_schema.render(diagram_path)

diagram_path + '.png'
