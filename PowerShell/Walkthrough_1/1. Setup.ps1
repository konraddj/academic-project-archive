# Check the existing version
$PSVersiontable
# Set an execution policy
Set-ExecutionPolicy RemoteSigned -Force
# Install Nuget as a package provider
Install-PackageProvider Nuget -MinimumVersion 2.8.5.201 -Force | Out-Null
# Install the module
  