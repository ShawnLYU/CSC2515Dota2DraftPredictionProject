import torch
import numpy as np

from torch.autograd import Variable

import torch.nn.functional as F

class Net_1(torch.nn.Module):
    def __init__(self, n_feature, n_output):
        super(Net_1, self).__init__()
        self.fc = torch.nn.Sequential(
            torch.nn.Linear(n_feature, 100),
            torch.nn.ReLU(True),
            torch.nn.Linear(100, n_output)
            )
    def forward(self, x):
        x = self.fc.forward(x)
        return x

class Net_2(torch.nn.Module):
    def __init__(self, n_feature, n_output):
        super(Net_2, self).__init__()
        self.fc = torch.nn.Sequential(
            torch.nn.Linear(n_feature, 100),
            torch.nn.Dropout(0.5),
            torch.nn.ReLU(True),
            torch.nn.Linear(100, n_output)
            )
    def forward(self, x):
        x = self.fc.forward(x)
        return x


class Net_3(torch.nn.Module):
    def __init__(self, n_feature, n_output):
        super(Net_3, self).__init__()
        self.fc = torch.nn.Sequential(
            torch.nn.Linear(n_feature, 160),
            torch.nn.ReLU(True),
            torch.nn.Linear(160, 100),
            torch.nn.ReLU(True),
            torch.nn.Linear(100, n_output)
            )
    def forward(self, x):
        x = self.fc.forward(x)
        return x

class Net_4(torch.nn.Module):
    def __init__(self, n_feature, n_output):
        super(Net_4, self).__init__()
        self.fc = torch.nn.Sequential(
            torch.nn.Linear(n_feature, 160),
            torch.nn.Dropout(0.5),
            torch.nn.ReLU(True),
            torch.nn.Linear(160, 100),
            torch.nn.Dropout(0.5),
            torch.nn.ReLU(True),
            torch.nn.Linear(100, n_output)
            )
    def forward(self, x):
        x = self.fc.forward(x)
        return x

class Net_5(torch.nn.Module):
    def __init__(self, n_feature, n_output):
        super(Net_5, self).__init__()
        self.fc = torch.nn.Sequential(
            torch.nn.Linear(n_feature, 160),
            torch.nn.ReLU(True),
            torch.nn.Linear(160, 100),
            torch.nn.ReLU(True),
            torch.nn.Linear(100, 20),
            torch.nn.ReLU(True),
            torch.nn.Linear(20, n_output)
            )
    def forward(self, x):
        x = self.fc.forward(x)
        return x

class Net_6(torch.nn.Module):
    def __init__(self, n_feature, n_output):
        super(Net_6, self).__init__()
        self.fc = torch.nn.Sequential(
            torch.nn.Linear(n_feature, 160),
            torch.nn.Dropout(0.5),
            torch.nn.ReLU(True),
            torch.nn.Linear(160, 100),
            torch.nn.Dropout(0.5),
            torch.nn.ReLU(True),
            torch.nn.Linear(100, 20),
            torch.nn.Dropout(0.5),
            torch.nn.ReLU(True),
            torch.nn.Linear(20, n_output)
            )
    def forward(self, x):
        x = self.fc.forward(x)
        return x
