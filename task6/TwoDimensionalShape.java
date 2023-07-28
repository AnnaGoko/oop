public interface TwoDimensionalShape {
    double area();
}

public interface ThreeDimensionalShape {
    double volume();
}

public class Circle implements TwoDimensionalShape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double area() {
        return 2 * 3.14 * radius;
    }
}

public class Cube implements ThreeDimensionalShape, TwoDimensionalShape {
    private int edge;

    public Cube(int edge) {
        this.edge = edge;
    }

    @Override
    public double area() {
        return 6 * edge * edge;
    }

    @Override
    public double volume() {
        return edge * edge * edge;
    }
}


TwoDimensionalShape circle = new Circle(5);
double circleArea = circle.area(); 

ThreeDimensionalShape cube = new Cube(3);
double cubeVolume = cube.volume(); 

TwoDimensionalShape cube2d = new Cube(3);
double cubeArea = cube2d.area(); 