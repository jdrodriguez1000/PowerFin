
import zipfile
import xml.etree.ElementTree as ET
import os

def get_docx_text(path):
    try:
        with zipfile.ZipFile(path) as z:
            xml_content = z.read('word/document.xml')
        
        tree = ET.fromstring(xml_content)
        # Handle all possible namespaces found in docx
        ns = {
            'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
            'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
            'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
            'v': 'urn:schemas-microsoft-com:vml',
            'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math'
        }
        
        paragraphs = []
        for paragraph in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            texts = []
            for text_node in paragraph.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                if text_node.text:
                    texts.append(text_node.text)
            if texts:
                paragraphs.append("".join(texts))
        
        return "\n".join(paragraphs)
    except Exception as e:
        return f"Error: {e}"

path = r'c:\Users\USUARIO\Documents\Proyectos\FinancApp\PRD.docx'
output_path = r'c:\Users\USUARIO\Documents\Proyectos\FinancApp\prd_extracted.txt'
if os.path.exists(path):
    text = get_docx_text(path)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Extracted to {output_path}")
else:
    print(f"File not found: {path}")
