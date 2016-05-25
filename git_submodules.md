## adding a gitsubmodule ##
add sub module to root of the git repo,

`
git submodlue add https://URL
`
or add submodule to spesific subdirectory,
`
git submodule add https://URL local/path/of/module
`

In either case a new version controlled file will be added ".gitmodules"
this file contains the localpath the URL and other settings for the module.
After adding the module it will be cloned into that location as a git
repository.

## Cloneing a project with submodules ##
If you clone a project that has a submodule the contents of the sub module will
not normaly be cloned automaticaly. You can either after cloning the repo run
the commands,
`
git submodule init
git submodule update
`
or you can automaticaly download submodules when cloning by adding the flag
"--recursive" for example,
`
git clone --recursive https://github.com/NuGrid/Sandbox
`

