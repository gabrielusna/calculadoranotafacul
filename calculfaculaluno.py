aprovados = []
reprovados = []

while True:
  aluno = str(input("Qual é seu nome ?: "))
  while True: 
    ativ1 = float(input(f"{aluno}, Qual Sua Nota Da Atividade Um ?: "))
    if ativ1  < 0.0 or ativ1 > 1.0:
      print("Sua Nota Está Incorreta, Tente Novamente!")
    else: 
      break

  while True:
    ativ2 = float(input(f"{aluno}, Qual Sua Nota Da Atividade Dois ?: "))
    if ativ2  < 0.0 or ativ2 > 2.0:
      print("Sua Nota Está Incorreta, Tente Novamente!")
    else: 
      break

  while True:
    ativ3 = float(input(f"{aluno}, Qual Sua Nota Da Atividade Três ?: "))
    if ativ3  < 0.0 or ativ3 > 1.0:
      print("Sua Nota Está Incorreta, Tente Novamente!")
    else: 
      break

  while True:
    provaregular = float(input(f"{aluno}, Qual Sua Nota Da Prova Regular ?: "))
    if provaregular  < 0.0 or provaregular > 6.0:
      print("Sua Nota Está Incorreta, Tente Novamente!")
    else: 
      break
  media = (ativ1 + ativ2 + ativ3 + provaregular) 
  if (media >=7):
    print(f"O aluno {aluno} foi APROVADO com {media} pontos")
    aprovados.append(aluno)
  if (media <=6):
    print(f"O aluno {aluno} ficou com {media} pontos, e não atingiu a média! \nAgora precisa fazer a recuperação!") 
    while True:
      recuperacao = float(input(f"Digite Sua Nota De Recuperação, {aluno}: "))
      mediaGeral = (media + recuperacao) /2
      if recuperacao >= 5.0 and recuperacao <= 10.0:
        print(f"O aluno {aluno} ficou com {mediaGeral} pontos na recuperação, e foi APROVADO!") 
        aprovados.append(aluno)
        print("-" * 48)
        break
      elif recuperacao >= 0 and recuperacao < 5:
        print(f"O aluno {aluno} ficou com {mediaGeral} pontos na recuperação, e foi REPROVADO!")
        reprovados.append(aluno)
        print("-" * 48)
        break
      else:
        print("Sua Nota Está Incorreta, Tente Novamente!")

  while True:
   continuar = str(input("Gostaria de calcular mais uma nota? [s/n]: "))
   if continuar == "s":                                                              
      break
   elif continuar == "n":
      break
  if continuar == "n":
     break
print("-" * 48)

total_alunos = len(aprovados) + len(reprovados)
aprovados_pcento = (100 / total_alunos) * len(aprovados)
reprovados_pcento = (100 / total_alunos) * len(reprovados)

print("{:.2f}% alunos foram APROVADOS e {:.2f}% ficaram REPROVADOS".format(aprovados_pcento, reprovados_pcento))
 
