print('WELCOME TO MY FIRST QUIZE GAME')
ans=input('what does CPU stand for? ').lower()
score=0
if ans=='central processing unit':
    print('Correct..')
    score+=1
else:
    print('Incorrect..')
ans=input('what does PC stand for? ').lower()
if ans=='personal computer':
    print('Correct..')
    score += 1
else:
    print('Incorrect..')
ans=input('what does PSU stand for? ').lower()
if ans=='power supply':
    print('Correct..')
    score += 1
else:
    print('Incorrect..')
ans=input('what does CA stand for? ').lower()
if ans=='charted account':
    print('Correct..')
    score += 1
else:
    print('Incorrect..')
print('you answer correctly for '+str(score)+' question')
print('note:for one correct answer you can get 10 point')
print('you got '+str(score*10)+' point')
