import torch


def sigm(x):
    return 1 / (1 + torch.exp(-x))


torch.manual_seed(7)
inputs = torch.randn((1, 10), requires_grad=True)
w1 = torch.randn((10, 1), requires_grad=True)
b1 = torch.randn((1, 1), requires_grad=True)
output = sigm(torch.matmul(inputs, w1) + b1)
print(output)
output.backward()
print(w1.grad)
print(b1)
print(b1.grad)
