import difflib
from tkinter.filedialog import askopenfilename
import os
os.path.dirname(os.path.abspath(__file__))


file1 = askopenfilename()
file2 = askopenfilename()

file1_lines = open (file1).readlines()
file2_lines = open (file2).readlines()


difference = difflib.HtmlDiff().make_file(file1_lines, file2_lines, file1, file2)
difference_report = open('Juxtapose.html' , 'w')
difference_report.write(difference)
diff = difflib.ndiff(open(file1).readlines(),open(file2).readlines())
#print ''.join(diff),
difference_report.close
