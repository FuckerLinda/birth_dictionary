import sys
import getopt

#mod=1:19990303
#mod=2:1999-03-03
#mod=3:1999/03/03
#mod=4:1999-3-3
#mod=5:1999/3/3

#把年月日写入f,同时根据模式mod生成不同结果
def write(f,year,mon,day,mod):
    #年
    f.write(str(year))
    if (mod==1 or mod==2 or mod==3):
        if mod==2:
            f.write("-")
        if mod==3:
            f.write("/")
        #月
        if mon > 9:
            f.write(str(mon))
        else:
            f.write("0" + str(mon))
        if mod==2:
            f.write("-")
        if mod==3:
            f.write("/")
        #日
        if day > 9:
            f.write(str(day))
        else:
            f.write("0" + str(day))
    if (mod==4 or mod==5):
        if mod==4:
            f.write("-")
        if mod==5:
            f.write("/")
        f.write(str(mon))
        if mod==4:
            f.write("-")
        if mod==5:
            f.write("/")
        f.write(str(day))

    f.write("\n")



#年月日进位,同时根据模式mod生成不同结果
def increase(f,year,mon,day,mod):
    # 2月
    if mon == 2:
        # 若逆推是闰年29
        if day == 30:
            mon = 3
            day = 1
        # 若逆推是平年28
        if day == 29 and not ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            mon = 3
            day = 1
    # 不然若逆推是30天
    elif (day == 31):
        if (mon in [4, 6, 9, 11]):
            mon += 1
            day = 1
    elif (day == 32):
        mon += 1
        day = 1
    if mon == 13:
        year += 1
        mon = 1
    write(f, year, mon, day,mod)

    return year,mon,day





"""
birth -m(mode) 4 20020203 19981107

"""

def mode(begin,end,mod):
    begin = list(map(int, begin))
    end = list(map(int, end))
    f=open("birth.txt","w")

    year=1000*begin[0]+100*begin[1]+10*begin[2]+begin[3]
    mon=10*begin[4]+begin[5]
    day=10*begin[6]+begin[7]

    year2 = 1000 * end[0] + 100 * end[1] + 10 * end[2] + end[3]
    mon2 = 10 * end[4] + end[5]
    day2 = 10 * end[6] + end[7]

    write(f, year, mon, day,mod)

    while(year!=year2 or mon!=mon2 or day!=day2):
        day+=1
        year,mon,day=increase(f,year,mon,day,mod)

    f.close()
"""

def main():
    mode("20200203","20261227",5)

"""

def to_help():
    print('\n[1]use "-h" for help\n'
          '[2]use "-mx" to set mode, and it should follow with yyyymmdd yyyymmdd\n'
          '"x" is number.\n'
          '"yyyymmdd":the first is Start Date and the second is End Date\n'
          'x=1, output YYYYMMDD\n'
          'x=2, output YYYY-MM-DD\n'
          'x=3, output YYYY/MM/DD\n'
          'x=4, output YYYY-M-D\n'
          'x=5, output YYYY/M/D\n'
          'for example,use "python3 birth.py -m2 20000102 20200102, and it output a dictionary named "birth.txt". It ranges from 2000-01-02 to 2020-01-02\n')



def happy_birth_day(args,arg):
    print("\nexecute...")
    print(
        "\n            iiiiiiiiiii"
        '\n           |:H:a:p:p:y:|'
        '\n         __|___________|__'
        '\n        |^^^^^^^^^^^^^^^^^|'
        "\n        |:B:i:r:t:h:d:a:y:|")
    mode(args[0], args[1], int(arg))
    print("===========!!!success!!!============\n")


#birth.py -h -m5 19990101 20210101
def main(argv):
    #有参
    if len(sys.argv) > 1:
        mod=1;
        #参数输入
        try:
            opts, args = getopt.getopt(argv, "hm:")
        #无参时
        except getopt.GetoptError:
            to_help()
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                to_help()
                exit()
            if opt == '-m':
                happy_birth_day(args,arg)
                exit()

    #无参打印
    else:
        to_help()


if __name__=='__main__':
    main(sys.argv[1:])