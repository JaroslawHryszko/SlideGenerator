from paraphrase import paraphrase_eugene
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

outputfile = open("content.tex", "w")


linecounter = 0
slidecounter = 0
poprzednialinia = ''
header1 = ''
header2 = ''
header3 = ''
openframe = 0
itemize = 0
liniinaslajd = 4
ignore = 0
parsedline = ''
sectionstart = 0
startcollecting = 0

with open('source.txt', encoding='utf8') as file:
    for line in file:
        linecounter+=1
        if line[0].isdigit() and (line[1] == "." or (line[0].isdigit() and line[1].isdigit() and line[2] == ".")):
            startcollecting = 0
            naglowek = line.strip()
            if (line[2].isdigit() and line[3] == "." and line[4].isdigit()) or (line[0].isdigit() and line[1].isdigit() and line[2] == "." and line[3].isdigit() and line[4] == "." and line[5].isdigit()):
                header3 = line.strip()
                line = "\\subsubsection{" + line.strip() + "}\n\n"
                linecounter -= 1
            elif (line[2].isdigit() and not line[3].isdigit() and line[3] != ".") or (line[0].isdigit() and line[1].isdigit() and line[2] == "." and line[3].isdigit() and not line[4].isdigit() and line[4] != "."):
                header2 = line.strip()
                header3 = ""
                line = "\\subsection{" + line.strip() + "}\n\n"
                linecounter -= 1
            elif line[0].isdigit() and ((line[1] == "." and not line[2].isdigit()) or (line[1].isdigit() and line[2] == "." and not line[3].isdigit())):
                header1 = line.strip()
                line = "\\section{" + line.strip() + "}\n\n"
                linecounter -= 1
                header2 = ""
                header3 = ""
                sectionstart = 1
                print(header1)
            if openframe == 1:
                line = "\\end{frame}\n\n" + line
                openframe = 0
                linecounter = 0
                slidecounter += 1
            line = line + "\\begin{frame}\n\\centering\n" + naglowek + "\n\\end{frame}\n"
            if header2 == "": header = header1
            else: header = header2
            if sectionstart != 1:
                if header3 != "": line = line + "\n\\begin{frame}{" + header + "}\n\\framesubtitle{" + header3 + "}\n"
                else: line = line + "\n\\begin{frame}{" + header + "}\n"
                openframe = 1
            else:
                line = line + "\n"
                sectionstart = 0
        elif line.strip() == "\\begin{itemize}": itemize = 1
        elif line.strip() == "\\end{itemize}": itemize = 0
        elif line[0:19] == "Learning Objectives":
            startcollecting = 0
            if header1 == "": header = header2
            else: header = header1
            line = "\\begin{frame}{" + header + "}\n\\framesubtitle{Learning objectives}\n"
            if openframe == 1: line =  "\\end{frame}\n\n" + line
            if itemize == 1:
                line = "\\end{itemize}\n" + line
                itemize = 0
            openframe = 1
            linecounter = 0
            slidecounter += 1
            header3 = "Learning Objectives"
        elif line.strip() == "Keywords":
            startcollecting = 0
            if header1 == "": header = header2
            else: header = header1
            line = "\\begin{frame}{" + header + "}\n\\framesubtitle{Keywords}\n\\textbf{Keywords:}"
            if openframe == 1: line =  "\\end{frame}\n\n" + line
            if itemize == 1:
                line = "\\end{itemize}\n" + line
                itemize = 0
            openframe = 1
            keywordsframe = 1
            linecounter = 0
            slidecounter += 1
            header3 = "Keywords"
        elif linecounter >= liniinaslajd and line.strip() != "\\begin{itemize}" and line.strip() != "\\end{itemize}":
            lines = line.split(".", 1)
            #bufor = line
            if header2 == "": header = header1
            else: header = header2
            if len(lines) > 1 and header3 != "Learning Objectives":
                if lines[0].strip() != "" and lines[1].strip() != "":
                    if header3 != "": line = lines[0] + ".\n\\end{frame}\n\n\\begin{frame}{" + header + "}\n\\framesubtitle{" + header3 + "}\n" + lines[1]
                    else: line = lines[0] + ".\n\\end{frame}\n\n\\begin{frame}{" + header + "}\n" + lines[1]
                elif lines[0].strip() != "" and lines[1].strip() == "":
                    if header3 != "": line = lines[0] + ".\n\\end{frame}\n\n\\begin{frame}{" + header + "}\n\\framesubtitle{" + header3 + "}\n"
                    else: line = lines[0] + ".\n\\end{frame}\n\n\\begin{frame}{" + header + "}\n"
                linecounter = 1
            elif header3 != "Learning Objectives":
                linecounter -= 1
            openframe = 1
            slidecounter += 1
        line.replace("“",",,")
        line.replace("”","''")
        parsedline = ""
        lastletter = ""
        if (header3 == "Learning Objectives" or header3 == "Keywords") and line.strip() != "":
            line = line.strip() + "\\newline" + "\n"
        for letter in line:
            if letter == "[": ignore = 1
            if ignore != 1:
                parsedline = parsedline + lastletter
            if letter != "]": lastletter = letter
            else:
                ignore = 0
                lastletter = ""
        line = parsedline + lastletter
        if line.strip() == "":
            pass
        #else:
        #    if line.strip()[0] == "-":
        #        line = line.strip() + "\\newline\n"
        outputfile.write(line)
        poprzednialinia = line
if itemize == 1: outputfile.write("\\end{itemize}\n")
if openframe == 1:
    outputfile.write("\n\\end{frame}\n")
    openframe = 0
outputfile.close()

donotparaphraseline = 0
ignoreblock = 0
textblock = ''
justwritedamnline = 0
number_of_lines = 1

outputfile = open("preprocessed.tex", "w")
with open('content.tex') as file:
    for line in file:
        #cls()
        #sys.stdout.write("Line: %d%%   \r" % (number_of_lines))
        #sys.stdout.flush()
        number_of_lines += 1
        justwritedamnline = 1
        if line.strip() != "":
            if line.strip()[0] == "\\": donotparaphraseline = 1
            if line[0].isdigit() and (line[1] == "." or (line[0].isdigit() and line[1].isdigit() and line[2] == ".")): ignoreblock = 1
        if line.strip() == "\\framesubtitle{Keywords}" or line.strip() == "\\framesubtitle{Learning objectives}\\newline":
            ignoreblock = 1
        if not donotparaphraseline and not ignoreblock and line.strip() != "":
            textblock = textblock + " " + line.strip()
            justwritedamnline = 0
        if line.strip() == "\\end{frame}" and ignoreblock == 0:
            print("0:" + textblock)
            if textblock.strip() != "":
                paraphrased_text = paraphrase_eugene(textblock)
                print("01:" + paraphrased_text)
                print("*******************************")
                outputfile.write(paraphrased_text + "\n")
            textblock = ""
            paraphrased_text = ""
        elif line.strip() == "\\end{frame}" and ignoreblock == 1:
            ignoreblock = 0
        donotparaphraseline = 0
        if justwritedamnline:
            outputfile.write(line)
outputfile.close()