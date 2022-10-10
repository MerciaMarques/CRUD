#CRUD

import os
import time

registros=[]
nomes= []
idades= []
telefones= []
plano = []
dadosdocliente= [registros, nomes, idades, telefones, plano]
campos =['Registro:','Nome:' , 'Idade:' , 'Tel:' , 'Convênio:' ]


with open("crud.txt","r+") as arquivo:
    lista=[]
    for dados in arquivo:
        lista.append(dados[:-1])
        #print(lista)

    for i in range (int(len(lista)/5)):
        registros.append(lista[(i*5)])
        nomes.append(lista[(i*5)+1])
        idades.append(lista[(i*5)+2])
        telefones.append(lista[(i*5)+3])
        plano.append(lista[(i*5)+4])
        #print(dadosdocliente)


while True: 
    os.system('clear') #limpar tela
    print ("\nCadastro dos Clientes do Consultório Médico")
    print("_________________________________________________")

    print ("\n Menu Principal")
  
    print("\nO que gostaria de fazer?")
    print("\n1 - Criar o cadastro digite ")
    print("2 - Consultar o cadastro digite")
    print("3 - Alterar o cadastro digite")
    print("4 - Deletar o cadastro digite")
    print("0 - Sair")
    opcao = input("\nSelecione uma opcao: ")
    
    os.system('clear') #limpar tela

    if (opcao == '1'): #Primeiro cadastro
        registro = (len(registros)) +1
        registros.append(registro)
        nome=input("Digite o nome: ")
        nomes.append(nome)
        idade=int(input("Digite a idade: " ))
        idades.append(idade)
        telefone=int(input("Digite o telefone: "))
        telefones.append(telefone)
        segurosaude= input("Plano de saúde: \n 's'sim \n 'n' não \n")
        if (segurosaude == 's'):
            tipo = input("Qual o Plano de Saúde:")
            plano.append (tipo)
            time.sleep (2) 
            os.system('clear')
        else: 
            print ("Consulta Particular R$ 200,00")
            plano.append ('Particular')
            time.sleep (2) 
            os.system('clear')

        with open("crud.txt","r+") as arquivo:
            for i in range (len(registros)):
                arquivo.write (str(registros[i])+'\n')
                arquivo.write (str(nomes[i])+'\n')
                arquivo.write (str(idades[i])+'\n')    
                arquivo.write (str(telefones[i])+'\n')
                arquivo.write (str(plano[i])+'\n')

    elif (opcao =='2'): #Visualizar o Cadastro
        print ("1 - Consultar pelo nome")
        print ("2 - Consultar pela chave") 
        escolha = input("\nSelecione uma opcao: ")
        os.system('clear')


        if (escolha == '1'):
            nome = input("Digite o nome: ")
            indice = nomes.index(nome)  #contador para buscar o indice dentro da lista nomes
            for i in range (len(dadosdocliente)): #Imprimir os dados do cliente
                print(campos[i], dadosdocliente[i][indice]) #Imprimir os dados do cliente
                

            print ( )# Dentro de Visualizar o Cadastro, pode alterar ou deletar
            print("A - Deseja alterar o cadastro?")
            print("D - Deseja deletar o cadastro?")
            print("R - Retornar ao Menu Principal?")
            alterar_deletar= input("Digite a opção: ")
            
            os.system('clear')

            if (alterar_deletar=='A' or alterar_deletar=='a'): #Alterar dentro do Visualização do cadastro
                while (escolha!='0'):
                    escolha= input("O que desejar alterar \n1 - Nome, \n2 - Idade,\n3 - Telefone\n4 - Convênio \n5 - Sair \n__= ")
                    if (escolha=='1'):
                        nomes.insert (indice, input("Digite o novo nome: "))
                    elif (escolha=='2'):
                        idades.insert(indice, input("Digite a nova idade: "))
                    elif (escolha=='3'):
                        telefones.insert (indice, input("Digite o novo telefone: "))  
                    elif (escolha=='4'):
                        plano.insert (indice, input("Digite o Convênio: "))
                    for i in range (len(dadosdocliente)): 
                        print(campos[i], dadosdocliente[i][indice])                   
                time.sleep (3) 
                os.system('clear')
            
            elif (alterar_deletar=='D'or alterar_deletar=='d'): # Deletar dentro da visualizacao do cadastro
                print ("O que deseja deletar: ")

                deletar= input("1 - Cadastro do Paciente \n2 - Idade \n3 - Telefone \n4 - Convênio \n0 - Retornar para o Menu Principal =__")  
                while (deletar!='0'):
                    if (deletar=='1'):
                        escolha= input("Tem certeza que deseja apagar todos os dados do cliente \n sim \n não \n__:")
                        if (escolha=='s'):
                            nomes[indice] = ' '
                            idades[indice] = ' '
                            telefones[indice] = ' '
                            plano[indice] = ' ' 
                        deletar = '0'
                            #Final da opção de deletar o cadastro do paciente
                        time.sleep (2) 
                        os.system('clear')

                    elif (deletar=='2'):
                        idades[indice]= ' '
                        print("Idade do cliente deletada")
                        deletar = '0'
                        time.sleep (2) 
                        os.system('clear') 

                    elif (deletar=='3'):
                        telefones[indice]= ' '
                        print("Telefone do cliente deletado")
                        deletar = '0'
                        time.sleep (2) 
                        os.system('clear')

                    elif (deletar=='4'):
                        plano[indice]=('Particular')
                        print("Convênio deletado, \nConsulta Particular")   
                        deletar = '0'
                        time.sleep (2)
                        os.system('clear')

                with open("crud.txt","w") as arquivo:
                    for i in range (len(registros)):
                        arquivo.write (str(registros[i])+'\n')
                        arquivo.write (str(nomes[i])+'\n')
                        arquivo.write (str(idades[i])+'\n')    
                        arquivo.write (str(telefones[i])+'\n')
                        arquivo.write (str(plano[i])+'\n') 
            
        elif (escolha=='2'):# Consultar pela chave dentro do visualizar cadastro
            registro= input("Digite o registro do cliente ")
            if  registro in registros:
                indice = registros.index(registro) 
                for i in range (len(dadosdocliente)): #Imprimir os dados do cliente
                    print(campos[i], dadosdocliente[i][indice])

                print("A - Deseja alterar o cadastro?") # Fazer alteração ou deletar dentro da visualização da chave
                print("D - Deseja deletar o cadastro?")
                print("R - Retornar ao Menu Principal?")
                alterar_deletar=input("Digite a opção: ")
                time.sleep (2)
                os.system('clear')
            
                if (alterar_deletar=='A'or alterar_deletar=='a'):# Alterar pela chave
                    while (escolha!='0'):
                        escolha= input("O que desejar alterar \n1 - Nome \n2 - Idade\n3 - Telefone\n4 - Convênio \n0 - Sair \n__= ")
                        if (escolha=='1'):
                            nomes.insert (indice, input("Digite o novo nome: "))
                        elif (escolha=='2'):
                            idades.insert(indice, input("Digite a nova idade: "))
                        elif (escolha=='3'):
                            telefones.insert (indice, input("Digite o novo telefone: "))  
                        elif (escolha=='4'):
                            plano.insert (indice, input("Digite o Convênio: "))
                        for i in range (len(dadosdocliente)): 
                            print(campos[i], dadosdocliente[i][indice])                    
                        time.sleep (2) 
                        os.system('clear')
                
                elif (alterar_deletar=='D'or alterar_deletar=='d'): # Deletar pela chave
                    print ("O que deseja deletar: ")

                    deletar= input("1 - Cadastro do Paciente \n2 - Idade \n3 - Telefone \n4- Convênio \n0 - Retornar para o Menu Principal=__")  
                    while (deletar!='0'):
                        if (deletar=='1'):
                            escolha= input("Tem certeza que deseja apagar todos os dados do cliente \n sim \n não \n__:")
                            if (escolha=='s'):
                                nomes[indice] = ' '
                                idades[indice] = ' '
                                telefones[indice] = ' '
                                plano[indice] = ' '
                                print (dadosdocliente[i][indice])
                                print ("Cadastro deletado")
                            deletar = '0'
                            #Final da opção de deletar o cadastro COMPLETO do paciente 
                            time.sleep (2) 
                            os.system('clear')

                        elif (deletar=='2'):
                            idades[indice]= ' '
                            print("Idade do cliente deletada")
                            deletar = '0'
                            time.sleep (2) 
                            os.system('clear') 

                        elif (deletar=='3'):
                            telefones[indice]= ' '
                            print("Telefone do cliente deletado")
                            deletar = '0'
                            time.sleep (2) 
                            os.system('clear')

                        elif (deletar=='4'):
                            plano[indice]=('Particular')
                            print("Convênio deletado, \nConsulta Particular") 
                            deletar = '0'  
                            time.sleep (2)
                            os.system('clear')

                with open("crud.txt","w") as arquivo:
                    for i in range (len(registros)):
                        arquivo.write (str(registros[i])+'\n')
                        arquivo.write (str(nomes[i])+'\n')
                        arquivo.write (str(idades[i])+'\n')    
                        arquivo.write (str(telefones[i])+'\n')                        
                        arquivo.write (str(plano[i])+'\n') 
            else: # chave digita maior do que ao len de registro
                print("Opcao Invalida")
                print ("Retornando ao Menu Principal")   
                os.system('clear')        
        else: # erro a opcao de visualizacao nome/chave
            print ("Opcao Invalida!")
            print ("Retornando ao Menu Principal")
            deletar ='0'  
            time.sleep (2)
            os.system('clear')
                         
    elif (opcao =='3'): #Alterar o Cadastro do Menu Principal (3)
        print("\nDeseja alterar dados \n's' sim ou \n'n' não")
        alterar= input("\nSelecione uma opcao: ")
        if (alterar=='s'):         
            nome = input("Digite o nome: ")
            indice = nomes.index(nome) 
            for i in range (len(dadosdocliente)): 
                print(campos[i], dadosdocliente[i][indice])
                print( )
            alterar= input("O que desejar alterar \n1 - Nome, \n2 - Idade,\n3 - Telefone\n4 - Convênio \n0 - Sair \n__= ")
            time.sleep (2) 
            os.system('clear')

            if (alterar=='1'):
                nomes.insert (indice, input("Digite o novo nome: "))
                for i in range (len(dadosdocliente)): 
                    print(campos[i], dadosdocliente[i][indice])
            elif (alterar=='2'):
                idades.insert (indice, input("Digite a nova idade: "))
                for i in range (len(dadosdocliente)): 
                    print(campos[i], dadosdocliente[i][indice])
            elif (alterar=='3'):
                telefones.insert (indice, input("Digite o novo telefone: "))
                for i in range (len(dadosdocliente)): 
                    print(campos[i], dadosdocliente[i][indice]) 
            elif (alterar=='4'):
                plano.insert (indice, input("Digite o Convênio: "))
                for i in range (len(dadosdocliente)): 
                    print(campos[i], dadosdocliente[i][indice])

            with open("crud.txt","w") as arquivo:
                for i in range (len(registros)):
                    arquivo.write (str(registros[i])+'\n')
                    arquivo.write (str(nomes[i])+'\n')
                    arquivo.write (str(idades[i])+'\n')    
                    arquivo.write (str(telefones[i])+'\n') 
                    arquivo.write (str(plano[i])+'\n')    

            os.system('clear')

    elif (opcao=='4'):#Deletar pelo Menu Principal
        print ("O que deseja deletar: ")
        deletar= input("1 - Cadastro do Paciente \n2 - Idade \n3 - Telefone \n4 - Convênio \n0 - Retornar para o Menu Principal=__ ")
        while (deletar!='0'):   
            if (deletar=='1'):
                nome = input("Digite o nome: ")
                indice = nomes.index(nome)  

                for i in range (len(dadosdocliente)): 
                    print(campos[i], dadosdocliente[i][indice])

                escolha= input("Tem certeza que deseja apagar os dados do cliente \n's' sim \n'n' não \n__:")
                if (escolha=='s'):
                    nomes[indice] = ' '
                    idades[indice] = ' '
                    telefones[indice] = ' '
                    plano[indice] = ' '
                    print (dadosdocliente[i][indice])
                    
                deletar = '0'
                print("Cadastro do cliente deletado!") 
                time.sleep (2) 
                os.system('clear')

            elif (deletar=='2'):
                nome = input("Digite o nome: ")
                indice = nomes.index(nome)
                for i in range (len(dadosdocliente)):  
                    idades[indice]= ' '
                print("Idade do cliente deletada") 
                time.sleep (2) 
                os.system('clear')

            elif (deletar=='3'):
                nome = input("Digite o nome")
                indice = nomes.index(nome)
                for i in range (len(dadosdocliente)):               
                    telefones[indice]= ' '
                print("Telefone do cliente deletado")
                time.sleep (2) 
                os.system('clear')

            elif (deletar=='4'):
                nome = input("Digite o nome")
                indice = nomes.index(nome)
                for i in range (len(dadosdocliente)):               
                    plano[indice]=('Particular')
                print("Convênio deletado, \nConsulta Particular") 
                time.sleep (2) 
                os.system('clear')

        with open("crud.txt","w") as arquivo:
            for i in range (len(registros)):
                arquivo.write (str(registros[i])+'\n')
                arquivo.write (str(nomes[i])+'\n')
                arquivo.write (str(idades[i])+'\n')                       
                arquivo.write (str(telefones[i])+'\n')
                arquivo.write (str(plano[i])+'\n')  


    elif (opcao == '0'):
        print("Agradecemos o cadastro")
        print("____________________________")
        exit()

    else:
        print("Opcao Invalida!")
        print("Retornando ao Menu Principal")
        time.sleep(2)
        os.system('clear')