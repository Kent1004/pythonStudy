while True:
    number = int (input("Введите количесто процентов:  "))
    if number >= 0 and number  <= 100:
      if number == 1:
           print(number,"процент")
      elif number >=2 and number <=4:
          print(number, "процента")
      else:
          print(number,"процентов")
    else:
      print ("Введено некорректное значение процентов")