import sys

#入力を受け取る
args = sys.argv

if args[1] == "copy":

    #TODO try文の重複をwith句で定義 
    #TODO バリデータ
    #TODO 機能的には出来ているがめちゃめちゃ汚い
    try:
        inputPath = args[2]
        ifile = open(inputPath)
        iStr = ifile.read()
        ifile = close()
    except:
        print('コピー元が入力されていない。もしくは存在しません')

    try:
        outputPath = args[3]
        ofile = open(outputPath,'w',encoding='utf-8')
        ofile.write(iStr)
        ofile.close()
    except:
        print('コピー先が入力されていません。')

if args[1] == "reverse":

    try:
        inputPath = args[2]
        ifile = open(inputPath)
        iStr = ifile.read()
        print(iStr[0])
        ifile.close()
    except:
        print('コピー元が入力されていない。もしくは存在しません')
    
    try:
        outputPath = args[3]
        ofile = open(outputPath,'w',encoding='utf-8')
        for i in range(len(iStr)):
            ofile.write(iStr[len(iStr)-i-1])
        
        ofile.close()
    except:
        print('コピー先が入力されていません。')

if args[1] == "duplicate-contents":

    inputPath = args[2]
    ifile = open(inputPath)
    iStr = ifile.read()
    ifile.close()
    
    ifile2 = open(inputPath,'a')

    try:
        inputNumber = int(args[3])
    except:
        print('複製回数が入力されていません')
    
    for i in range(inputNumber):
        ifile2.write(f'{iStr}')
    
    ifile2.close()

if args[1] == "replace-string":

    inputPath = args[2]
    ifile = open(inputPath)
    iStr = ifile.read()
    ifile.close()

    replaceString = args[3]
    replaceToString = args[4]

    newIStr = iStr.replace(replaceString, replaceString)

    ifile2 = open(inputPath,'w')

    ifile2.write(newIStr)

    ifile2.close()




    

    
