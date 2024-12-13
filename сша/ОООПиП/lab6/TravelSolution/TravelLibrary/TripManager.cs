using System;
using System.Linq;

namespace TravelLibrary
{
    /// <summary>
    /// Класс для управления туристическими поездками.
    /// </summary>
    public class TripManager
    {
        /// <summary>
        /// Массив для хранения поездок.
        /// </summary>
        private Trip[] trips;

        /// <summary>
        /// Конструктор класса управления поездками.
        /// </summary>
        /// <param name="trips">Массив поездок.</param>
        public TripManager(Trip[] trips)
        {
            this.trips = trips;
        }

        /// <summary>
        /// Вывод всех поездок за указанный год.
        /// </summary>
        /// <param name="year">Год.</param>
        /// <returns>Массив поездок за указанный год.</returns>
        public Trip[] GetTripsByYear(int year)
        {
            return trips.Where(t => t.StartDate.Year == year).ToArray();
        }

        /// <summary>
        /// Подсчет количества поездок по типам за указанный период.
        /// </summary>
        /// <param name="startDate">Дата начала периода.</param>
        /// <param name="endDate">Дата окончания периода.</param>
        /// <returns>Массив количества поездок по типам.</returns>
        public int[] GetTripTypeCounts(DateTime startDate, DateTime endDate)
        {
            int[] typeCounts = new int[Enum.GetValues(typeof(TripType)).Length];

            foreach (var trip in trips)
            {
                if (trip.StartDate >= startDate && trip.EndDate <= endDate)
                {
                    typeCounts[(int)trip.Type]++;
                }
            }

            return typeCounts;
        }

        /// <summary>
        /// Подсчет использования транспорта за указанный период.
        /// </summary>
        /// <param name="startDate">Дата начала периода.</param>
        /// <param name="endDate">Дата окончания периода.</param>
        /// <returns>Массив количества использования транспорта.</returns>
        public int[] GetTransportUsageCounts(DateTime startDate, DateTime endDate)
        {
            int[] transportCounts = new int[Enum.GetValues(typeof(TransportType)).Length];

            foreach (var trip in trips)
            {
                if (trip.StartDate >= startDate && trip.EndDate <= endDate)
                {
                    transportCounts[(int)trip.Transport]++;
                }
            }

            return transportCounts;
        }
    }
}