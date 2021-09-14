import torch

torch_array = torch.rand((3, 3), requires_grad=True)
t = torch_array ** 2
t.backward(torch.ones_like(torch_array))

print(torch_array)
print(torch_array.grad)

