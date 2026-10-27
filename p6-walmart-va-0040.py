import matplotlib.pyplot as plt
import numpy as np
# Hugo Fabian NC 0040   

cant_productos=[100,150,200,300,500]
precio = [4000, 7000, 9000, 12000, 18000]

plt.plot(cant_productos,precio)
plt.show()

# personalizar grafica
plt.plot(cant_productos, precio, color="black", marker="o", linestyle="--", linewidth=2, markersize=12)
plt.title("Ventas de Walmart 0040")
plt.xlabel("cant prod")
plt.ylabel("precio")
plt.show()