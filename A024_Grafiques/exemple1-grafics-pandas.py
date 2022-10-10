import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

#np --> numerical panda, es una llibreria per a realitzar càlcul numèric
#les notes de dawbio amb series
student_list=["John","Mary","Lucy","Peter", "Sarah"]
grades_list = [7,9,8,4,5]
wants_dual_list = [False,True,False,True, True]
datos: dict[list] = {"grade": grades_list,
                   "dual": wants_dual_list}
students_frame = pd.DataFrame(
    index=student_list,
    data = datos
)
students_frame = students_frame.sort_values(by=['grade'], ascending=False)
students_frame.loc[:,"grade"].plot(kind="bar")
plt.show()