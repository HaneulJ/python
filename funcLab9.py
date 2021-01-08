"""함수명 : sumEven1
   매개변수 : 가변형(전달받을 수 있는 아규먼트 개수에 제한이 없다.)
   리턴값 : 1개
   기능 : 아규먼트가 몇 개가 전달되든 처리해야 한다.
         아규먼트는 1 이상의 숫자만 온다고 정한다.
         전달된 아규먼트들에서 짝수에 해당하는 숫자들만 합을 계산해서 리턴한다.
         전달된 아규먼트들 중에 짝수가 없으면 0을 리턴한다.
         아규먼트가 전달되지 않으면 -1을 리턴한다.
"""
def sumEven1(*n):
    for n in range(1,):
        sum = 0
        if n % 2 ==0:
            sum += n
            return sum
        else: return 0
    if n in None:
        return -1