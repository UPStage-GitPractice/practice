#fizz Buzz program

for i in range(1, 16+1):
  if i%15==0:
        print('fizzbuzz')
  elif i%3==0:
        print("fizz")
  elif i % 5 == 0:
        print('buzz')
  else:
        print(i)


res = ['fizzbuzz' if i%15==0 else 'fizz' if i%3==0 else 'buzz' if i%5==0 else i for i in range(1, 16+1)]
print(res)
