import sys

#入力を受け取る
args = sys.argv

if args[1] == "copy":

    #TODO try文の重複をwith句で定義
    try:
        inputPath = args[2]
        ifile = open(inputPath)
        iStr = ifile.read()
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

    
    
