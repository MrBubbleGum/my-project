
Set fso = CreateObject("Scripting.FileSystemObject")
Set WshShell = CreateObject("WScript.Shell")
WScript.Echo "Enter source folder path:"
sourceFolder = WScript.StdIn.ReadLine
WScript.Echo "Enter destination folder path:"
destinationFolder = WScript.StdIn.ReadLine
WScript.Echo "Enter file extension (e.g., .txt, .jpg):"
fileExtension = WScript.StdIn.ReadLine
If sourceFolder = "" Or destinationFolder = "" Or fileExtension = "" Then
    WScript.Echo "Error: Missing parameters. All parameters (source folder, destination folder, file extension) must be provided."
    WScript.Quit
End If

If Not fso.FolderExists(sourceFolder) Then
    WScript.Echo "Error: Source folder does not exist."
    WScript.Quit
End If

If Not fso.FolderExists(destinationFolder) Then
    WScript.Echo "Error: Destination folder does not exist."
    WScript.Quit
End If
command = "robocopy """ & sourceFolder & """ """ & destinationFolder & """ *" & fileExtension & " /E /Z /R:3 /W:5"
WshShell.Run command, 0, True
WScript.Echo "Backup completed."
