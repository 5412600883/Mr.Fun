[Setup]
AppName=SupportApp
AppVersion=1.0
DefaultDirName={pf}\SupportApp
DefaultGroupName=SupportApp
OutputBaseFilename=SupportAppInstaller
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin

[Files]
Source: "C:\Users\Furkan ozan\Desktop\gh\lara.ps1"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Furkan ozan\Desktop\gh\support_app.exe"; DestDir: "{app}"; Flags: ignoreversion



[Icons]
Name: "{group}\SupportApp"; Filename: "{app}\support_app.exe"


[Run]
Filename: "powershell.exe"; Parameters: "-ExecutionPolicy Bypass -File ""{app}\lara.ps1"""; Flags: runhidden
Filename: "{app}\support_app.exe"; Flags: nowait postinstall

[UninstallDelete]
Type: files; Name: "{app}\support_app.exe"
Type: files; Name: "{app}\lara.ps1"



