using System;
using System.Collections.Generic;
using System.Windows;
using System.Windows.Controls;
using TireShopLibrary;

namespace TireShopApp
{
    public partial class MainWindow : Window
    {
        private WorkManager workManager;

        public MainWindow()
        {
            InitializeComponent();
            workManager = new WorkManager();
            workDataGrid.ItemsSource = new List<Work>();
        }

        private void AddWork_Click(object sender, RoutedEventArgs e)
        {
            DateTime date = datePicker.SelectedDate ?? DateTime.Now;
            string car = carTextBox.Text;
            string workType = (workTypeComboBox.SelectedItem as ComboBoxItem)?.Content.ToString();
            decimal cost = decimal.Parse(costTextBox.Text);

            Work work = null;

            switch (workType)
            {
                case "Замена шин":
                    work = new TireReplacement(date, car, cost);
                    break;
                case "Ремонт проколов":
                    work = new PunctureRepair(date, car, cost);
                    break;
                case "Балансировка колес":
                    work = new WheelBalancing(date, car, cost);
                    break;
            }

            if (work != null)
            {
                workManager.AddWork(work);
                workDataGrid.ItemsSource = null;
                workDataGrid.ItemsSource = workManager.GetWorks();
            }
        }
    }
}