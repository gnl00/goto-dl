# 与门
def and_gate(x1, x2):
  w1, w2, theta = 0.5, 0.5, 0.7
  return  1 if w1*x1 + w2*x2 > theta else 0

print(and_gate(0, 0))
print(and_gate(0, 1))
print(and_gate(1, 0))
print(and_gate(1, 1))


