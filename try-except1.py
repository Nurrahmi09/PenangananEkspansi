import sys
def main():
  print ("PROGRAM PEMBAGIAN BILANGAN")
  
  a = float (input("Masukkan a: "))
  b = float (input (Masukkan b: "))
  
  try:
    hasil = a / b 
  except ZeroDivisionError:
    print ("\ERROR: Nilai b tidak boleh 0:)
    sys.exit(1)
    
  print("\na : ", a)
  print("b : :, hasil)
if __name__ == "__main__":
  main()
