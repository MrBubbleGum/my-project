using System;

namespace TravelLibrary
{
    /// <summary>
    /// Класс, представляющий туристическую поездку.
    /// </summary>
    public class Trip
    {
        /// <summary>
        /// Дата начала поездки.
        /// </summary>
        public DateTime StartDate { get; set; }

        /// <summary>
        /// Дата окончания поездки.
        /// </summary>
        public DateTime EndDate { get; set; }

        /// <summary>
        /// Тип поездки.
        /// </summary>
        public TripType Type { get; set; }

        /// <summary>
        /// Транспорт, использованный в поездке.
        /// </summary>
        public TransportType Transport { get; set; }

        /// <summary>
        /// Конструктор класса поездки.
        /// </summary>
        /// <param name="startDate">Дата начала поездки.</param>
        /// <param name="endDate">Дата окончания поездки.</param>
        /// <param name="type">Тип поездки.</param>
        /// <param name="transport">Тип транспорта.</param>
        public Trip(DateTime startDate, DateTime endDate, TripType type, TransportType transport)
        {
            StartDate = startDate;
            EndDate = endDate;
            Type = type;
            Transport = transport;
        }

        /// <summary>
        /// Возвращает строковое представление поездки.
        /// </summary>
        /// <returns>Строковое описание поездки.</returns>
        public override string ToString()
        {
            return $"Trip: {StartDate.ToShortDateString()} - {EndDate.ToShortDateString()}, Type: {Type}, Transport: {Transport}";
        }
    }
}