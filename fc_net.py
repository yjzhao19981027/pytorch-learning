import torch
import torch.nn as nn


class FC_Net(nn.Module):
    def __init__(self):
        super(FC_Net, self).__init__()
        self.fc1 = nn.Linear(10, 20)
        self.fc2 = nn.Linear(20, 20)
        self.out = nn.Linear(20, 10)


    def forward(self, x):
        hidden1 = self.fc1(x)
        hidden2 = self.fc2(hidden1)
        output = self.out(hidden2)
        return output


input_layer = torch.rand(10)
net = FC_Net()
result = net.forward(input_layer)
print(result)
