def keyargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
keyargs(name="tesla", company="Tesla")
keyargs(name="tesla")
keyargs(name="seltos", company="Kia", model="latest")