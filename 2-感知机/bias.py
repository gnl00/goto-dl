# y = x1*w1 + x2*w2 + b > 0 ?
import numpy as np
x = np.array([0, 1]) # 输入 x0=0 x1=1
w = np.array([0.5, 0.5]) # 权重 w0 w1
b = -0.7 # bias
print(x * w) # numpy 数组对应位置相乘
print(b + np.sum(x * w)) # numpy 数组对应位置相乘再求和，最后加上偏移量

def and_gate(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7
  result = np.sum(x * w) + b
  return 1 if result > 0 else 0

def nand_gate(x1, x2):
  x = np.array([x1, x2])
  w = np.array([-0.5, -0.5]) # 与非门的权重与偏移量和与门不同
  b = 0.7
  result = np.sum(x * w) + b
  return 1 if result > 0 else 0

def or_gate(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5]) # 或门、与门、与非门的本质不同仅在偏移量和权重上有所不同
  b = -0.2
  result = np.sum(x * w) + b
  return 1 if result > 0 else 0


def xor(x1, x2):
  s1 = nand_gate(x1, x2)
  s2 = or_gate(x1, x2)
  result = and_gate(s1, s2)
  return result

print(xor(0, 0))
print(xor(0, 1))
print(xor(1, 0))
print(xor(1, 1))