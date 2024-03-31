import sys

#入力を受け取る
args = sys.argv

if args[1] == "copy":
    # TODO Try
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
    
    
