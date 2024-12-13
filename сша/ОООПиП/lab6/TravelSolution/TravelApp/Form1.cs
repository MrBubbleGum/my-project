using System;
using System.Linq;
using System.Windows.Forms;
using TravelLibrary;

namespace TravelApp
{
    public partial class Form1 : Form
    {
        // ������ ������� � �������� ��� ���������� ���������
        private Trip[] trips;
        private TripManager tripManager;

        public Form1()
        {
            InitializeComponent();

            // ������������� ������� ������� �������
            trips = new Trip[] { };
            tripManager = new TripManager(trips);

            // ���������� ��������� ComboBox ������� �� ������������
            comboBoxTripType.DataSource = Enum.GetValues(typeof(TripType));
            comboBoxTransportType.DataSource = Enum.GetValues(typeof(TransportType));
        }

        /// <summary>
        /// ���������� ������� ������ ���������� �������.
        /// </summary>
        private void buttonAddTrip_Click(object sender, EventArgs e)
        {
            // ��������, ��� ���� ������ �� ����� ���� ���������
            if (dateTimePickerStart.Value.Date > dateTimePickerEnd.Value.Date)
            {
                MessageBox.Show("���� ������ ������� �� ����� ���� ����� ���� ���������.");
                return;
            }

            // �������� ����� �������
            Trip newTrip = new Trip(
                dateTimePickerStart.Value.Date,
                dateTimePickerEnd.Value.Date,
                (TripType)comboBoxTripType.SelectedItem,
                (TransportType)comboBoxTransportType.SelectedItem
            );

            // ���������� ����� ������� � ������
            trips = trips.Append(newTrip).ToArray();
            tripManager = new TripManager(trips);  // ���������� ��������� �������

            // ����� ����� ������� � ��������� ����
            textBoxTrips.AppendText(newTrip.ToString() + Environment.NewLine);
        }

        /// <summary>
        /// ���������� ������� ������ ��� ������ ����������.
        /// </summary>
        private void buttonShowStats_Click(object sender, EventArgs e)
        {
            DateTime startDate = dateTimePickerStart.Value.Date;
            DateTime endDate = dateTimePickerEnd.Value.Date;

            // ��������� ���������� �� ����� �������
            int[] tripTypeCounts = tripManager.GetTripTypeCounts(startDate, endDate);
            string tripTypeStat = "���������� �� ����� �������:" + Environment.NewLine;
            foreach (TripType type in Enum.GetValues(typeof(TripType)))
            {
                tripTypeStat += $"{type}: {tripTypeCounts[(int)type]}" + Environment.NewLine;
            }

            // ��������� ���������� �� ����������
            int[] transportCounts = tripManager.GetTransportUsageCounts(startDate, endDate);
            string transportStat = "���������� �� ����������:" + Environment.NewLine;
            foreach (TransportType transport in Enum.GetValues(typeof(TransportType)))
            {
                transportStat += $"{transport}: {transportCounts[(int)transport]}" + Environment.NewLine;
            }

            // ����� ���������� � ��������� ����
            textBoxStats.Text = tripTypeStat + Environment.NewLine + transportStat;
        }
    }
}