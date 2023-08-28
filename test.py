# import os
# import sys
# import win32com.shell.shell as shell
# ASADMIN = 'asadmin'

# if sys.argv[-1] != ASADMIN:
#     script = os.path.abspath(sys.argv[0])
#     params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
#     shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
#     sys.exit(0)

# import shutil
# import os

# source_file = "vid_player.py"
# target_dir = "C:\\AdminDir\\"

# try:
#     # Copy the file to the target directory
#     shutil.copy(source_file, target_dir)
#     print("File copied successfully.")
# except Exception as e:
#     print("Error:", e)

# import ctypes, sys

# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False

# if is_admin():
#     # Code of your program here
#     pass
# else:
#     # Re-run the program with admin rights
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

<code>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Percentage Bar</title>
  <style>
    /* Embedded CSS Styles */
    .percentage-bar {
      width: 100%;
      height: 20px;
      background-color: #1a1a1a;
      border-radius: 5px;
      position: relative;
      margin-top: 20px;
      border: 2px dotted #ffffff;
    }

    .progress {
      width: 70%; /* Adjust this value to set the percentage */
      height: 100%;
      background-color: #ffffff; /* Change color for progress */
      border-radius: 5px;
    }
    .text {
       font-family: Arial, Helvetica, sans-serif;
       font-size: larger;
       color: #ffffff;

    }
  </style>
</head>
<body>
    <p class="text"> Houdini </p>
  <div class="percentage-bar">
    <div class="progress"></div>
  </div>
</body>
</html>

</code>