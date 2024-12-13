using System;

namespace GeometryLibrary
{
    public abstract class Polygon : GeometricFigure, IComparable<Polygon>
    {
        public (double X, double Y)[] Vertices { get; set; }

        public abstract double CalculatePerimeter();
        public override abstract double CalculateArea();

        public int CompareTo(Polygon other)
        {
            return CalculateArea().CompareTo(other.CalculateArea());
        }
    }
}