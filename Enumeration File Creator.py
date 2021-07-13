import numpy as np

with open("Enumeration File.txt.", 'a') as writer:
    for source in range(1, 6+1):
        for slope in np.arange(0, 2+0.1, 0.1):
            for Q1 in range(215, 225+1):
                for Q2 in range(225, 235+1):
                    writer.write("{}_{}_{}_{}\n".format(int(source), round(slope, 1), int(Q1), int(Q2)))
