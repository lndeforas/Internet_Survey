import matplotlib.pyplot as plt
from data import Data

d = Data()
why, folder_save, question = d.args()
plt.rcParams["figure.figsize"] = (11,9)

# All 
d.plot("children")

# Gender 
d.plot("gender")

# Prim/sec school
d.plot("school")

# Gender and prim/sec school
d.plot("school_gender")