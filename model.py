import torch
import torch.nn as nn

class RNNModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers):
        super(RNNModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.lstm(x)
        
        # If out is a 3D tensor, use the final time step's output
        if len(out.shape) == 3:
            out = self.fc(out[:, -1, :])
        else:
            out = self.fc(out)  # If out is 2D, use the entire sequence's output
        
        return out
