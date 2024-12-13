using System;
using TravelLibrary;
using Xunit;

namespace TravelLibrary.Tests
{
    public class TripManagerTests
    {
        [Fact]
        public void GetTripsByYear_ReturnsCorrectTrips()
        {
            // Arrange
            Trip[] trips = new Trip[]
            {
                new Trip(new DateTime(2023, 5, 1), new DateTime(2023, 5, 10), TripType.BeachHoliday, TransportType.Airplane),
                new Trip(new DateTime(2023, 7, 1), new DateTime(2023, 7, 15), TripType.Skiing, TransportType.Bus),
                new Trip(new DateTime(2024, 2, 1), new DateTime(2024, 2, 10), TripType.Excursion, TransportType.Train)
            };
            TripManager manager = new TripManager(trips);

            // Act
            Trip[] result = manager.GetTripsByYear(2023);

            // Assert
            Assert.Equal(2, result.Length);
        }

        [Fact]
        public void GetTripTypeCounts_ReturnsCorrectCounts()
        {
            // Arrange
            Trip[] trips = new Trip[]
            {
                new Trip(new DateTime(2023, 5, 1), new DateTime(2023, 5, 10), TripType.BeachHoliday, TransportType.Airplane),
                new Trip(new DateTime(2023, 7, 1), new DateTime(2023, 7, 15), TripType.Skiing, TransportType.Bus),
                new Trip(new DateTime(2023, 8, 1), new DateTime(2023, 8, 10), TripType.BeachHoliday, TransportType.Train)
            };
            TripManager manager = new TripManager(trips);

            // Act
            int[] result = manager.GetTripTypeCounts(new DateTime(2023, 1, 1), new DateTime(2023, 12, 31));

            // Assert
            Assert.Equal(2, result[(int)TripType.BeachHoliday]);
            Assert.Equal(1, result[(int)TripType.Skiing]);
        }

        [Fact]
        public void GetTransportUsageCounts_ReturnsCorrectCounts()
        {
            // Arrange
            Trip[] trips = new Trip[]
            {
                new Trip(new DateTime(2023, 5, 1), new DateTime(2023, 5, 10), TripType.BeachHoliday, TransportType.Airplane),
                new Trip(new DateTime(2023, 7, 1), new DateTime(2023, 7, 15), TripType.Skiing, TransportType.Bus),
                new Trip(new DateTime(2023, 8, 1), new DateTime(2023, 8, 10), TripType.BeachHoliday, TransportType.Train)
            };
            TripManager manager = new TripManager(trips);

            // Act
            int[] result = manager.GetTransportUsageCounts(new DateTime(2023, 1, 1), new DateTime(2023, 12, 31));

            // Assert
            Assert.Equal(1, result[(int)TransportType.Airplane]);
            Assert.Equal(1, result[(int)TransportType.Bus]);
            Assert.Equal(1, result[(int)TransportType.Train]);
        }
    }
}