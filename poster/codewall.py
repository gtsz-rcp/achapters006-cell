import sys
import re
from xml.etree.ElementTree import Element, dump, ElementTree

def get_tex(filepath):
    with open(filepath, encoding='utf-8') as filedata:
        return filedata.read()
    return False

def find_command(line):
    r = re.compile(r'(\\[a-z]+)')
    if r.match(line):
        line = r.sub(r'<code>\g<1></code>', line)
        print(line)
    return line

if __name__ == '__main__':
    tex = get_tex('../tex/cell.master.tex')
    lines = tex.split('\n')
    xml = Element('root')
    doc = Element('doc')
    for line in lines:
        el = Element('line')
        find_command(line)
        el.text = line
        doc.append(el)
    
    xml.append(doc)
    ElementTree(xml).write("codewall.xml", encoding='utf-8', xml_declaration=True)