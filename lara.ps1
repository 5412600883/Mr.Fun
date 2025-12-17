$AppPath = "$PSScriptRoot\support_app.exe"
$TaskName = "SupportAppAutoStart"

# Eski görev varsa sil
if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

# Yeni görev oluştur
$Action = New-ScheduledTaskAction -Execute $AppPath
$Trigger = New-ScheduledTaskTrigger -AtStartup
Register-ScheduledTask -Action $Action -Trigger $Trigger -TaskName $TaskName -Description "Runs Support App at startup" -User "SYSTEM" -RunLevel Highest

