def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None
    
    return peso / altura ** 2

print(imc(352.5, 1.65))

def lbakg(lb):
    return lb * 0.45359237

print(lbakg(1))
def piepulgam(pie, pulgada):
    return pie * 0.3048 + pulgada * 0.0254

print(piepulgam(1, 1))