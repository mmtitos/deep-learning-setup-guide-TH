import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader


transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # <-- Esto es razonable para imágenes RGB, no tanto para MNIST
])


train_loader = DataLoader(
    datasets.MNIST('.', train=True, download=True, transform=transform),
    batch_size=10000, shuffle=True
)


class BadNet(nn.Module):
    def __init__(self):
        super(BadNet, self).__init__()
        self.fc1 = nn.Linear(28*28, 10)  # <-- Sin capa oculta
    def forward(self, x):
        x = x.view(-1, 28*28)
        return self.fc1(x)  # <-- Sin activación no lineal

model = BadNet()


criterion = nn.MSELoss() 
optimizer = optim.SGD(model.parameters(), lr=0.1)


for epoch in range(1):
    for data, target in train_loader:
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target.float())  
        loss.backward()
        optimizer.step()
    print(f"Loss: {loss.item()}")

print("Entrenamiento completado.")
