import csv
import matplotlib.pyplot as plt

def main():
    try:
        data = []
        with open('./data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for line in reader:
                data.append([float(line[0]), float(line[1])])

        mileage = [row[0] for row in data]
        price = [row[1] for row in data]

        meanMileage = sum(mileage) / len(mileage)
        deviations = [(x - meanMileage) ** 2 for x in mileage]
        variance = sum(deviations) / len(deviations)
        stdMileage = variance ** 0.5

        mileageNormalized = [(x - meanMileage) / stdMileage for x in mileage]

        numIterations = 1000
        theta0 = 0.0
        theta1 = 0.0
        try:
            with open("gradient.csv", "r") as gradients:
                next(gradients)  # Skip header
                theta0, theta1, _, _ = map(float, gradients.readline().split(','))  # Read and parse the first line
        except:
            print("No gradient file, creating one")
        learningRate = 0.01
        m = len(price)
        
        for iteration in range(numIterations):
            sumError = 0
            sumErrorKm = 0
            for i in range(m):
                km = mileageNormalized[i]
                actualPrice = price[i]
                prediction = theta0 + theta1 * km
                error = prediction - actualPrice
                precision = error
                if (precision < 0):
                    precision = precision * -1
                print(str(100 - ((precision * 100) / actualPrice)) + " %")
                sumError += error
                sumErrorKm += error * km

            gradientTheta0 = (1/m) * sumError
            gradientTheta1 = (1/m) * sumErrorKm

            theta0 -= learningRate * gradientTheta0
            theta1 -= learningRate * gradientTheta1

        try:
            with open('gradient.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['theta0', 'theta1', 'meanMileage', 'stdMileage'])
                writer.writerow([theta0, theta1, meanMileage, stdMileage])
        except Exception as e:
            print("Error while creating gradient save file : " + e.message + "\n\tResult not saved")
        print(f"Final: theta0 = {theta0}, theta1 = {theta1}")
        plt.figure(figsize=(10, 5))
        plt.scatter(mileage, price, color='blue', label='Data')
        linear_regression = [theta0 + theta1 * ((x - meanMileage) / stdMileage) for x in mileage]
        plt.plot(mileage, linear_regression, color='red', label='linear regression')
        plt.title('Prix en fonction du kilométrage')
        plt.xlabel('km')
        plt.ylabel('Price €')
        plt.legend()
        plt.show()

    except FileNotFoundError:
        print("Error: data.csv file not found")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    main()
