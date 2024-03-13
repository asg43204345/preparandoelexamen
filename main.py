bandas=[]


#construyendo la interfaz
print("***ALTAVOZ ES TU VOZ***")
print("***********************")

opcion=100
while(opcion!=5):
    
    print("1.Registrar Banda")
    print("2.buscar Informacion de una Banda")
    print("3.Agenda del Evento ")
    print("4.modificar Banda")
    print("5.Salir")
    
    
    opcion=int(input("digita una opcion: "))
     
    if opcion==1:
        banda={}
         #Creando los datos del diccionario
        banda["id"]=int(input("Digita el id: "))
        banda["nombre"]=input("Nombre de la Banda: ")
        banda["genero"]=input("Genero: ")
        banda["clasificacion"]=input("Clasificacion: ")
        banda["Tiempo"]=int(input("Tiempo: "))
        banda["costo"]=int(input("Costo: $"))
         
      #Agregando un Diccionario a una lista
        bandas.append(banda)
    
    elif opcion==2:
        
        bandaBuscada=input("Digita el nombre de la banda que estas buscando: ")
        for bandAuxiliar in bandas:
           if bandAuxiliar["nombre"]==bandaBuscada:
               #como lo encontre muestro los datos de bandAuxiliar
               print(f"id: {bandAuxiliar["id"]}---nombre: {bandAuxiliar["nombre"]}") 
               print("oe lo encontre...")
        else:
                print("parce siga buscando....")
           
         
    elif opcion==3:
        print(banda)
    elif opcion==4:
        
    elif opcion==5:
        pass
    else:
        pass   
    