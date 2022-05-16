# my resolution:
msg = 'bottles of beer on the wall'
for num in range(100, -1, -1):
    print(f"{num} {msg}")
    print(f"Take one down, pass it around,{num - 1} {msg}")
    if num == 0:
        print('No more bottles of beer on the wall')
        
# another resolution:
for num_bottles in range(99, 0, -1):
    print(f"{num_bottles} bottles of beer on the wall")
    print(f"{num_bottles} bottles of beer.")
    print(f"Take one down, pass it around, {num_bottles - 1} bottles of beer on the wall")        