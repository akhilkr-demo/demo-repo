import pandas as pd
import numpy as np

# Create a random DataFrame with three columns: 'A', 'B', 'C'
data = {
    'A': np.random.rand(5),
    'B': np.random.rand(5),
    'C': np.random.rand(5)
}

df = pd.DataFrame(data)

# Print the DataFrame
print(df)
