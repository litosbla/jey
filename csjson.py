import json
general={}
general["Vendedores"]=[]
with open("archivoplano.txt","r") as file:
    lineas=file.readlines()

print(lineas)

for i_linea in range(1,len(lineas)):
    splits=lineas[i_linea].replace("\n","").split(", ")
    data={
        "Apellido":splits[0],
        "Id":splits[1],
        "Ventas":[int(x) for x in splits[2:]]
    }
    general["Vendedores"].append(data)

 
with open('vendedores.json','w') as file:
    json.dump(general,file,indent=4)