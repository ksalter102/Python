flowers = ["daffodil",
           "evening primrose",
           "hydrangea",
           "iris",
           "lavender",
           "tiger lily",
           "sunflower"
    ]
# for flower in flowers:
#     print(flower)

seperator = " | "
output = seperator.join(flowers)
print(output) #will add | as a seperator between items

print(", ".join(flowers)) #will sep with ,
#join only works with strings