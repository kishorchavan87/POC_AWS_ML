import torch
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from torch import nn

df = pd.read_csv("/app/data/clean_data.csv")
X = torch.tensor(df.iloc[:,1:].values, dtype=torch.float32)
y = LabelEncoder().fit_transform(df.iloc[:,0].values)
y = torch.tensor(y, dtype=torch.long)

_, X_test, _, y_test = train_test_split(X, y, test_size=0.2)

model = nn.Sequential(
    nn.Linear(X.shape[1], 16),
    nn.ReLU(),
    nn.Linear(16, len(set(y.tolist())))
)
model.load_state_dict(torch.load("/app/data/model.pt"))

with torch.no_grad():
    preds = model(X_test).argmax(1)
    acc = (preds == y_test).float().mean().item()

with open("/app/data/metrics.txt", "w") as f:
    f.write(f"Accuracy: {acc:.4f}")
print(f"Evaluation complete. Accuracy={acc:.4f}")
