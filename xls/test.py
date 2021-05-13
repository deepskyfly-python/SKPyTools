import xlrd
import xlwt
import re
import sys


#     打开excel
# readbook = xlrd.open_workbook(r‘\test\canying.xlsx‘)

#     2、获取读入的文件的sheet
# sheet = readbook.sheet_by_index(1)#索引的方式，从0开始
# sheet = readbook.sheet_by_name(‘sheet2‘)#名字的方式

# 　　3、获取sheet的最大行数和列数
# nrows = sheet.nrows#行
# ncols = sheet.ncols#列

#　　4、获取某个单元格的值
# lng = table.cell(i,3).value#获取i行3列的表格值
# lat = table.cell(i,4).value#获取i行4列的表格值

#　　5、打开将写的表并添加sheet
# writebook = xlwt.Workbook()#打开一个excel
# sheet = writebook.add_sheet('test')#在打开的excel中添加一个sheet

#　　6、将数据写入excel
# sheet.write(i,0,result[0])#写入excel，i行0列
# sheet.write(i,1,result[1])

#　　7、保存
# writebook.save('answer.xls')#一定要记得保存

filePath = sys.path[0]+"\\英语单词.xlsx"

workbook = xlrd.open_workbook(filePath)
sheet = workbook.sheet_by_name("英语单词")
nrows = sheet.nrows

writebook = xlwt.Workbook()#打开一个excel
wsheet = writebook.add_sheet('word')

wordLink = ''
writeRowId = 0
for i in range(nrows):
    if i > 0:
        rList = sheet.row(i)
        if rList[len(rList)-1].value != '':
            wordLink = rList[len(rList)-1].value            

        for j in rList:
            if j.value != '':
                word = j.value
                # print(word)
                if isinstance(word,str) and word != 'Subtopic' and re.search("^[A-Za-z]+$",word):
                    wsheet.write(writeRowId,0,word)#写入excel，i行0列
                    wsheet.write(writeRowId,1,wordLink)
                    writeRowId +=1

writebook.save('wordBiliExplain.xls')        