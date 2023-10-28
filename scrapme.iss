[Setup]
AppName=ScrapME
AppVersion=1.0
DefaultDirName={pf}\ScrapMe
OutputDir=C:\Users\SHHEKO\Desktop\project\project
OutputBaseFilename=ScrapMe
DisableDirPage=yes
DisableProgramGroupPage=yes
DefaultGroupName=ScrapME


[Files]
Source: "C:\Users\SHHEKO\Desktop\project\project\main.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\SHHEKO\Desktop\project\project\downloadimagesfromexcel.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\SHHEKO\Desktop\project\project\exportdatatoexcelfile.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\SHHEKO\Desktop\project\project\scrapdata.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\SHHEKO\Desktop\project\project\MyApp.spec"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{commondesktop}\ScrapME"; Filename: "{app}\main.py"; WorkingDir: "{app}"

