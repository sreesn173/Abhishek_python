"""list examples"""

EC2_name_list=["t2.medium", "t3.large", "t2.large"]



print(EC2_name_list[1])

'''Q3: What is the difference between a list and a tuple in Python, and when would you choose one over the other in a DevOps context?

list is mutable and tuple is immutable.
'''

'''Q4: How can you access elements in a list, and provide a DevOps-related example?

'''

servers = ['web-server-01', 'db-server-01', 'app-server-01']
#first_server = servers.pop(0)

print(servers)

servers = ['web-server-01', 'db-server-01', 'app-server-01']
servers.append('db-server-02')

print(servers)

no_servers= {10,300,20, 40, 20, 55, 66}

print(no_servers)