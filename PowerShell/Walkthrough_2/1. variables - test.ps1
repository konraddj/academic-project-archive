$Rubbish = 1, 2, "a", "££"
$Rubbish
clear-variable -Name Rubbish
$Rubbish
Remove-Variable -Name Rubbish
[int]$Rubbish = 1
$Rubbish = "123456789"
$Rubbish
[int]$Rubbish = 1
$Rubbish = "This will give you an error!"
$Rubbish.GetType()
$Rubbish
[datetime]$OGGI = "12/25/2022"
$OGGI