using System;
using System.Linq;
using System.Windows.Forms;
using TravelLibrary;

namespace TravelApp
{
    public partial class Form1 : Form
    {
        // Массив поездок и менеджер для управления поездками
        private Trip[] trips;
        private TripManager tripManager;

        public Form1()
        {
            InitializeComponent();

            // Инициализация пустого массива поездок
            trips = new Trip[] { };
            tripManager = new TripManager(trips);

            // Заполнение элементов ComboBox данными из перечислений
            comboBoxTripType.DataSource = Enum.GetValues(typeof(TripType));
            comboBoxTransportType.DataSource = Enum.GetValues(typeof(TransportType));
        }

        /// <summary>
        /// Обработчик нажатия кнопки добавления поездки.
        /// </summary>
        private void buttonAddTrip_Click(object sender, EventArgs e)
        {
            // Проверка, что дата начала не позже даты окончания
            if (dateTimePickerStart.Value.Date > dateTimePickerEnd.Value.Date)
            {
                MessageBox.Show("Дата начала поездки не может быть позже даты окончания.");
                return;
            }

            // Создание новой поездки
            Trip newTrip = new Trip(
                dateTimePickerStart.Value.Date,
                dateTimePickerEnd.Value.Date,
                (TripType)comboBoxTripType.SelectedItem,
                (TransportType)comboBoxTransportType.SelectedItem
            );

            // Добавление новой поездки в массив
            trips = trips.Append(newTrip).ToArray();
            tripManager = new TripManager(trips);  // Обновление менеджера поездок

            // Вывод новой поездки в текстовое поле
            textBoxTrips.AppendText(newTrip.ToString() + Environment.NewLine);
        }

        /// <summary>
        /// Обработчик нажатия кнопки для показа статистики.
        /// </summary>
        private void buttonShowStats_Click(object sender, EventArgs e)
        {
            DateTime startDate = dateTimePickerStart.Value.Date;
            DateTime endDate = dateTimePickerEnd.Value.Date;

            // Получение статистики по типам поездок
            int[] tripTypeCounts = tripManager.GetTripTypeCounts(startDate, endDate);
            string tripTypeStat = "Статистика по типам поездок:" + Environment.NewLine;
            foreach (TripType type in Enum.GetValues(typeof(TripType)))
            {
                tripTypeStat += $"{type}: {tripTypeCounts[(int)type]}" + Environment.NewLine;
            }

            // Получение статистики по транспорту
            int[] transportCounts = tripManager.GetTransportUsageCounts(startDate, endDate);
            string transportStat = "Статистика по транспорту:" + Environment.NewLine;
            foreach (TransportType transport in Enum.GetValues(typeof(TransportType)))
            {
                transportStat += $"{transport}: {transportCounts[(int)transport]}" + Environment.NewLine;
            }

            // Вывод статистики в текстовое поле
            textBoxStats.Text = tripTypeStat + Environment.NewLine + transportStat;
        }
    }
}