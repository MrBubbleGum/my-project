   M S B A M L   `   `   `  ����  TireShopApp    TireShopApp.MainWindow   5   	   W SPresentationCore, Version=8.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=8.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35e aSystem.Windows.Controls.Ribbon, Version=8.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089R NWindowsBase, Version=8.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35F 9http://schemas.microsoft.com/winfx/2006/xaml/presentation     5   	   R NSystem.Xaml, Version=8.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	     � Title$  	Tire Shop��5   	   $	��350��6   $	��525��6(   .��5      � .+�5   
   �� $��Дата работы��6   $
��Left=�6&   $	��Top=�6A   $��	10,10,0,0q�6Y   (  "System.Windows.Controls.DatePicker  5   
   -   5          Name$ 
datePicker��5      $
��Left=�6)   $	��Top=�6D   $��
100,10,0,0q�6\   �� 5	   
   $��Автомобиль��6   $
��Left=�6%   $	��Top=�6@   $��	10,40,0,0q�6X   �� 5
   
   -   5         ��Name$ 
carTextBox��5
      $
��Left=�6&   $	��Top=�6A   $��
100,40,0,0q�6Y   $	��150��6m   �� 5   
   $��Тип работы��6   $
��Left=�6%   $	��Top=�6@   $��	10,70,0,0q�6X   �� 5   
   -   5         ��Name$ workTypeComboBox��5      $
��Left=�6-   $	��Top=�6H   $��
100,70,0,0q�6`   $	��150��6t   .@�5      �� $��Замена шин��6   �� 5      $#��Ремонт проколов��6   �� 5      $)��#Балансировка колес��6   5      �� 5   
   $��Стоимость��6   $
��Left=�6$   $	��Top=�6?   $��
10,100,0,0q�6W   �� 5   
   -   5        $ costTextBox��5      $
��Left=�6'   $	��Top=�6B   $��100,100,0,0q�6Z   $	��150��6o   �� 5   
   -   5        $#��Добавить работу��5      $
��Left=�6+   $	��Top=�6F   $��
10,130,0,0q�6^   $	��150��6r   6~   &   System.Windows.Controls.DataGrid  5   
   -   5          Name$ workDataGrid��5      $
��Left=�6)   $	��Top=�6D   $��
10,160,0,0q�6\   $	��500��6p   $	��150��6|   5      5      