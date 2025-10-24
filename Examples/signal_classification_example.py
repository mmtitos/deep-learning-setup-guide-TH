
# Simple example: recognize if a sound is "voice" or "noise"

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

# 1. Create fake data (simulate short audio signals)
# "Voice": smooth sinusoidal waves
# "Noise": random values

def generate_data(n_samples=200, n_points=100):
    X, y = [], []
    for _ in range(n_samples):
        if np.random.rand() > 0.5:
            freq = np.random.uniform(2, 6)
            signal = np.sin(np.linspace(0, freq * np.pi, n_points)) + 0.1*np.random.randn(n_points)
            label = 1  # voice
        else:
            signal = np.random.randn(n_points)
            label = 0  # noise
        X.append(signal)
        y.append(label)
    return np.array(X, dtype=np.float32), np.array(y, dtype=np.int64)
  
# 2. Check fake data (simulate short audio signals)
# "Voice": smooth sinusoidal waves
# "Noise": random values

X, y = generate_data()
plt.plot(X[0])
plt.title("Example of generated signal")
plt.show()

# Convert to tensors (mandatory to use GPU)
X_tensor = torch.tensor(X)
y_tensor = torch.tensor(y)

# 3. Define a very simple neural network

#simple neural network (MLP) with only one hidden layer

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(100, 32)
        self.fc2 = nn.Linear(32, 2)  # 2 classes: noise / voice
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

model = SimpleNet()

#define the loss function for training the network
criterion = nn.CrossEntropyLoss()

#define the optimization method
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 4. Train the model

for epoch in range(50):
    optimizer.zero_grad()
    outputs = model(X_tensor)
    loss = criterion(outputs, y_tensor)
    loss.backward()
    optimizer.step()
    if (epoch+1) % 10 == 0:
        print(f"Epoch {epoch+1}: Loss = {loss.item():.4f}")

# 5. Test the model

with torch.no_grad():
    preds = torch.argmax(model(X_tensor), dim=1)
    acc = (preds == y_tensor).float().mean()
    print(f"\n Accuracy on synthetic data: {acc.item()*100:.1f}%")

# 6.  Try a new signal
test_voice = np.sin(np.linspace(0, 3*np.pi, 100)) + 0.1*np.random.randn(100)
test_noise = np.random.randn(100)

def predict(signal):
    x = torch.tensor(signal, dtype=torch.float32).unsqueeze(0)
    y_pred = torch.argmax(model(x)).item()
    label = "VOICE" if y_pred == 1 else "NOISE"
    print(f"Prediction: {label}")
    plt.plot(signal)
    plt.title(label)
    plt.show()

print("\n Testing on new samples:")
predict(test_voice)
predict(test_noise)
