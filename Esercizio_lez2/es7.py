def tipo_triangolo(a, b, c):
    
    if (a + b > c) & (a + c > b) & (b + c > a):
        
        
        if a == b == c:
            return "Triangolo Equilatero"
        elif a == b or b == c or a == c:
            return "Triangolo Isoscele"
        else:
            return "Triangolo Scaleno"
            
    else:
        return "Questi valori non possono formare un triangolo"
    