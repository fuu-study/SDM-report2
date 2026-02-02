#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('^[0-9]+$') # 整数のみを許可する正規表現に変更 (小数点を含まない)
        if p.match(ai) and p.match(bi): # or ではなく and にして両方が整数であることを確認
                a=float(ai)
                b=float(bi)
                if 1 <= a <= 999 and 1 <= b <= 999: # 1以上999以下を判定
                        valid=True
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return int(ans) # 整数として返す
        else:
                return -1
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
