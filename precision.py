import csv

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
        theta0 = 0.0
        theta1 = 0.0
        m = len(price)
        try:
            with open("gradient.csv", "r") as gradients:
                next(gradients)  # Skip header
                theta0, theta1, _, _ = map(float, gradients.readline().split(','))  # Read and parse the first line
        except:
            print("Erreur opening gradient file : Using default theta values (0.0)")
        precision = []
        sumError = 0
        for i in range(m):
            km = mileageNormalized[i]
            actualPrice = price[i]
            prediction = theta0 + theta1 * km
            error = prediction - actualPrice
            sumError += error
            if (error < 0):
                error = error * -1            
            if (sumError < 0):
                sumError = sumError * -1
            precision.append((error * 100) / actualPrice)
 
        i = 0
        for p in precision:
            i += 1
            print(f"{i} : {100 - p} %")
        sumPrecision = 0.0
        for value in precision:
            sumPrecision += value
        sumPrecision = sumPrecision / m
        print("Mean precision = " + str(100 - sumPrecision) + " %")
    except FileNotFoundError:
        print("Error: data.csv file not found")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    main()
