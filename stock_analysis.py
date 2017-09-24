


def main():

    import commands
    import os

    #Get the script numbers and put is a temp file
    oscom = 'awk \'{print $1}\' LIST'
    stock_ref = commands.getoutput(oscom)
    workdir = commands.getoutput('pwd')
    fname = workdir + '/temp.txt'
    f = open(fname,'w')
    f.write(stock_ref)
    f.close()

    #Use data from tempfile and create full URLs
    tempfile = open(fname)
    fname = workdir + '/url_list.txt'
    g = open(fname,'w')
    for line in tempfile:
        script_no = line[0:6]
        g.write('http://www.bseindia.com/stock-share-price/stockreach_financials.aspx?scripcode=' + script_no + '&expandable=0\n')
    g.close()
    	
    os.system('rm temp.txt')




main()
