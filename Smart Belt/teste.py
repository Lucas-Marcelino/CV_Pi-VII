from timer import TicToc

TicToc = TicToc(5)
input()
TicToc.setToc()
input()
TicToc.setTic()
print(TicToc.diff())
print(TicToc.canScore())