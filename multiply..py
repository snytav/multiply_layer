import torch
import torch.nn as nn

# https://stackoverflow.com/questions/75542366/pytorch-what-module-should-i-use-to-multiply-the-output-of-a-layer-using-seque
# https://pytorch.org/tutorials/beginner/pytorch_with_examples.html#pytorch-custom-nn-modules

class Multiply(nn.Module):
    def __init__(self, alpha):
        super().__init__()
        self.alpha =  alpha

    def forward(self, x):
        x = torch.mul(x, self.alpha)
        return x