# -*- coding: cp936 -*-
import docx
document =docx.Document(r'E:\�����ĵ�\20171101��������\���ĳ��̿ͻ�������20171110.docx')
#��ȡ��������
docText='\n\n'.join([paragraph.text.encode('cp936') for paragraph in document.paragraphs])
#��ȡ�������
exlText= r' '.join(
[cell.text
    for table in document.tables
        for row in table.rows
            for cell in row.cells
])
print exlText
print docText
