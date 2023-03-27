import ipdb
from lib import *


# role ---<  # audition 


# Test your code below...


mcbeth = Role("mcbeth")
peter_parker = Role("peter_parker")
slash = Role("slash")

kevin = Audition("kevin", "new york, ny", False, peter_parker)
dakota = Audition("dakota", "sunnyville, fl", False, slash)
mike = Audition("mike", "cancun, mexico", False, mcbeth)
jon = Audition("jon", "lima, peru", True, mcbeth)
joe = Audition("joe", "clifton, nj", True, mcbeth)





# the below line allows us to stop & try stuff!
ipdb.set_trace()



#mcbeth.lead() 
# if self.hired == false,
# print(no actor has been hired for this role)