Num1 = input("Enter the first number: ")
Num2 = input("Enter the second number: ")


if (Num1.isdigit() and Num2.isdigit())==False:
      print("invalid number")
else:
        choice = input("Choose the operation (+, -, /, *): ")
        if choice == "+":
         	result = int(Num1)+ int(Num2)
         	print("answer=:",result)
        elif choice == "-":
            result = int(Num1) - int(Num2)
            print("answer=:",result)
        elif choice == "/":
        	result = int(Num1)/int(Num2)
        	print("answer=:" ,result)
        elif choice == "*":
            result = int(Num1)*int(Num2)
            print("answer=:" ,result)
        else:
        	print("the operation is not valid.")

