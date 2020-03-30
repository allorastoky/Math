a= int(input("Inserire il termine di x (a): "))
b= int(input("Inserire il termine di y (b): "))
c= int(input("Inserire il termine noto (c): "))
if a==0 and b==0 and c==0:
	print("L'equazione alla circonferenza: x^2+y^2")
elif a==0 and b==0:
	if c>0:
		print("L'equazione inserita non corrisponde a quella di una circonferenza, poichè il raggio verrebe sottoforma della radice di un numero negativo.")
	else:
		print("L'equazione inserita corrisponde alla circonferenza: x^2+y^2", c, "\n Il centro della circonferenza si trova all'origine degli assi: c(0, 0)")
