import Convereter   #One  way
from  Convereter import lbs_to_kgs   # Another way to import
from  Convereter import kgs_to_lbs

print(kgs_to_lbs(42))
print(lbs_to_kgs(43))

print(Convereter.kgs_to_lbs(42))