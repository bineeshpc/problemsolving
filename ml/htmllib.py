import HTML

infile = 'ids.txt'
outfile = 'profiles.txt'


def getprofile(numid):
    profileurl = "http://profile.keralamatrimony.com/profiledetail/viewprofile.php?id={}&gaact=SID&gasrc=SRCH"
    numid = numid.strip()
    if numid[0] != 'E':
        fullid = 'E{}'.format(numid)
    else:
        fullid = numid
    purl = profileurl.format(fullid)
    #outline = "{},{},\n".format(fullid, purl)
    return fullid, purl

inf = open(infile)
#ouf = open(outfile, 'a')

def makehtml(data):
    return """<html>
           {}
           </html>""".format(data)

def maketable():
    header_row = ['id',   'Details']
    table_data = []
    for line in inf:
       fullid, purl = getprofile(line)
       idlink = """<a href="{}" target="_blank">{}</a>""".format(purl, fullid)
       table_data.append([idlink, "test"])
    return HTML.table(table_data)

#    ouf.write(outline)

print makehtml(maketable())
