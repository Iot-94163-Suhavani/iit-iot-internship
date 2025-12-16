kg=lambda t:t*1000
g=lambda kg:kg*1000
mg=lambda g:g*1000
p=lambda mg:mg*0.0000022046

W=float(input("Enter weight in tonns :"))

print(f"t_kg={kg(W)}")
print(f"kg_to_g={g(W)}")
print(f"g_to_mg={mg(W)}")
print(f"mg_to_p={p(W)}")
