$I = 0
$env:PSModulePath -split ';' |
ForEach-Object {"[{0:N}] {1}" -f $I++, $_}