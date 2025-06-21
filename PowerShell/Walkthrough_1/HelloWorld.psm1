$MyModulePath = "C:\Users\$env:USERNAME\Documents\Powershell\Modules\HelloWorld" #does not works, 
#need to determine the user-specific path to the directory/directories with modules
#determine where to install your module using one of the paths stored in the $ENV: PSModulePath by running the command:
#$Env:PSModulePath
$MyModule = @"
# HelloWorld.PSM1
Function Get-HelloWorld {
    "Hello World from KDJ"
}
"@
New-Item -Path $MyModulePath -ItemType Directory -Force | Out-Null
$MyModule | Out-File -FilePath $MyModulePath\HelloWorld.PSM1
Get-Module -Name HelloWorld -ListAvailable