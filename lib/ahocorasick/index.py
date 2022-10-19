# https://pypi.org/project/pyahocorasick/
import ahocorasick

a = ["你好", "再见", "拜拜"]
b = ["开心", "高兴", "快乐"]
region = set(a+b)
print(region)


actree = ahocorasick.Automaton()
for index, word in enumerate(region):
    actree.add_word(word, (index, word))
actree.make_automaton()

for i in actree.iter("我真的好开心啊，拜拜!"):
  print(i)
  print(i[1][1])
