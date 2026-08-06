def main() -> None:
    Answer = input ("Hello, do you want to convert Celsius or Fahrenheit? ")
    Degree = float(input ("What is the temperature? "))
    if (Answer == "Celsius"):
        # Celsius to Fahrenheit
        Fahrenheit = Degree * 1.8 + 32
        print ("Temperature in Fahrenheit: %f degrees" % Fahrenheit)
    elif (Answer == "Fahrenheit"):
        # Fahrenheit to Celsius
        Celsius = (Degree - 32) * (5/9)
        print ("Temperatrue in Celsius: %f degrees" % Celsius)
    else:
        print ("Please choose either Celsius or Fahrenheit")
    


if __name__ == "__main__":
    main()
