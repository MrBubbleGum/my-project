namespace TravelApp
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            dateTimePickerStart = new DateTimePicker();
            dateTimePickerEnd = new DateTimePicker();
            comboBoxTripType = new ComboBox();
            comboBoxTransportType = new ComboBox();
            textBoxTrips = new TextBox();
            textBoxStats = new TextBox();
            buttonAddTrip = new Button();
            buttonShowStats = new Button();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            label5 = new Label();
            label6 = new Label();
            SuspendLayout();
            // 
            // dateTimePickerStart
            // 
            dateTimePickerStart.Location = new Point(160, 25);
            dateTimePickerStart.Name = "dateTimePickerStart";
            dateTimePickerStart.Size = new Size(200, 23);
            dateTimePickerStart.TabIndex = 0;
            // 
            // dateTimePickerEnd
            // 
            dateTimePickerEnd.Location = new Point(160, 83);
            dateTimePickerEnd.Name = "dateTimePickerEnd";
            dateTimePickerEnd.Size = new Size(200, 23);
            dateTimePickerEnd.TabIndex = 1;
            // 
            // comboBoxTripType
            // 
            comboBoxTripType.FormattingEnabled = true;
            comboBoxTripType.Location = new Point(208, 134);
            comboBoxTripType.Name = "comboBoxTripType";
            comboBoxTripType.Size = new Size(121, 23);
            comboBoxTripType.TabIndex = 2;
            // 
            // comboBoxTransportType
            // 
            comboBoxTransportType.FormattingEnabled = true;
            comboBoxTransportType.Location = new Point(208, 173);
            comboBoxTransportType.Name = "comboBoxTransportType";
            comboBoxTransportType.Size = new Size(121, 23);
            comboBoxTransportType.TabIndex = 3;
            // 
            // textBoxTrips
            // 
            textBoxTrips.Location = new Point(605, 72);
            textBoxTrips.Multiline = true;
            textBoxTrips.Name = "textBoxTrips";
            textBoxTrips.ScrollBars = ScrollBars.Vertical;
            textBoxTrips.Size = new Size(183, 187);
            textBoxTrips.TabIndex = 4;
            // 
            // textBoxStats
            // 
            textBoxStats.Location = new Point(401, 72);
            textBoxStats.Multiline = true;
            textBoxStats.Name = "textBoxStats";
            textBoxStats.ScrollBars = ScrollBars.Vertical;
            textBoxStats.Size = new Size(176, 186);
            textBoxStats.TabIndex = 5;
            // 
            // buttonAddTrip
            // 
            buttonAddTrip.Location = new Point(37, 227);
            buttonAddTrip.Name = "buttonAddTrip";
            buttonAddTrip.Size = new Size(126, 31);
            buttonAddTrip.TabIndex = 6;
            buttonAddTrip.Text = "Добавить поездку";
            buttonAddTrip.UseVisualStyleBackColor = true;
            buttonAddTrip.Click += buttonAddTrip_Click;
            // 
            // buttonShowStats
            // 
            buttonShowStats.Location = new Point(207, 227);
            buttonShowStats.Name = "buttonShowStats";
            buttonShowStats.Size = new Size(153, 32);
            buttonShowStats.TabIndex = 7;
            buttonShowStats.Text = "Показать статистику ";
            buttonShowStats.UseVisualStyleBackColor = true;
            buttonShowStats.Click += buttonShowStats_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(35, 31);
            label1.Name = "label1";
            label1.Size = new Size(77, 15);
            label1.TabIndex = 15;
            label1.Text = "Дата начала:";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(36, 89);
            label2.Name = "label2";
            label2.Size = new Size(98, 15);
            label2.TabIndex = 16;
            label2.Text = "Дата окончания:";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(37, 137);
            label3.Name = "label3";
            label3.Size = new Size(77, 15);
            label3.TabIndex = 17;
            label3.Text = "Тип поездки:";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(37, 181);
            label4.Name = "label4";
            label4.Size = new Size(96, 15);
            label4.TabIndex = 18;
            label4.Text = "Тип транспорта:";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(441, 43);
            label5.Name = "label5";
            label5.Size = new Size(98, 15);
            label5.TabIndex = 19;
            label5.Text = "Список поездок:";
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Location = new Point(660, 43);
            label6.Name = "label6";
            label6.Size = new Size(71, 15);
            label6.TabIndex = 20;
            label6.Text = "Статистика:";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(label6);
            Controls.Add(label5);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(buttonShowStats);
            Controls.Add(buttonAddTrip);
            Controls.Add(textBoxStats);
            Controls.Add(textBoxTrips);
            Controls.Add(comboBoxTransportType);
            Controls.Add(comboBoxTripType);
            Controls.Add(dateTimePickerEnd);
            Controls.Add(dateTimePickerStart);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private DateTimePicker dateTimePickerStart;
        private DateTimePicker dateTimePickerEnd;
        private ComboBox comboBoxTripType;
        private ComboBox comboBoxTransportType;
        private TextBox textBoxTrips;
        private TextBox textBoxStats;
        private Button buttonAddTrip;
        private Button buttonShowStats;
        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
        private Label label5;
        private Label label6;
    }
}
