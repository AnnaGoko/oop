public interface AllowedSpeedCalculator {
    double calculateAllowedSpeed(Vehicle vehicle);
}

public class CarAllowedSpeedCalculator implements AllowedSpeedCalculator {
    public double calculateAllowedSpeed(Vehicle vehicle) {
        return vehicle.getMaxSpeed() * 0.8;
    }
}

public class BusAllowedSpeedCalculator implements AllowedSpeedCalculator {
    public double calculateAllowedSpeed(Vehicle vehicle) {
        return vehicle.getMaxSpeed() * 0.6;
    }
}

public class Vehicle {
    int maxSpeed;
    AllowedSpeedCalculator allowedSpeedCalculator;

    public Vehicle(int maxSpeed, AllowedSpeedCalculator allowedSpeedCalculator) {
        this.maxSpeed = maxSpeed;
        this.allowedSpeedCalculator = allowedSpeedCalculator;
    }

    public int getMaxSpeed() {
        return this.maxSpeed;
    }

    public double getAllowedSpeed() {
        return allowedSpeedCalculator.calculateAllowedSpeed(this);
    }
}

Vehicle car = new Vehicle(200, new CarAllowedSpeedCalculator());
double carAllowedSpeed = car.getAllowedSpeed(); 

Vehicle bus = new Vehicle(120, new BusAllowedSpeedCalculator());
double busAllowedSpeed = bus.getAllowedSpeed(); 