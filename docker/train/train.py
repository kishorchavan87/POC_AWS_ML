import pandas as pd
import torch
from torch import nn, optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Fake dataset example
df = pd.read_csv("/app/data/clean_data.csv")
X = torch.tensor(df.iloc[:,1:].values, dtype=torch.float32)
y = LabelEncoder().fit_transform(df.iloc[:,0].values)
y = torch.tensor(y, dtype=torch.long)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = nn.Sequential(
    nn.Linear(X.shape[1], 16),
    nn.ReLU(),
    nn.Linear(16, len(set(y.tolist())))
)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

for epoch in range(5):
    optimizer.zero_grad()
    out = model(X_train)
    loss = criterion(out, y_train)
    loss.backward()
    optimizer.step()

torch.save(model.state_dict(), "/app/data/model.pt")
print("Model trained and saved")
