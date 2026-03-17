import numpy as np

# Charger le fichier
data = np.load('scenedir/poses_bounds.npy')
data2 = np.fromfile('scenedir/sparse/0/images.bin', dtype=np.float32)
# Afficher le contenu
print(f"Forme (shape): {data.shape}")
print(f"Forme (shape) data2: {data2.shape}")    
print(data[0])