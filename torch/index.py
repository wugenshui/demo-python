import torch
import numpy as np


# 直接生成张量
data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
print(f"x_data: \n {x_data} \n")

# 通过Numpy数组来生成张量
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
print(f"x_np: \n {x_np} \n")

# 通过已有的张量来生成新的张量
x_ones = torch.ones_like(x_data)   # 保留 x_data 的属性
print(f"x_ones: \n {x_ones} \n")
x_rand = torch.rand_like(x_data, dtype=torch.float)   # 重写 x_data 的数据类型：int -> float
print(f"x_rand: \n {x_rand} \n")

# 通过指定数据维度来生成张量
shape = (2,3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)
print(f"rand_tensor: \n {rand_tensor} \n")
print(f"ones_tensor: \n {ones_tensor} \n")

print(f"Shape of tensor: {rand_tensor.shape}")
print(f"Datatype of tensor: {rand_tensor.dtype}")
print(f"Device tensor is stored on: {rand_tensor.device}")

print(torch.cuda.is_available())
# 判断当前环境GPU是否可用, 然后将tensor导入GPU内运行
if torch.cuda.is_available():
  tensor = rand_tensor.to('cuda')

print(f"Shape of tensor: {rand_tensor.shape}")
print(f"Datatype of tensor: {rand_tensor.dtype}")
print(f"Device tensor is stored on: {rand_tensor.device}")
