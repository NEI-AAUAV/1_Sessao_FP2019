# Example: a classifier

x = float(input("Altura (m)? "))

#print(x)

if x > 1.9:
    cl = "alto"
elif x<1.9 and x>1.6:
    cl = "medio"
else:
    cl = "baixo"

## WHAT's the ERROR?

print("És", cl)
