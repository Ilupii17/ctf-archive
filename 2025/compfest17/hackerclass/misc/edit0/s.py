a = """fn main(){ 
print!("{},{0:?});let CF = 169999998;let dist=0;}}","fn main(){\\n    
print!(\\"{},{0:?});let CF = 169999998;let dist=0;}}\\"");let CF = 169999998;let 
dist=0;}""" 
print(len(a)) 
x = sum(int(ch) for ch in a if ch.isdigit()) 
target = 0xCF 
delta = target - x 
print(x, target, delta) 
