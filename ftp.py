import ftplib

ftp = ftplib.FTP("bighome.iitb.ac.in")
ftp.login("gpatil", "belgaum!")
print(ftp.getwelcome())
data = []
#ftp.cwd("../public_html")
print(ftp.pwd())
ftp.dir(data.append)

ftp.quit()
ftp.close()
for line in data:
    print (line)
