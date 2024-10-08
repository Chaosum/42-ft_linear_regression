def main():
    theta0 = 0
    theta1 = 0
    meanMileage = 1
    stdMileage = 1
    try:
        with open("gradient.csv", 'r') as gradients:
            next(gradients)  # Skip header
            theta0, theta1, meanMileage, stdMileage = map(float, gradients.readline().split(','))  # Read and parse the first line
    except FileNotFoundError:
        print("gradient file not found : defalt value for theta0 and theta1")
    try:
        mileage = float(input("Enter the km of the car : "))
    except Exception as e:
        print(f"Error : {e}")
        return
    try:
        normalizedMileage = (mileage - meanMileage) / stdMileage  # Normalize the input mileage
        predicted_price = theta0 + theta1 * normalizedMileage
        if predicted_price < 0:
            
            predicted_price = 0
        print(f"The price of a car with {mileage} km is {predicted_price:.2f} euros.")
    except Exception as e:
        print(f"Error : {e}")
if __name__ == "__main__":
    main()
