This is a introduction to assignment 1, for which I used the ubuntu 20.04 and python3.8. The code and some commands for questions 1 and 2 are summarized in the report(in canvas). For question 3, I uploaded the Python code and the XML file for this question. Thanks for your reading.

Here are some tips of codes (also in the report).
### Q1.Linux operating system and memory hierarchy

(1) Open a terminal, run the command ”top”, and save a screenshot in your report.

Run the command "top", which can real-time display the system each process of the resource occupation status.

```shell
$ top
```

(2) Use a few Linux commands to collect the hardware information of your computer to draw the memory hierarchy diagram (see, e.g., Slide 54 in Lecture 1). List the used commands and briefly explain what they are used for.

--Collect the CPU information by using the command "lscpu"

```shell
$ lscpu
```

```shell
$ lshw -short
```

(3) Install the Linux “tree” command

```shell
$ sudo apt install tree
$ cd /; tree | head -n 15
```

--The "cd" command is an acronym for each word in "Change Directory," functions to switch from the current working directory to the specified working directory.

--The "tree" command is to view the directory and file structure, default Ubuntu does not install tree, so use sudo apt install tree to install first.

--The "head" command is used to display the contents of the beginning of a file. By default, the head command displays the first 10 lines of the file. Here “head | -n 15" means displaying the first 15 lines of the file.

### Q2.Bash script

Write a bash script to create 100 directories/folders, whose names are “DDM1, DDM2, DDM3, ..., DDM100”. In each directory, generate a text file, “time till now.txt”

```shell
touch test.sh                   "Create a bash script"
vim test.sh                     "Modify the bash script"

for i in {1...100}
do
   mkdir./DDM$I
   i=$(($i+1))
done

:w and :q                       "Save and exit"
bash test.sh                    "Run the bash script"
ls                              "displays the contents of the working directory)."
```

### Q3.Regular expression

(1) Print all the text lines with the “blockID” values that start with the letter “i” or “g”, and end with digits, e.g., ‘<emItem blockID="i334" id="{0F827075-B026-42F3-885D-98981EE7B1AE}">’. 

```python
import re
import xml.etree.ElementTree as ET

tree=ET.parse('blocklist.xml')
root1=tree.getroot()
#print(len(root1))
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
try:
    import unicodedata
    unicodedata.numeric(s)
    return True
except (TypeError, ValueError):
    pass 
return False

for i in range(len(root1)):
    for j in range(len(root1[i])):
        temp=root1[i][j]
        temp_str=root1[i][j].attrib['blockID']
        if is_number(temp_str[len(temp_str)-1]):
            if temp_str[0]=='i' :
                print("<emItem blockID=\"%s\" id=\"%s\">"%(temp.attrib['blockID'],temp.attrib['id']))
            if temp_str[0]=='g' :
                print("<gfxBlacklistEntry blockID=\"%s\">"%(temp.attrib['blockID']))
```
Some output like this:
<br>
\<emItem blockID="i1211" id="flvto@hotger.com"\>
<br>
\<emItem blockID="i576" id="newmoz@facebook.com"\>
<br>
\<emItem blockID="i258" id="helperbar@helperbar.com"\>
<br>
\<emItem blockID="i218" id="ffxtlbr@claro.com"\>

(2) Print all the text lines where the “id” values are email addresses. Skip the email addresses that are written by regular expressions containing special characters, such as “\, /, ˆ ”.

```python
import re
import xml.etree.ElementTree as ET

tree=ET.parse('blocklist.xml')
root1=tree.getroot()
#print(len(root1))
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
try:
    import unicodedata
    unicodedata.numeric(s)
    return True
except (TypeError, ValueError):
    pass
return False

for i in range(len(root1)):
    for j in range(len(root1[i])):
        temp=root1[i][j]
        if 'id' in temp.attrib:
            if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',temp.attrib['id']):
                print("<emItem blockID=\"%s\" id=\"%s\">"%(temp.attrib['blockID'],temp.attrib['id']))
```
Some output like this:
<br>
\<emItem blockID="i1523" id="{a0d7ccb3-214d-498b-b4aa-0e8fda9a7bf7}"\>
   <br>
\<emItem blockID="i1524" id="ext@alibonus.com"\>
   <br>
\<gfxBlacklistEntry blockID="g194"\>
   <br>
\<gfxBlacklistEntry blockID="g1072"\>
