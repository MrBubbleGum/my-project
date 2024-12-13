Dim fso, objShell, sourceFile, destinationFolder, programPath, desktopPath, s

' Инициализация объектов
Set fso = CreateObject("Scripting.FileSystemObject")
Set objShell = CreateObject("WScript.Shell")

Do
    ' Вывод меню
    WScript.Echo "menu:"
    WScript.Echo "1. Information"
    WScript.Echo "2. Copy"
    WScript.Echo "3. Create"
    WScript.Echo "4. Exit"

    ' Чтение ввода от пользователя
    s = WScript.StdIn.ReadLine

    ' Обработка выбранного пункта меню
    If (s = "1") Then
        WScript.Echo "Info:"
        WScript.Echo "Vazhnaya Yana Ivanovna"
        WScript.Echo "ITI-21"
        WScript.Echo "Description of actions: Copying files, creating shortcuts on the desktop."

    ElseIf (s = "2") Then
        ' Копирование файлов с использованием команды xcopy
        WScript.Echo "File path:"
        sourceFile = WScript.StdIn.ReadLine
        WScript.Echo "Folder path:"
        destinationFolder = WScript.StdIn.ReadLine
    
        If sourceFile = "" Or destinationFolder = "" Then
            WScript.Echo "Null."
        ElseIf Not fso.FileExists(sourceFile) Then
            WScript.Echo "File err."
        ElseIf Not fso.FolderExists(destinationFolder) Then
            WScript.Echo "Folder err."
        Else
            ' Используем команду xcopy через WshShell для копирования файла
            Set WshShell = CreateObject("WScript.Shell")
            
            ' Формируем команду для копирования с параметрами
            command = "xcopy """ & sourceFile & """ """ & destinationFolder & """ /Y /I"
            
            ' Выполняем команду
            WshShell.Run command, 0, True ' 0 - скрытое окно, True - ждать завершения
    
            WScript.Echo "File copied using xcopy."
        End If
    

    ElseIf (s = "3") Then
        ' Создание ярлыка на рабочем столе
        desktopPath = objShell.SpecialFolders("Desktop")
        
        WScript.Echo "Enter the full path to the program you want to create a shortcut for:"
        programPath = WScript.StdIn.ReadLine

        If programPath = "" Then
            WScript.Echo "Error path."
        Else
            If fso.FileExists(programPath) Then
                ' Проверяем, существует ли уже ярлык
                If fso.FileExists(desktopPath & "\MyProgram.lnk") Then
                    WScript.Echo "Early created."
                Else
                    ' Создаем ярлык
                    Set objShortcut = objShell.CreateShortcut(desktopPath & "\MyProgram.lnk")
                    objShortcut.TargetPath = programPath
                    objShortcut.WorkingDirectory = fso.GetParentFolderName(programPath)
                    objShortcut.IconLocation = programPath
                    objShortcut.Save
                    WScript.Echo "Created."
                End If
            Else
                WScript.Echo "Error."
            End If
        End If

    ElseIf (s = "4") Then
        ' Выход из программы
        WScript.Echo "Exit."
        Exit Do
    Else
        WScript.Echo "Error"
    End If

Loop
