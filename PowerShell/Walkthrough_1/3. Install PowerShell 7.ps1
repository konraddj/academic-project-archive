#set up the parameters in a variable for install PowerShell 7
$MYPARMS = @{
    UseMSI = $true
    Quiet = $true
    AddExplorerContextMenu = $true
    EnablePSRemoting = $true
}
C:\Users\konra\'OneDrive - Atlantic TU'\PowerShell\Install-PowerShell.ps1 @MYPARMS