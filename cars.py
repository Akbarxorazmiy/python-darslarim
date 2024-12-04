narx=15000
choy=1
salat=0

if choy and salat:
    narx=narx+10000
elif choy or salat:
    narx=narx+5000
    
print(f"Sizdan {narx} so'm bo'ldi")
