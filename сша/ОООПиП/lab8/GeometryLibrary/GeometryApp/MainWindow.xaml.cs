using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;
using GeometryLibrary;

namespace GeometryApp
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void LoadFigures_Click(object sender, RoutedEventArgs e)
        {
            List<GeometricFigure> figures = new List<GeometricFigure>();

            FiguresList.Items.Clear();

            foreach (var line in File.ReadLines("figures.txt"))
            {
                // Display the original data
                var originalDataItem = new ListBoxItem
                {
                    Content = $"Original Data: {line}",
                    Foreground = Brushes.Gray
                };
                FiguresList.Items.Add(originalDataItem);

                var parts = line.Split(',');
                var color = parts[0];
                var type = parts[1];

                if (type == "Rectangle")
                {
                    var vertices = ParseVertices(parts, 2, 4);
                    figures.Add(new Rectangle(vertices) { Color = color });
                }
                else if (type == "Triangle")
                {
                    var vertices = ParseVertices(parts, 2, 3);
                    figures.Add(new Triangle(vertices) { Color = color });
                }
                else if (type == "Circle")
                {
                    var center = (
                        double.Parse(parts[2], CultureInfo.InvariantCulture),
                        double.Parse(parts[3], CultureInfo.InvariantCulture)
                    );
                    var radius = double.Parse(parts[4], CultureInfo.InvariantCulture);
                    figures.Add(new Circle(center, radius) { Color = color });
                }
            }

            figures.Sort((a, b) => a.CalculateArea().CompareTo(b.CalculateArea()));

            foreach (var figure in figures)
            {
                figure.DisplayInfo();
                var listItem = new ListBoxItem
                {
                    Content = $"{figure.GetType().Name}: {figure.Color}, Area: {figure.CalculateArea()}",
                    Foreground = GetBrushFromColorName(figure.Color)
                };
                FiguresList.Items.Add(listItem);
            }
        }

        private (double X, double Y)[] ParseVertices(string[] parts, int startIndex, int count)
        {
            var vertices = new (double X, double Y)[count];
            for (int i = 0; i < count; i++)
            {
                vertices[i] = (
                    double.Parse(parts[startIndex + i * 2], CultureInfo.InvariantCulture),
                    double.Parse(parts[startIndex + i * 2 + 1], CultureInfo.InvariantCulture)
                );
            }
            return vertices;
        }

        private Brush GetBrushFromColorName(string colorName)
        {
            try
            {
                return (Brush)new BrushConverter().ConvertFromString(colorName);
            }
            catch
            {
                return Brushes.Black;
            }
        }
    }
}