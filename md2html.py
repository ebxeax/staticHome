import markdown
import os
import sys


def md2html(mdstr):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

    html = '''
    <html lang="zh-cn">
    <head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type" />
    <link href="css/default.css" rel="stylesheet">
    <link href="css/github.css" rel="stylesheet">
    </head>
    <body>
    %s
    </body>
    </html>
    '''

    ret = markdown.markdown(mdstr,extensions=exts)
    return html % ret

def get_from_argv():
    if len(sys.argv) < 3:
        print('usage: md2html.py [source_filename] [target_file]')
        sys.exit()
    infile = open(sys.argv[1],'r')
    md = infile.read()
    infile.close()
    if os.path.exists(sys.argv[2]):
        os.remove(sys.argv[2])
    outfile = open(sys.argv[2],'a')
    outfile.write(md2html(md))
    outfile.close()
    print('convert %s to %s success!'%(sys.argv[1],sys.argv[2]))

if __name__ == '__main__':

    root = './_src/'
    des = './_posts/'
    dir = os.listdir(path = root)
    ll = []
    for i in dir:
        if i.split(sep = '.')[1] == 'md':
            ll.append(i)
    for i in ll:
        oldfile = root + i
        newfile = des + i.split('.')[0] + '.html'
        print(oldfile)
        print(newfile)
        infile = open(oldfile, 'r')
        md = infile.read()
        infile.close()
        outfile = open(newfile ,'w')
        outfile.write(md2html(md))
        outfile.close()