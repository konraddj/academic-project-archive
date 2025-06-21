# Download PowerShell 7 installation script
Set-Location C:\Users\konra\'OneDrive - Atlantic TU'\PowerShell
$URI = "https://aka.ms/install-powershell.ps1"
Invoke-RestMethod -Uri $URI | 
Out-File -FilePath C:\Users\konra'\OneDrive - Atlantic TU'\PowerShell\Install-PowerShell.ps1