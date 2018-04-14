#This python file is tested on version 3.5-6 

# u2800 - u283F
unibase = ['280', '281', '282', '283']
uniend = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
ordered_unicodes = [chr(int(''.join(['0x', j, i]),0)) for j in unibase for i in uniend]

# 64 symbols
brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢',
            '⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅',
            '⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵','⠪','⠳','⠻','⠘','⠸']

# corresponding unicodes for Braille symbols
unicodes = [u'\u2800',u'\u282e',u'\u2810',u'\u283c',u'\u282b',u'\u2829',u'\u282f',u'\u2804',
            u'\u2837',u'\u283e',u'\u2821',u'\u282c',u'\u2820',u'\u2824',u'\u2828',u'\u280c',
            u'\u2834',u'\u2802',u'\u2806',u'\u2812',u'\u2832',u'\u2822',u'\u2816',u'\u2836',
            u'\u2826',u'\u2814',u'\u2831',u'\u2830',u'\u2823',u'\u283f',u'\u281c',u'\u2839',
            u'\u2808',u'\u2801',u'\u2803',u'\u2809',u'\u2819',u'\u2811',u'\u280b',u'\u281b',
            u'\u2813',u'\u280a',u'\u281a',u'\u2805',u'\u2807',u'\u280d',u'\u281d',u'\u2815',
            u'\u280f',u'\u281f',u'\u2817',u'\u280e',u'\u281e',u'\u2825',u'\u2827',u'\u283a',
            u'\u282d',u'\u283d',u'\u2835',u'\u282a',u'\u2833',u'\u283b',u'\u2818',u'\u2838']


# corresponding bitwise matrix for Braille symbols
matrixcodes = [
    [[0, 0], [0, 0], [0, 0]],[[0, 1], [1, 0], [1, 1]],[[0, 0], [0, 1], [0, 0]],[[0, 1], [0, 1], [1, 1]],
    [[1, 1], [1, 0], [0, 1]],[[1, 1], [0, 0], [0, 1]],[[1, 1], [1, 0], [1, 1]],[[0, 0], [0, 0], [1, 0]],
    [[1, 0], [1, 1], [1, 1]],[[0, 1], [1, 1], [1, 1]],[[1, 0], [0, 0], [0, 1]],[[0, 1], [0, 0], [1, 1]],
    [[0, 0], [0, 0], [0, 1]],[[0, 0], [0, 0], [1, 1]],[[0, 1], [0, 0], [0, 1]],[[0, 1], [0, 0], [1, 0]],
    [[0, 0], [0, 1], [1, 1]],[[0, 0], [1, 0], [0, 0]],[[0, 0], [1, 0], [1, 0]],[[0, 0], [1, 1], [0, 0]],
    [[0, 0], [1, 1], [0, 1]],[[0, 0], [1, 0], [0, 1]],[[0, 0], [1, 1], [1, 0]],[[0, 0], [1, 1], [1, 1]],
    [[0, 0], [1, 0], [1, 1]],[[0, 0], [0, 1], [1, 0]],[[1, 0], [0, 1], [0, 1]],[[0, 0], [0, 1], [0, 1]],
    [[1, 0], [1, 0], [0, 1]],[[1, 1], [1, 1], [1, 1]],[[0, 1], [0, 1], [1, 0]],[[1, 1], [0, 1], [0, 1]],
    [[0, 1], [0, 0], [0, 0]],[[1, 0], [0, 0], [0, 0]],[[1, 0], [1, 0], [0, 0]],[[1, 1], [0, 0], [0, 0]],
    [[1, 1], [0, 1], [0, 0]],[[1, 0], [0, 1], [0, 0]],[[1, 1], [1, 0], [0, 0]],[[1, 1], [1, 1], [0, 0]],
    [[1, 0], [1, 1], [0, 0]],[[0, 1], [1, 0], [0, 0]],[[0, 1], [1, 1], [0, 0]],[[1, 0], [0, 0], [1, 0]],
    [[1, 0], [1, 0], [1, 0]],[[1, 1], [0, 0], [1, 0]],[[1, 1], [0, 1], [1, 0]],[[1, 0], [0, 1], [1, 0]],
    [[1, 1], [1, 0], [1, 0]],[[1, 1], [1, 1], [1, 0]],[[1, 0], [1, 1], [1, 0]],[[0, 1], [1, 0], [1, 0]],
    [[0, 1], [1, 1], [1, 0]],[[1, 0], [0, 0], [1, 1]],[[1, 0], [1, 0], [1, 1]],[[0, 1], [1, 1], [0, 1]],
    [[1, 1], [0, 0], [1, 1]],[[1, 1], [0, 1], [1, 1]],[[1, 0], [0, 1], [1, 1]],[[0, 1], [1, 0], [0, 1]],
    [[1, 0], [1, 1], [0, 1]],[[1, 1], [1, 1], [0, 1]],[[0, 1], [0, 1], [0, 0]],[[0, 1], [0, 1], [0, 1]]
]

# corresponding hexcodes for Braille symbols
hexbase  = ['2', '3', '4', '5']
hexend   = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
hexcodes = [''.join([j, i]) for j in hexbase for i in hexend]

# corresponding ascii codes for Braille symbols
asciicodes = [' ','!','"','#','$','%','&','','(',')','*','+',',','-','.','/',
              '0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
              'r','s','t','u','v','w','x','y','z','[','\\',']','^','_']

# corresponding dotcodes for Braille symbols
'''
dotcodes = ['','2-3-4-6','5','3-4-5-6','1-2-4-6','1-4-6','1-2-3-4-6','3','1-2-3-5-6','2-3-4-5-6','1-6','3-4-6','6','3-6','4-6',
            '3-4','3-5-6','2','2-3','2-5','2-5-6','2-6','2-3-5','2-3-5-6','2-3-6','3-5','1-5-6','5-6','1-2-6','1-2-3-4-5-6',
            '3-4-5','1-4-5-6','4','1','1-2','1-4','1-4-5','1-5','1-2-4','1-2-4-5','1-2-5','2-4','2-4-5','1-3','1-2-3','1-3-4',
            '1-3-4-5','1-3-5','1-2-3-4','1-2-3-4-5','1-2-3-5','2-3-4','2-3-4-5','1-3-6','1-2-3-6','2-4-5-6','1-3-4-6','1-3-4-5-6',
            '1-3-5-6','2-4-6','1-2-5-6','1-2-4-5-6','4-5','4-5-6']
'''
dotcodes = ['','2346','5','3456','1246','146','12346','3','12356','23456','16','346','6','36','46',
            '34','356','2','23','25','256','26','235','2356','236','35','156','56','126','123456',
            '345','1456','4','1','12','14','145','15','124','1245','125','24','245','13','123','134',
            '1345','135','1234','12345','1235','234','2345','136','1236','2456','1346','13456',
            '1356','246','1256','12456','45','456']
# corresponding letter/word combinations for Braille symbols
meanings = ['(space)','the','(contraction)','(number prefix)','ed','sh','and','(undefined)','of','with','ch','ing','(uppercase prefix)','-',
            '(italic prefix)','st','”',',',';',':','.','en','!','( or )','“ or ?','in','wh','(letter prefix)','gh','for','ar','th',
            '(accent prefix)','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'ow','ou','er','(currency prefix)','(contraction)']

# corresponding word combinations for Braille symbols
words = ['','THE','','','','SHALL','AND','','OF','WITH','CHILD','ING','','','','STILL','WAS','','BE','','','ENOUGH','TO','WERE','HIS',
         'IN','WHICH','','','FOR','','THIS','','','BUT','CAN','DO','EVERY','FROM','GO','HAVE','','JUST','KNOWLEDGE','LIKE','MORE','NOT',
         '','PEOPLE','QUITE','RATHER','SO','THAT','US','VERY','WILL','IT','YOU','AS','','OUT','','','']

# todo: decoded strings of possible translations of Braille symbols
# this can be improved for more robust and clever way to translating
# grade 2 Braille input to human eye readable sentences
decodings = ['SPACE/empty','THE/5-there/4-5-these/4-5-6-their','5-','ble/#','ed','sh/SHALL','AND','3-','OF','WITH','ch/CHILD/5-character',
             'ing','6-','com/-','4-6-','st/STILL','was/BY/”','ea/,','be/bb/;','con/cc/:','dis/dd/.','en/ENOUGH','to/ff/!','were/gg/()',
             'his/?/“','in','wh/WHICH/5-where/4-5-whose','5-6-','gh/RELEASE CAPS/<','FOR/full','ar','th/THIS/5-through/4-5-those','´/@',
             'a/1','b/BUT/2','c/CAN/4-5-6-cannot/3','d/DO/5-day/4-6-ound/4','e/EVERY/5-ever/4-6-ance/5-6-ence/5','f/FROM/5-father/6',
             'g/GO/5-6-ong/7','h/HAVE/5-here/4-5-6-had/8','i/9','j/JUST/0','k/KNOWLEDGE/5-know','l/LIKE/5-lord/5-6-ful/RELEASE',
             'm/MORE/5-mother/4-5-6-many','n/NOT/5-name/4-6-sion/5-6-tion/6-ation','o/5-one','p/PEOPLE/5-part','q/QUITE/5-question',
             'r/RATHER/5-right','s/SO/5-some/4-5-6-spirit/4-6-less/5-6-ness','t/THAT/5-time/4-6-ount/5-6-ment','u/US/5-under/4-5-upon',
             'v/VERY','w/WILL/5-work/4-5-word/4-5-6-world','x/IT','y/YOU/5-young/5-6-ity/6-ally/','z/AS','ow','ou/OUT/5-ought','er',
             '4-5- ','4-5-6-']

def convert(string, toNotation, fromNotation):
    return [toNotation[fromNotation.index(d)] for c in string for d in fromNotation if c == d]

# ascii to braille. currently supporting grade 1 conversion only
# you should use convert function to find out possible translations for braille code:
# convert("⠏⠽⠃⠗⠁⠊⠇⠇⠑⠀⠊⠎⠀⠉⠕⠕⠇⠮", meanings, brailles) OR
# convert("⠏⠽⠃⠗⠁⠊⠇⠇⠑⠀⠊⠎⠀⠉⠕⠕⠇⠮", words, brailles) OR
# convert("⠏⠽⠃⠗⠁⠊⠇⠇⠑⠀⠊⠎⠀⠉⠕⠕⠇⠮", decodings, brailles)
def braille(string):
    return ''.join(convert(string, brailles, asciicodes))

def braille2(string):
    return "Grade 2 conversion not supported yet. you should use convert function to find out translation possibilities for Grade 2."

# braille to ascii
def ascii(string):
    return ''.join(convert(string, asciicodes, brailles))

# braille to matrix
def matrix(string):
    return convert(string, matrixcodes, brailles)

# braille to hex
def hex(string):
    return convert(string, hexcodes, brailles)

# braille to dot
def dot(string):
    return convert(string, dotcodes, brailles)

# helper function for n2braille
# these functions differs from ascii, matrix, hex and dot by taking
# an array of items instead of a string
def convert_list(arr, toNotation, fromNotation):
    return [toNotation[fromNotation.index(c)] for c in arr]

# matrix to braille
def matrix2braille(arr):
    return ''.join(convert_list(arr, brailles, matrixcodes))

# hex to braille
def hex2braille(arr):
    return ''.join(convert_list(arr, brailles, hexcodes))

# dot to braille
def dot2braille(arr):
    return ''.join(convert_list(arr, brailles, dotcodes))


def fn(s):
    #print(s)
    bral = braille(s)
    #print(bral)
    dawt = (dot(bral))
    try:
        dawt1 = str(dawt[0])
    except IndexError:
        dawt1 = '0'

    #print(dawt1)

    st0 = ''
    st1 = ''
    for i in range(1, 7):
        if dawt1=='0':
            st0='000000'
            break
        if str(i) in dawt1 and dawt1 != 0:

            st0 += '1'
        else:
            st0 += '0'
    #print(st0)
    gar= (int(st0, 2))
    time.sleep(0.005)
    print(gar)
    ser.write(str(int(st0, 2)).encode())
    if len(dawt)>=1:
        try:
            dawt2 = str(dawt[1])
        except IndexError:
            dawt2 = '0'

        #print(dawt2)

        for i in range(1, 7):
            if dawt2 == '0':
                st1 = '000000'
                break
            if str(i) in dawt2 and dawt2 != 0:

                st1 += '1'
            else:
                st1 += '0'
        #print(int(st1, 2))





import cv2
import sys
import numpy as np
import pytesseract
import serial
import time
ser=serial.Serial('COM43',9600)
#ser.open()

cap=cv2.VideoCapture('vid.mp4')

while True:
    ret,img=cap.read()
    #ser.close()

    #img = cv2.imread('card.png')
    img = img[70:300, 300:500]

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
    # ret,threshold = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # threshold = cv2.adaptiveThreshold(image,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,1)
    img=cv2.medianBlur(img,15)
    img=cv2.GaussianBlur(img,(15,15),0)

    height = np.size(img, 0)
    width = np.size(img, 1)

    text = pytesseract.image_to_string(img, lang="eng")
    text = text[0:2]
    if len(text)>0:
        fn(text)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
