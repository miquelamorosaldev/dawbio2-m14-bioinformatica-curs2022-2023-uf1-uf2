# VSCode Debug HowTo
-------------------------------------------------------------------------------

# 1. Create launch.json
- Open a .py file in VSCode
- Open the 'Debug' panel to the left.
- Click 'create .json configuration'
- It will automatically create a .vscode/launch.json file
- This file will enable all the Debug configurations.
  They will appear at the top of the Debug panel, in an foldable list.

# 2. Edit launch.json
- When executing code, VS Code uses the workspace dir as the working directory.
- You can edit launch.json to make it use another dir.
- Example 1 PHP:

        {
            "name": "Launch Rewriter",
            "type": "php",
            "request": "launch",
            "runtimeArgs": [
                "-dxdebug.mode=debug",
                "-dxdebug.start_with_request=yes",
                "-S",
                "localhost:8080",
                "-t",
                "${fileDirname}/../../public",
                "${file}"
            ],
            "program": "",
            "cwd": "${workspaceRoot}",
            "port": 9003,
            "serverReadyAction": {
                "pattern": "Development Server \\(http://localhost:([0-9]+)\\) started",
                "uriFormat": "http://localhost:%s",
                "action": "openExternally"
            }
        }

- Example 2 FLASK:

{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "app.py",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true,
            "justMyCode": true
        },
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${fileDirname}",
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}

-------------------------------------------------------------------------------
