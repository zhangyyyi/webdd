#!/usr/bin/env python
#coding=utf-8
"""A more advanced Mapper, using Python iterators and generators."""

import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')


def read_input(file):
    for line in file:
        # split the line into words
        yield line.split(",")


def findSubstrings(substrings, destString):
    res = filter(lambda x: x in destString, substrings)
    #if res:
        #return ', '.join(list(res))
    return len(res)


def is_valid_date(str):
  '''判断是否是一个有效的日期字符串'''
  try:
    time.strptime(str, "%Y-%m-%d")
    return True
  except:
    return False


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
    for words in data:
        #index range limit
        if len(words) > 1:
            #head = words[7][12:-1]
            id = 0
            username = ''
            date = ''
            brower = ''
            system = ''
            screen = ''
            #print head
            if words[-1].find('userScreen') != -1:
                date = words[-6][15:25]

                brower = words[-3].find('null') == -1 and words[-3][14:-1] or words[-3][13:]
                #brower = words[-3][13:]
                system = words[-4].find('null') == -1 and words[-4][17:-1] or words[-4][16:]
                #if words[-1].find('null') == -1:
                    #screen = words[-1][14:-3]
                screen = words[-1].find('null') == -1 and words[-1][14:-3] or words[-1][13:-2]
                #print brower

            elif words[-2].find('null') == -1 and words[-3].find('null') == -1 and \
                len(words[-2]) < 40 and len(words[-3]) < 40 :#exclude invalid data
                date = words[-5][15:25]
                brower = words[-2].find('null') == -1 and words[-2][14:-1] or words[-3][13:]
                # brower = words[-3][13:]
                system = words[-3].find('null') == -1 and words[-3][17:-1] or words[-4][16:]



            id = words[0][7:-1]
            username = words[5][12:-1]

            if findSubstrings([' ', '　','\t'], username) == 0 and \
                len(username) > 0 and len(username) < 200 and \
                len(id) < 10 and len(id) > 0 and \
                is_valid_date(date) == True:#用户未登录记为空 账号不含空格
                #用户信息：id,username,brower,system,screen,date
                userInfo = ','.join([id, username, brower, system, screen, date])

                print '%s%s%d' % (userInfo, separator, 1)\
                 #int(words[3].decode('utf-8')[4:]))

if __name__ == "__main__":
    main()
